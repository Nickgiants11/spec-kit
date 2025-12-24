# Buzzlead List Building Intelligence System - Constitution

> This document defines the core principles, workflows, and business rules that govern all list building operations for Buzzlead.

## Mission

Build high-quality, targeted lead lists that maximize campaign performance for our clients by leveraging deep market research, multi-source data aggregation, and intelligent qualification processes.

---

## Core Principles

### 1. Data Quality Over Quantity
- Never sacrifice data accuracy for volume
- Every company and contact must meet qualification criteria before entering a campaign
- Duplicate prevention is mandatory at every stage
- Data normalization ensures consistency across all sources

### 2. Client-Centric Approach
- Each client has unique ICP criteria that must be respected
- Qualification prompts may vary by client - always check client-specific rules first
- Campaign history informs future list building decisions
- 90-day contact cooling period before re-engagement

### 3. Multi-Source Validation
- Never rely on a single data source for company information
- Cross-reference company data across sources when possible
- Contact data should be verified through email validation services
- LinkedIn profiles should be verified as active before outreach

### 4. Systematic Documentation
- All scraping sessions must be logged with source, date, and volume
- Qualification decisions should be traceable
- Client campaign history must be maintained in Airtable
- RevyOps serves as the single source of truth for qualified companies

### 5. Human-in-the-Loop
- AI assists with research, qualification suggestions, and data processing
- Human approval required before executing bulk data operations
- Final campaign lists require human review before EmailBison push
- Client-facing deliverables need human quality check

---

## Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        DATA SOURCES                                  │
├─────────────────────────────────────────────────────────────────────┤
│  COMPANIES                          │  CONTACTS                      │
│  ├── Crunchbase (script)           │  ├── Apollo (API)              │
│  ├── Discolikes (API)              │  ├── AI Ark (API)              │
│  ├── AI Ark (API)                  │  ├── LinkedIn (Clay)           │
│  ├── Apollo (manual)               │  └── Claygent (GPT search)     │
│  ├── LinkedIn (manual)             │                                 │
│  └── Google Maps (API)             │                                 │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    COMPANY CSV DROPBOX                               │
│  (Streamlit App - Header Mapping, Merge, Normalize, Dedupe)         │
│  https://company-csv-dropbox.streamlit.app/                         │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    QUALIFICATION LAYER                               │
│  ├── Company Qualification Agents                                    │
│  │   ├── ICP Fit Scorer                                             │
│  │   ├── Industry Classifier                                        │
│  │   ├── Size/Revenue Validator                                     │
│  │   └── Client-Specific Qualifiers                                 │
│  └── Contact Qualification Agents                                    │
│      ├── LinkedIn Active Verifier                                   │
│      ├── Title Relevance Scorer                                     │
│      ├── Email Validator (MillionVerifier/Debounce)                 │
│      └── Name Normalizer                                            │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      DATA STORAGE                                    │
│  ├── RevyOps (Qualified Companies - Source of Truth)                │
│  ├── Airtable (Historical Lists & Campaign Tracking)                │
│  └── EmailBison (Campaign Sequences)                                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Standard Field Mappings

### Company Fields (Output Format)
| Field Name | Required | Description |
|------------|----------|-------------|
| Domain | Yes | Primary identifier, must be clean (no www/https) |
| Name | Yes | Company legal/trading name |
| LinkedIn URL | No | Company LinkedIn page |
| Industry | No | Primary industry classification |
| Subindustry | No | More specific industry segment |
| Employee Count | No | Number range or exact |
| Description | No | Company description/tagline |
| Estimated Revenue | No | Revenue range |
| City | No | HQ city |
| State | No | HQ state/province |
| Country | No | HQ country |
| Website URL | No | Full website URL |
| Source | Yes | Where data was scraped from |
| Client | Yes | Which client this is for |

### Contact Fields (Output Format)
| Field Name | Required | Description |
|------------|----------|-------------|
| Email | Yes | Verified business email |
| First Name | Yes | Cleaned/normalized |
| Last Name | Yes | Cleaned/normalized |
| Title | Yes | Job title |
| Company | Yes | Company name |
| Company Domain | Yes | Links to company record |
| LinkedIn URL | No | Personal LinkedIn profile |
| Phone | No | Direct phone if available |
| Location | No | City, State, Country |
| Seniority | No | C-Level, VP, Director, Manager, etc. |
| Department | No | Sales, Marketing, Operations, etc. |

---

## RevyOps Workspace Assignments

| Workspace | API Key Reference | Clients |
|-----------|------------------|---------|
| Buzzlead | `secrets/revyops_keys.json:Buzzlead` | Buzzlead internal |
| Product EVO | `secrets/revyops_keys.json:Product EVO` | Product EVO |
| Incentive Solutions Corp | `secrets/revyops_keys.json:Incentive Solutions Corp` | Incentive Solutions |
| Interdependence | `secrets/revyops_keys.json:Interdependence` | IDPR |
| Master Account | `secrets/revyops_keys.json:Master Account` | All other clients |

---

## Qualification Workflow Standards

### Company Qualification Process
1. **Initial Filter** - Remove obvious mismatches (wrong country, size, etc.)
2. **ICP Scoring** - Score against client's ideal customer profile
3. **Industry Validation** - Confirm industry/subindustry alignment
4. **Exclusion Check** - Check against client's exclusion list
5. **Enrichment** - Fill missing fields from secondary sources
6. **Human Review** - Flag edge cases for human decision

### Contact Qualification Process
1. **Email Validation** - Verify deliverability (MillionVerifier/Debounce)
2. **LinkedIn Verification** - Confirm profile is active
3. **Title Relevance** - Score title against target personas
4. **Recency Check** - Ensure not contacted in last 90 days
5. **Name Cleaning** - Normalize names, remove titles/suffixes
6. **Deduplication** - Check against existing contact database

---

## Use Case Triggers

### Use Case 1: New Client Onboarding
**Trigger**: Client completes Typeform onboarding
**Command**: `/buzzlead.onboard [client-name]`
**Goal**: Map total addressable market, build draft accounts list, qualify, scrape contacts

### Use Case 2: Active Client - New Campaign Strategy
**Trigger**: Client requests new market/offer test
**Command**: `/buzzlead.new-campaign [client-name] [campaign-name]`
**Goal**: Research new market, build company list, identify new personas, scrape contacts

### Use Case 3: Active Client - Campaign Refill
**Trigger**: Existing campaign needs more data
**Command**: `/buzzlead.refill [client-name] [campaign-name]`
**Goal**: Find new contacts at qualified companies, respect 90-day cooling period

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-24 | Initial constitution |
