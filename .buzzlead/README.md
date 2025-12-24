# Buzzlead List Building Intelligence System

> An AI-powered knowledge base and workflow system for B2B lead list building operations.

## Overview

This system provides a structured approach to list building with three main use cases:

1. **New Client Onboarding** (`/buzzlead.onboard`) - Map markets and build initial lead lists for new clients
2. **New Campaign Strategy** (`/buzzlead.new-campaign`) - Research new markets and build campaign-specific lists
3. **Campaign Refill** (`/buzzlead.refill`) - Find new contacts at already-qualified companies

## Directory Structure

```
.buzzlead/
├── README.md                 # This file
├── memory/                   # Core knowledge base
│   ├── constitution.md       # Business rules & principles
│   ├── tech-stack.md         # Tools, APIs, integrations
│   └── sops/                 # Standard Operating Procedures
│       ├── company-scraping.md
│       ├── qualification-criteria.md
│       └── data-storage.md
├── clients/                  # Client profiles & data
│   ├── _template/            # Template for new clients
│   │   ├── profile.md
│   │   ├── exclusions.md
│   │   └── campaigns/
│   └── [client-name]/        # Actual client folders
├── prompts/                  # AI agent prompts
│   ├── research/             # Market research prompts
│   │   ├── market-research.md
│   │   ├── persona-mapping.md
│   │   └── data-source-discovery.md
│   ├── qualification/        # Qualification agents
│   │   ├── company/
│   │   │   ├── icp-fit-scorer.md
│   │   │   ├── industry-classifier.md
│   │   │   ├── exclusion-checker.md
│   │   │   └── company-enricher.md
│   │   └── contact/
│   │       ├── linkedin-verifier.md
│   │       ├── title-relevance-scorer.md
│   │       └── email-validator.md
│   └── data-cleaning/        # Data processing prompts
│       ├── name-normalizer.md
│       └── field-mapper.md
├── commands/                 # Main workflow commands
│   ├── onboard.md           # New client onboarding
│   ├── new-campaign.md      # New campaign strategy
│   └── refill.md            # Campaign refill
├── integrations/            # API integrations
│   └── revyops_api.py       # RevyOps API client
└── secrets/                 # API keys (gitignored)
    ├── .gitkeep
    └── secrets-template.json # Template for keys
```

## Quick Start

### 1. Set Up Secrets

Copy the template and add your API keys:

```bash
cd .buzzlead/secrets
cp secrets-template.json api_keys.json
cp secrets-template.json revyops_keys.json
# Edit the JSON files with your actual keys
```

### 2. Create a New Client

```bash
# Copy template
cp -r clients/_template clients/[client-name]

# Edit profile.md with client ICP
# Edit exclusions.md with competitors/customers
```

### 3. Run a Use Case

```bash
# New client onboarding
/buzzlead.onboard "ClientName"

# New campaign for existing client
/buzzlead.new-campaign "ClientName" "CampaignName"

# Refill existing campaign
/buzzlead.refill "ClientName" "CampaignName"
```

## Modular Agents

The qualification agents can be used independently:

### Company Qualification
- **ICP Fit Scorer** - Score companies against client ICP (0-100)
- **Industry Classifier** - Standardize industry classifications
- **Exclusion Checker** - Filter out excluded companies
- **Company Enricher** - Fill missing company data

### Contact Qualification
- **LinkedIn Verifier** - Verify LinkedIn profiles are active
- **Title Relevance Scorer** - Score titles against personas
- **Email Validator** - Validate email deliverability

### Data Cleaning
- **Name Normalizer** - Clean and format contact names
- **Field Mapper** - Map CSV columns to standard schema

## Data Flow

```
Raw Data Sources
      │
      ▼
Company CSV Dropbox (Merge, Normalize, Dedupe)
      │
      ▼
Qualification Layer (Agents)
      │
      ▼
RevyOps (Companies) + Airtable (Contacts/History)
      │
      ▼
EmailBison (Campaign Execution)
```

## Key Integrations

| System | Purpose |
|--------|---------|
| RevyOps | Qualified company storage |
| Airtable | Contact history & tracking |
| EmailBison | Campaign sequences |
| Company CSV Dropbox | Data merging & normalization |
| MillionVerifier | Email validation |
| Debounce | Email validation (secondary) |

## Human Approval Checkpoints

The system is designed with human-in-the-loop:

- Market research approval
- Data source selection
- Scraping initiation
- Company qualification review
- Contact list approval
- Campaign push approval

## Security

- API keys stored in `secrets/` directory (gitignored)
- Client data CSV files are gitignored
- Never commit sensitive credentials
- Share client profiles via secure channels

## Support

For questions or issues:
- Check SOPs in `memory/sops/`
- Review agent prompts for detailed logic
- Contact the Buzzlead team
