from datetime import datetime
import json
import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

from services.common.logging import configure_service_logger
from services.common.neo4j import create_leads, get_company_selected_gtms
from services.common.settings import settings

app = FastAPI(
    title="Discolikes Service",
    description="Finds company data from a gtm audience description using the discolikes discover api."
)

logger = configure_service_logger("discolikes")

class DiscolikesRequest(BaseModel):
    company_id: str

from typing import Any

CONFIDENCE_THRESHOLD = 0.55
DISCOLIKE_API_KEY = "1a47f174-3e88-4f01-b419-c0c1932b0db7"

def _extract_facebook_url(links: list[dict]) -> str | None:
    for link in links:
        if "facebook" in link:
            return link
    return None

def _extract_twitter_url(links: list[dict]) -> str | None:
    for link in links:
        if "twitter" in link:
            return link
    return None

def _extract_valid_keywords(keywords: list[dict]) -> list[str]:
    valid_keywords = [k for k, v in keywords.items() if v >= CONFIDENCE_THRESHOLD]

    return valid_keywords

def _extract_valid_industry_groups(industry_groups: list[dict]) -> list[str]:
    valid_industry_groups = [k for k, v in industry_groups.items() if v >= CONFIDENCE_THRESHOLD]
    return valid_industry_groups


def _convert_to_buzzlead_company(discolike_company: dict) -> dict:
    """Convert a discolike company record to a Buzzlead company format."""
    address = discolike_company.get("address", {})
    return {
        "lead_id": str(uuid.uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "record_type": "company",
        "domain": discolike_company.get("domain", None),
        "name": discolike_company.get("name", None),
        "linkedin_url": "",
        "industries": _extract_valid_industry_groups(discolike_company.get("industry_groups", [])),
        "employee_count": discolike_company.get("employees", None),
        "description": discolike_company.get("description", None),
        "estimated_revenue": discolike_company.get("estimated_revenue", None),
        "keywords": _extract_valid_keywords(discolike_company.get("keywords", [])),
        "tagline": discolike_company.get("tagline", None),
        "website_url": discolike_company.get("domain", None),
        "subindustry": "",
        "city": address.get("city", None),
        "state": address.get("state", None),
        "country": address.get("country", None),
        "location": json.dumps({
            "latitude": address.get("latitude", None),
            "longitude": address.get("longitude", None),
        }),
        "latitude": address.get("latitude", None),
        "longitude": address.get("longitude", None),
        "address": address.get("street", None),
        "zip_code": address.get("zip", None),
        "technologies_used": [],
        "founded_date": discolike_company.get("start_date", None),
        "facebook_url": _extract_facebook_url(discolike_company.get("social_urls", None)),
        "twitter_url": _extract_twitter_url(discolike_company.get("social_urls", None)),
        "all_social_urls": discolike_company.get("social_urls", None),
        "phone_numbers": discolike_company.get("phones", None),
        "general_emails": discolike_company.get("public_emails", None),
        "ipo_status": None,
        "business_type": None,
        "rating": None,
        "review_count": None,
        "number_of_locations": None,
        "total_funding": None,
        "last_funding_date": None,
        "last_funding_amount": None,
        "funding_stage": None,
        "number_of_founders": None,
        "source": "discolikes",
        "founders": None,
    }


@app.post("/discolikes")
async def build_leads(payload: DiscolikesRequest):
    """Access the discolikes API and validate resulting companies."""
    if not payload.company_id:
        raise HTTPException(status_code=400, detail="company_id is required")

    logger.info("Building discolikes leads for %s", payload.company_id)

    # Retrieve audience_description from selected gtm
    selected_gtms = get_company_selected_gtms(payload.company_id)
    if not selected_gtms:
        raise HTTPException(
            status_code=400,
            detail="No selected GTM for company_id",
        )

    # curl "https://api.discolike.com/v1/discover?country=US&min_score=50&max_score=600&redirect=1" \
    # -H "x-discolike-key: API_KEY"

    api_key = settings.discolikes_api_key
    if not api_key:
        raise HTTPException(status_code=500, detail="Missing Discolike API key")

    min_similarity = 50
    max_records = 5
    discolike_results = []

    headers = {"x-discolike-key": api_key}
    async with httpx.AsyncClient(timeout=60.0) as client:
        for i, gtm in enumerate(selected_gtms):
            audience_description = (gtm.get("audience_description") or None).strip()
            if not audience_description:
                raise HTTPException(
                    status_code=400,
                    detail="No audience description found in selected GTM",
                )

            logger.info("Selected GTM %d", i)
            params = {
                "country": "US",
                "min_similarity": min_similarity,
                "max_records": max_records,
                "redirect": 1,
                "icp_text": audience_description,
            }
            keywords = gtm.get("audience_keywords") or []
            if keywords:
                params["keyword"] = keywords

            response = await client.get("https://api.discolike.com/v1/discover", params=params, headers=headers)
            response.raise_for_status()
            buzzlead_companies = []
            for company in response.json():
                discolike_results.append(company)
                buzzlead_companies.append(_convert_to_buzzlead_company(company))
                logger.info("Discolike response for GTM %d: %s", i, company.get("name"))
            create_leads(payload.company_id, gtm["strategy_id"], buzzlead_companies)


    return {
        "status": "created leads",
        "company_id": payload.company_id,
        "discolike_responses": discolike_results,
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8009)
