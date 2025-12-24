---
description: "New client onboarding - Map markets and build initial lead lists"
---

# /buzzlead.onboard [client-name]

> Use Case 1: New Client Onboarding

## Purpose
When we sign a new client and receive their completed onboarding form, conduct deep research to identify the best personas and data sources, then build the initial qualified company and contact lists.

## Prerequisites
- Client has completed Typeform onboarding
- Client profile created in `.buzzlead/clients/[client-name]/`
- RevyOps workspace assigned

## Workflow

### Phase 1: Client Profile Setup
1. Create client directory from template:
   ```
   .buzzlead/clients/[client-name]/
   ├── profile.md      # ICP, personas, criteria
   ├── exclusions.md   # Do not contact list
   └── campaigns/
       └── onboarding/
   ```

2. Populate profile.md with:
   - ICP criteria from Typeform responses
   - Target industries and subindustries
   - Company size parameters
   - Geographic targets
   - Target personas and titles
   - Any specific exclusions

### Phase 2: Market Research
**Goal**: Identify the best data sources for this client's ICP

**Prompt to execute**:
```
Based on the following client ICP:
{{CLIENT_PROFILE}}

Research and recommend:
1. The best company data sources for this ICP
   - Which sources (Crunchbase, Apollo, Google Maps, etc.) will have the best coverage?
   - Any niche sources specific to their industry?

2. Optimal search strategies for each source
   - Search queries to use
   - Filters to apply
   - Expected volume from each source

3. Estimated Total Addressable Market (TAM)
   - How many companies likely fit this ICP?
   - Geographic breakdown

4. Recommended scraping priority order
   - Start with highest-quality sources
   - Fill gaps with secondary sources

Return a structured research report with actionable next steps.
```

### Phase 3: Company Data Collection
1. **Identify data sources** based on research:
   - Primary sources (highest quality)
   - Secondary sources (gap filling)
   - Enrichment sources

2. **Execute scraping** (human-approved):
   - [ ] Crunchbase scrape (if applicable)
   - [ ] Apollo export (if applicable)
   - [ ] Google Maps scrape (if applicable)
   - [ ] Other sources as identified

3. **Collect raw data** in campaign folder:
   ```
   campaigns/onboarding/
   ├── raw/
   │   ├── crunchbase_export.csv
   │   ├── apollo_export.csv
   │   └── google_maps_export.csv
   ```

### Phase 4: Data Processing
1. **Map fields** using Field Mapper agent
   - Normalize all CSVs to standard schema

2. **Merge & deduplicate** via Company CSV Dropbox
   - Upload all source files
   - Map headers to standard format
   - Export merged, deduplicated list

3. **Enrich data** using Company Enricher agent
   - Fill missing fields
   - Standardize industries

4. **Output**: `draft_accounts.csv`

### Phase 5: Company Qualification
1. **Run exclusion check** using Exclusion Checker agent
   - Remove competitors
   - Remove existing customers
   - Remove excluded industries

2. **Score ICP fit** using ICP Fit Scorer agent
   - Score each company 0-100
   - Flag companies for review (55-69)
   - Auto-qualify high scorers (85+)
   - Auto-disqualify low scorers (<40)

3. **Human review checkpoint**:
   - Review flagged companies
   - Approve/reject edge cases
   - Confirm final qualified list

4. **Push to RevyOps**:
   ```python
   from .buzzlead.integrations.revyops_api import push_companies_to_revyops
   push_companies_to_revyops(qualified_df, workspace="[client-workspace]")
   ```

5. **Output**: `qualified_accounts.csv`

### Phase 6: Persona Mapping & Contact Scraping
1. **Define target personas** from profile.md:
   - Primary decision makers
   - Influencers
   - Title patterns to search

2. **Execute contact scraping** (human-approved):
   - [ ] Apollo API for contacts at qualified companies
   - [ ] AI Ark for additional contacts
   - [ ] LinkedIn via Clay for enrichment

3. **Collect raw contact data**:
   ```
   campaigns/onboarding/
   ├── contacts/
   │   ├── apollo_contacts.csv
   │   └── aiark_contacts.csv
   ```

### Phase 7: Contact Qualification
1. **Normalize names** using Name Normalizer agent

2. **Score titles** using Title Relevance Scorer agent
   - Score against target personas
   - Priority tier assignment

3. **Validate emails** using Email Validator agent
   - MillionVerifier for bulk validation
   - Debounce for catch-alls

4. **Verify LinkedIn** using LinkedIn Verifier agent
   - Confirm current employment
   - Flag inactive profiles

5. **Final deduplication**:
   - Remove duplicates across sources
   - Check against existing contacts in Airtable

6. **Output**: `qualified_contacts.csv`

### Phase 8: Delivery
1. **Store in Airtable** for historical tracking

2. **Push to EmailBison** sequencer (human-approved)

3. **Update campaign tracking**:
   - Log campaign in client profile
   - Record source volumes and quality metrics

## Outputs

| File | Location | Description |
|------|----------|-------------|
| profile.md | clients/[client]/ | Client ICP profile |
| draft_accounts.csv | campaigns/onboarding/ | Initial company list |
| qualified_accounts.csv | campaigns/onboarding/ | Qualified companies |
| qualified_contacts.csv | campaigns/onboarding/ | Qualified contacts |
| campaign_report.md | campaigns/onboarding/ | Summary and metrics |

## Human Approval Checkpoints

- [ ] Market research approved
- [ ] Data sources selected
- [ ] Scraping initiated
- [ ] Company qualification reviewed
- [ ] Contact scraping initiated
- [ ] Final contact list approved
- [ ] Push to EmailBison approved

## Usage

```bash
# Start new client onboarding
/buzzlead.onboard "ClientName"

# Claude will:
# 1. Create client folder structure
# 2. Guide you through profile setup
# 3. Conduct market research
# 4. Coordinate data collection and qualification
# 5. Produce qualified company and contact lists
```
