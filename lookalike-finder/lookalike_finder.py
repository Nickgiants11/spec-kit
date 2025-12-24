#!/usr/bin/env python3
"""
Lookalike Finder CLI

Finds lookalike companies using DiscoLike API and enriches contacts via AI Ark.
"""

import argparse
import csv
import sys
import requests

DISCOLIKE_API_KEY = "1a47f174-3e88-4f01-b419-c0c1932b0db7"
AI_ARK_API_KEY = "997be5efa615474cb58afc665087cffe"

DISCOLIKE_BASE_URL = "https://api.discolike.com/v1"
AI_ARK_BASE_URL = "https://api.aiark.io/v1"


def discover_companies(query: str, is_icp: bool, limit: int) -> list[dict]:
    """Call DiscoLike API to discover lookalike companies."""
    headers = {"x-discolike-key": DISCOLIKE_API_KEY}
    params = {
        "country": "US",
        "max_records": limit,
    }

    if is_icp:
        params["icp_text"] = query
    else:
        params["domain"] = query

    response = requests.get(
        f"{DISCOLIKE_BASE_URL}/discover",
        headers=headers,
        params=params,
        timeout=60
    )
    response.raise_for_status()
    return response.json()


def enrich_people(domain: str) -> list[dict]:
    """Call AI Ark API to get people/contacts for a company domain."""
    headers = {
        "x-api-key": AI_ARK_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {"domain": domain}

    response = requests.post(
        f"{AI_ARK_BASE_URL}/people",
        headers=headers,
        json=payload,
        timeout=60
    )
    response.raise_for_status()
    return response.json()


def flatten_company(company: dict, people: list[dict] = None) -> list[dict]:
    """Flatten company data with optional people into CSV rows."""
    address = company.get("address", {}) or {}
    base_row = {
        "company_name": company.get("name", ""),
        "domain": company.get("domain", ""),
        "description": company.get("description", ""),
        "employees": company.get("employees", ""),
        "estimated_revenue": company.get("estimated_revenue", ""),
        "city": address.get("city", ""),
        "state": address.get("state", ""),
        "country": address.get("country", ""),
        "phone": ", ".join(company.get("phones", []) or []),
        "email": ", ".join(company.get("public_emails", []) or []),
    }

    if not people:
        return [base_row]

    rows = []
    for person in people:
        row = base_row.copy()
        row.update({
            "contact_name": person.get("name", ""),
            "contact_title": person.get("title", ""),
            "contact_email": person.get("email", ""),
            "contact_linkedin": person.get("linkedin_url", ""),
        })
        rows.append(row)

    return rows if rows else [base_row]


def main():
    parser = argparse.ArgumentParser(
        description="Find lookalike companies and enrich with contact data"
    )
    parser.add_argument(
        "query",
        help="ICP text description or company domain"
    )
    parser.add_argument(
        "--icp",
        action="store_true",
        help="Treat query as ICP text description (default: treat as domain)"
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=10,
        help="Maximum number of companies to return (default: 10)"
    )
    parser.add_argument(
        "--skip-people",
        action="store_true",
        help="Skip contact enrichment via AI Ark"
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output CSV file (default: stdout)"
    )

    args = parser.parse_args()

    # Discover companies
    print(f"Discovering companies for: {args.query}", file=sys.stderr)
    try:
        companies = discover_companies(args.query, args.icp, args.limit)
    except requests.RequestException as e:
        print(f"Error calling DiscoLike API: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(companies)} companies", file=sys.stderr)

    # Process companies and optionally enrich with people
    all_rows = []
    for company in companies:
        domain = company.get("domain")
        people = []

        if not args.skip_people and domain:
            print(f"Enriching contacts for {domain}...", file=sys.stderr)
            try:
                people = enrich_people(domain)
            except requests.RequestException as e:
                print(f"Warning: Could not enrich {domain}: {e}", file=sys.stderr)

        rows = flatten_company(company, people if not args.skip_people else None)
        all_rows.extend(rows)

    # Determine fieldnames based on whether we have people data
    if args.skip_people:
        fieldnames = [
            "company_name", "domain", "description", "employees",
            "estimated_revenue", "city", "state", "country", "phone", "email"
        ]
    else:
        fieldnames = [
            "company_name", "domain", "description", "employees",
            "estimated_revenue", "city", "state", "country", "phone", "email",
            "contact_name", "contact_title", "contact_email", "contact_linkedin"
        ]

    # Output CSV
    output_file = open(args.output, "w", newline="") if args.output else sys.stdout
    try:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_rows)
    finally:
        if args.output:
            output_file.close()

    print(f"Wrote {len(all_rows)} rows", file=sys.stderr)


if __name__ == "__main__":
    main()
