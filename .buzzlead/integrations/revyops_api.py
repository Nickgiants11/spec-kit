"""
RevyOps API Integration Module
Handles pushing company data from CSV to RevyOps.com API

This is the Buzzlead production integration for RevyOps.
"""
import json
import time
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Callable

import pandas as pd
import requests


# API Configuration
REVYOPS_BASE_URL = "https://app.revyops.com/api"
REVYOPS_POST_ENDPOINT = f"{REVYOPS_BASE_URL}/public/companies"
REVYOPS_GET_ENDPOINT = f"{REVYOPS_BASE_URL}/public/companies"

# Path to secrets
SECRETS_DIR = Path(__file__).parent.parent / "secrets"
REVYOPS_KEYS_FILE = SECRETS_DIR / "revyops_keys.json"


# Column mapping: CSV column name -> RevyOps custom field name
CUSTOM_FIELD_MAPPING = {
    "LinkedIn URL": "LinkedIn URL",
    "Industry": "Industry",
    "Employee Count": "Employee Count",
    "Description": "Description",
    "Estimated Revenue": "Estimated Revenue",
    "Keywords": "Keywords",
    "Tagline": "Tagline",
    "Website URL": "Website URL",
    "Subindustry": "Subindustry",
    "City": "City",
    "State": "State",
    "Country": "Country",
    "Location": "Location",
    "Address": "Address",
    "Zip Code": "Zip Code",
    "Technologies Used": "Technologies Used",
    "Twitter URL": "Twitter URL",
    "Founded Date": "Founded Date",
    "Facebook URL": "Facebook URL",
    "All Social URL's": "ALL Social URL's",
    "Phone Number": "Phone Number",
    "General Emails": "General Email(s)",
    "IPO Status": "IPO Status",
    "Business Type": "Business Type",
    "Rating": "Rating",
    "Review Count": "Review Count",
    "Number of Locations": "Number of Locations",
    "Source": "Source",
    "Total Funding": "Total Funding",
    "Last Funding Date": "Last Funding Date",
    "Last Funding Amount": "Last Funding Amount",
    "Funding Stage": "Funding Stage",
    "Number of Founders": "Number of Founders",
    "Founders": "Founders",
    "Client": "Client",
}

# Workspace name to key mapping
WORKSPACE_MAPPING = {
    "buzzlead": "Buzzlead",
    "product_evo": "Product EVO",
    "product evo": "Product EVO",
    "evo": "Product EVO",
    "incentive": "Incentive Solutions Corp",
    "incentive_solutions": "Incentive Solutions Corp",
    "incentive solutions": "Incentive Solutions Corp",
    "interdependence": "Interdependence",
    "idpr": "Interdependence",
    "master": "Master Account (Excludes IDPR, EVO, Incentives, Buzzlead)",
    "default": "Master Account (Excludes IDPR, EVO, Incentives, Buzzlead)",
}


def load_revyops_keys() -> Dict[str, str]:
    """Load RevyOps API keys from secrets file."""
    if not REVYOPS_KEYS_FILE.exists():
        raise FileNotFoundError(
            f"RevyOps keys file not found at {REVYOPS_KEYS_FILE}. "
            "Please create it from secrets-template.json"
        )

    with open(REVYOPS_KEYS_FILE, 'r') as f:
        return json.load(f)


def get_workspace_key(workspace_name: str) -> str:
    """
    Get the API key for a workspace by name.

    Args:
        workspace_name: Workspace name (case-insensitive, supports aliases)

    Returns:
        API key for the workspace
    """
    keys = load_revyops_keys()

    # Normalize workspace name
    normalized = workspace_name.lower().strip()

    # Check aliases
    if normalized in WORKSPACE_MAPPING:
        workspace_key = WORKSPACE_MAPPING[normalized]
    else:
        # Try exact match
        workspace_key = workspace_name

    if workspace_key not in keys:
        available = list(keys.keys())
        raise ValueError(
            f"Workspace '{workspace_name}' not found. "
            f"Available workspaces: {available}"
        )

    return keys[workspace_key]


def map_csv_row_to_revyops(row: pd.Series) -> dict:
    """
    Maps a CSV row to RevyOps JSON schema.

    Args:
        row: pandas Series representing a CSV row

    Returns:
        dict: RevyOps company data structure
    """
    company_data = {
        "domain": str(row.get("Domain", "")).strip() if pd.notna(row.get("Domain")) else "",
        "name": str(row.get("Name", "")).strip() if pd.notna(row.get("Name")) else "",
        "company_status": "",
        "company_custom_fields": []
    }

    for csv_column, field_name in CUSTOM_FIELD_MAPPING.items():
        if csv_column in row.index:
            value = row[csv_column]
            if pd.notna(value) and str(value).strip():
                company_data["company_custom_fields"].append({
                    "field_name": field_name,
                    "field_value": str(value).strip()
                })

    return company_data


