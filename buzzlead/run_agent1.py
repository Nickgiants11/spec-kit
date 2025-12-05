#!/usr/bin/env python3
"""
Buzzlead GTM Automation - Agent 1: Deep Research Runner

Command-line interface for running deep research on a new client.

Usage:
    python -m buzzlead.run_agent1 --client "ProductEVO" --onboarding onboarding.json
    python -m buzzlead.run_agent1 --client "ProductEVO" --interactive

Trigger:
    /deep-research [client_name]
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Optional

from .agents.agent1_deep_research import DeepResearchAgent, OnboardingData
from .utils.config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def load_onboarding_from_file(path: Path) -> OnboardingData:
    """Load onboarding data from JSON file."""
    if not path.exists():
        raise FileNotFoundError(f"Onboarding file not found: {path}")

    with open(path) as f:
        data = json.load(f)

    return OnboardingData.from_dict(data)


def create_interactive_onboarding() -> OnboardingData:
    """Create onboarding data interactively."""
    print("\n" + "=" * 50)
    print("BUZZLEAD DEEP RESEARCH - CLIENT ONBOARDING")
    print("=" * 50 + "\n")

    # Required fields
    company_name = input("Company name: ").strip()
    website = input("Website URL: ").strip()

    # Optional fields with defaults
    industry = input("Industry (optional): ").strip()
    offer_summary = input("What do they sell? (brief description): ").strip()
    pricing_range = input("Pricing range (optional): ").strip()

    # Lists
    print("\nEnter target industries (comma-separated, or press Enter to skip):")
    target_industries_input = input("Target industries: ").strip()
    target_industries = [i.strip() for i in target_industries_input.split(",") if i.strip()]

    print("\nEnter target job titles (comma-separated, or press Enter to skip):")
    job_titles_input = input("Job titles: ").strip()
    job_titles = [t.strip() for t in job_titles_input.split(",") if t.strip()]

    employee_range = input("\nCompany size (employee range, e.g., '50-200'): ").strip()

    print("\nEnter pain points you solve (comma-separated, or press Enter to skip):")
    pain_points_input = input("Pain points: ").strip()
    pain_points = [p.strip() for p in pain_points_input.split(",") if p.strip()]

    print("\nEnter sample ideal client URLs (comma-separated, or press Enter to skip):")
    sample_clients_input = input("Sample client URLs: ").strip()
    sample_clients = [u.strip() for u in sample_clients_input.split(",") if u.strip()]

    print("\nEnter DNC domains to exclude (comma-separated, or press Enter to skip):")
    dnc_input = input("DNC domains: ").strip()
    dnc_domains = [d.strip() for d in dnc_input.split(",") if d.strip()]

    return OnboardingData(
        company_name=company_name,
        website=website,
        industry=industry,
        offer_summary=offer_summary,
        pricing_range=pricing_range,
        target_industries=target_industries,
        job_titles=job_titles,
        employee_range=employee_range,
        pain_points=pain_points,
        sample_ideal_clients=sample_clients,
        dnc_domains=dnc_domains,
    )


def print_checkpoint_summary(summary: str):
    """Print the checkpoint summary for human review."""
    print("\n" + summary)
    print("\nWaiting for human approval...")

    while True:
        response = input("\nEnter decision [A]pprove / [R]evise / [Q]uit: ").strip().upper()
        if response in ("A", "APPROVE"):
            print("\n✓ Approved. Ready to proceed to Agent 2 (GTM Strategy Generator)")
            print("  Run: /gtm-strategy [client_name]")
            return True
        elif response in ("R", "REVISE"):
            print("\n→ Revision requested. Please update onboarding data and re-run.")
            return False
        elif response in ("Q", "QUIT"):
            print("\n✗ Research aborted.")
            return False
        else:
            print("Invalid input. Please enter A, R, or Q.")


def main(args: Optional[argparse.Namespace] = None):
    """Main entry point for Agent 1."""
    if args is None:
        parser = argparse.ArgumentParser(
            description="Buzzlead Agent 1: Deep Research",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  python -m buzzlead.run_agent1 --client "ProductEVO" --onboarding data/productevo.json
  python -m buzzlead.run_agent1 --interactive
  python -m buzzlead.run_agent1 --client "ProductEVO" --skip-synthesis
            """,
        )
        parser.add_argument(
            "--client",
            type=str,
            help="Client name (overrides onboarding file)",
        )
        parser.add_argument(
            "--onboarding",
            type=Path,
            help="Path to onboarding JSON file",
        )
        parser.add_argument(
            "--interactive",
            action="store_true",
            help="Enter onboarding data interactively",
        )
        parser.add_argument(
            "--skip-synthesis",
            action="store_true",
            help="Skip LLM synthesis (for testing/debugging)",
        )
        parser.add_argument(
            "--env-file",
            type=Path,
            help="Path to .env file with API keys",
        )
        parser.add_argument(
            "--verbose",
            "-v",
            action="store_true",
            help="Enable verbose logging",
        )
        args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Load or create onboarding data
    if args.interactive:
        onboarding = create_interactive_onboarding()
    elif args.onboarding:
        logger.info(f"Loading onboarding from {args.onboarding}")
        onboarding = load_onboarding_from_file(args.onboarding)
    else:
        print("Error: Either --onboarding or --interactive is required")
        sys.exit(1)

    # Override client name if provided
    if args.client:
        onboarding.company_name = args.client

    if not onboarding.company_name:
        print("Error: Client name is required")
        sys.exit(1)

    print(f"\n{'=' * 50}")
    print(f"STARTING DEEP RESEARCH: {onboarding.company_name}")
    print(f"{'=' * 50}\n")

    try:
        # Initialize agent
        agent = DeepResearchAgent.from_env(args.env_file)

        # Run research
        result = agent.run(
            onboarding=onboarding,
            skip_synthesis=args.skip_synthesis,
        )

        # Output results
        print(f"\n{'=' * 50}")
        print("RESEARCH COMPLETE")
        print(f"{'=' * 50}")
        print(f"\nOutput files saved to: {result['output_path']}")
        print("  - intelligence_doc.md")
        print("  - intelligence_doc.json")
        print("  - client_case_studies.md")
        print("  - cost_log.json")

        # Human checkpoint
        if print_checkpoint_summary(result["checkpoint_summary"]):
            print(f"\nNext step: /gtm-strategy {onboarding.company_name}")

        return result

    except ValueError as e:
        print(f"\nConfiguration Error: {e}")
        print("\nMake sure you have set up your API keys:")
        print("  1. Copy buzzlead/secrets/.env.example to buzzlead/secrets/.env")
        print("  2. Fill in your API keys")
        sys.exit(1)
    except Exception as e:
        logger.exception("Research failed with error")
        print(f"\nError: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