def post_company_to_revyops(
    company_data: dict,
    api_key: str,
    retries: int = 2
) -> Tuple[bool, dict, int]:
    """
    Sends POST request to create a company in RevyOps.

    Args:
        company_data: Company data dictionary
        api_key: RevyOps API key
        retries: Number of retry attempts for network errors

    Returns:
        Tuple of (success: bool, response_data: dict, status_code: int)
    """
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    for attempt in range(retries + 1):
        try:
            response = requests.post(
                REVYOPS_POST_ENDPOINT,
                json=company_data,
                headers=headers,
                timeout=30
            )

            status_code = response.status_code
            try:
                response_data = response.json() if response.content else {}
            except:
                response_data = {"message": response.text}

            if status_code == 201:
                return (True, response_data, status_code)

            if status_code == 409:
                return (False, response_data, status_code)

            if status_code in [400, 403]:
                return (False, response_data, status_code)

            if status_code >= 500 and attempt < retries:
                time.sleep(1 * (attempt + 1))
                continue

            return (False, response_data, status_code)

        except requests.exceptions.RequestException as e:
            if attempt < retries:
                time.sleep(1 * (attempt + 1))
                continue
            return (False, {"error": str(e)}, 0)

    return (False, {"error": "Max retries exceeded"}, 0)


def get_company_by_domain(domain: str, api_key: str) -> Optional[dict]:
    """
    Gets a company by domain from RevyOps.

    Args:
        domain: Company domain
        api_key: RevyOps API key

    Returns:
        Company data dict if found, None otherwise
    """
    headers = {"x-api-key": api_key}

    try:
        response = requests.get(
            REVYOPS_GET_ENDPOINT,
            params={"domain": domain},
            headers=headers,
            timeout=30
        )

        if response.status_code == 200:
            companies = response.json()
            if companies and len(companies) > 0:
                return companies[0]
        return None
    except requests.exceptions.RequestException:
        return None


def patch_company_in_revyops(
    company_id: int,
    company_data: dict,
    api_key: str,
    retries: int = 2
) -> Tuple[bool, dict, int]:
    """
    Sends PATCH request to update an existing company in RevyOps.
    """
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    patch_url = f"{REVYOPS_BASE_URL}/public/companies/{company_id}"

    for attempt in range(retries + 1):
        try:
            response = requests.patch(
                patch_url,
                json=company_data,
                headers=headers,
                timeout=30
            )

            status_code = response.status_code
            try:
                response_data = response.json() if response.content else {}
            except:
                response_data = {"message": response.text}

            if status_code in [200, 204]:
                return (True, response_data, status_code)

            if status_code in [400, 403, 404]:
                return (False, response_data, status_code)

            if status_code >= 500 and attempt < retries:
                time.sleep(1 * (attempt + 1))
                continue

            return (False, response_data, status_code)

        except requests.exceptions.RequestException as e:
            if attempt < retries:
                time.sleep(1 * (attempt + 1))
                continue
            return (False, {"error": str(e)}, 0)

    return (False, {"error": "Max retries exceeded"}, 0)


def push_companies_to_revyops(
    df: pd.DataFrame,
    workspace: str,
    progress_callback: Optional[Callable[[int, int, str], None]] = None
) -> dict:
    """
    Main function to push all companies from DataFrame to RevyOps.

    Args:
        df: DataFrame with company data
        workspace: Workspace name (will be resolved to API key)
        progress_callback: Optional callback function(processed, total, status)

    Returns:
        Summary dict with success, updated, failed counts and errors list
    """
    api_key = get_workspace_key(workspace)

    summary = {
        "workspace": workspace,
        "success": 0,
        "updated": 0,
        "failed": 0,
        "errors": [],
        "created_companies": [],
        "updated_companies": []
    }

    total_rows = len(df)

    for idx, row in df.iterrows():
        if progress_callback:
            progress_callback(idx + 1, total_rows, f"Processing row {idx + 1} of {total_rows}")

        company_data = map_csv_row_to_revyops(row)

        if not company_data.get("domain") or not company_data.get("name"):
            summary["failed"] += 1
            summary["errors"].append({
                "row": idx + 1,
                "domain": company_data.get("domain", "N/A"),
                "error": "Missing required field: domain or name"
            })
            continue

        domain = company_data.get("domain", "N/A")
        company_name = company_data.get("name", "N/A")

        success, response_data, status_code = post_company_to_revyops(company_data, api_key)

        company_id = None

        if success:
            company_id = response_data.get("id") or response_data.get("company_id")

        if not company_id:
            existing_company = get_company_by_domain(domain, api_key)
            if existing_company and "id" in existing_company:
                company_id = existing_company["id"]

        if company_id:
            patch_success, patch_response, patch_status = patch_company_in_revyops(
                company_id, company_data, api_key
            )

            if patch_success:
                if success:
                    summary["success"] += 1
                    summary["updated"] += 1
                    summary["created_companies"].append({
                        "domain": domain,
                        "name": company_name,
                        "row": idx + 1,
                        "company_id": company_id
                    })
                else:
                    summary["updated"] += 1
                summary["updated_companies"].append({
                    "domain": domain,
                    "name": company_name,
                    "row": idx + 1,
                    "company_id": company_id
                })
            else:
                if success:
                    summary["success"] += 1
                    summary["created_companies"].append({
                        "domain": domain,
                        "name": company_name,
                        "row": idx + 1,
                        "company_id": company_id
                    })
                summary["failed"] += 1
                summary["errors"].append({
                    "row": idx + 1,
                    "domain": domain,
                    "error": f"PATCH failed: {patch_status} - {patch_response}"
                })
        else:
            summary["failed"] += 1
            error_msg = response_data.get("message", response_data.get("error", "Unknown error"))
            summary["errors"].append({
                "row": idx + 1,
                "domain": domain,
                "error": f"POST failed ({status_code}: {error_msg})"
            })

        time.sleep(0.5)

    return summary


def verify_companies_in_revyops(domains: List[str], workspace: str) -> dict:
    """
    Verify which companies exist in RevyOps by checking their domains.

    Args:
        domains: List of domain names to check
        workspace: Workspace name

    Returns:
        dict with found, not_found lists and details
    """
    api_key = get_workspace_key(workspace)

    verification_result = {
        "workspace": workspace,
        "found": [],
        "not_found": [],
        "errors": []
    }

    headers = {"x-api-key": api_key}

    for domain in domains:
        if not domain or domain == "N/A":
            continue

        try:
            response = requests.get(
                REVYOPS_GET_ENDPOINT,
                params={"domain": domain},
                headers=headers,
                timeout=30
            )

            if response.status_code == 200:
                companies = response.json()
                if companies and len(companies) > 0:
                    company = companies[0]
                    verification_result["found"].append({
                        "domain": domain,
                        "company_id": company.get("id"),
                        "name": company.get("name"),
                        "company_status": company.get("company_status"),
                        "updated_time": company.get("updated_time")
                    })
                else:
                    verification_result["not_found"].append(domain)
            elif response.status_code == 403:
                verification_result["errors"].append({
                    "domain": domain,
                    "error": "403 Forbidden - Invalid API key"
                })
            else:
                verification_result["not_found"].append(domain)

        except requests.exceptions.RequestException as e:
            verification_result["errors"].append({
                "domain": domain,
                "error": str(e)
            })

        time.sleep(0.3)

    return verification_result


# CLI Interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Push companies to RevyOps")
    parser.add_argument("csv_file", help="Path to CSV file")
    parser.add_argument("--workspace", "-w", required=True, help="RevyOps workspace name")
    parser.add_argument("--verify-only", action="store_true", help="Only verify, don't push")

    args = parser.parse_args()

    df = pd.read_csv(args.csv_file)

    if args.verify_only:
        domains = df["Domain"].dropna().tolist()
        result = verify_companies_in_revyops(domains, args.workspace)
        print(f"Found: {len(result['found'])}")
        print(f"Not Found: {len(result['not_found'])}")
        print(f"Errors: {len(result['errors'])}")
    else:
        def progress(current, total, status):
            print(f"\r{status}", end="", flush=True)

        result = push_companies_to_revyops(df, args.workspace, progress)
        print(f"\n\nResults for workspace: {result['workspace']}")
        print(f"Created: {result['success']}")
        print(f"Updated: {result['updated']}")
        print(f"Failed: {result['failed']}")
        if result['errors']:
            print("\nErrors:")
            for error in result['errors'][:10]:
                print(f"  Row {error['row']}: {error['error']}")
