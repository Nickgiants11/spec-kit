---
description: "New campaign strategy - Test new markets or offers with fresh research"
---

# /buzzlead.new-campaign [client-name] [campaign-name]

> Use Case 2: Active Client - New Campaign Strategy, New Scraping

## Purpose
When an existing client wants to test a new market, new offer, or new persona strategy, conduct fresh research and build new company/contact lists specifically for this campaign.

## Prerequisites
- Client already exists in `.buzzlead/clients/[client-name]/`
- Client profile.md is up to date
- Clear campaign objective defined

## Workflow

### Phase 1: Campaign Brief
1. Create campaign directory:
   ```
   .buzzlead/clients/[client-name]/campaigns/[campaign-name]/
   ├── brief.md
   ├── raw/
   ├── companies/
   └── contacts/
   ```

2. Define campaign brief:
   ```markdown
   # Campaign: [campaign-name]

   ## Objective
   [What is this campaign testing?]

   ## Target Market Changes
   - New industries:
   - New geographies:
   - New company sizes:

   ## Target Persona Changes
   - New titles:
   - New departments:
   - New seniority levels:

   ## Offer/Messaging Focus
   [What's the angle for this campaign?]

   ## Success Metrics
   - Target company count:
   - Target contact count:
   - Expected response rate:
   ```

### Phase 2: Delta Research
**Goal**: Understand what's different from existing ICP and identify optimal data sources

**Prompt to execute**:
```
Client: {{CLIENT_NAME}}
Existing ICP: {{EXISTING_PROFILE}}
New Campaign: {{CAMPAIGN_BRIEF}}

Analyze the delta between existing ICP and new campaign requirements:

1. What's DIFFERENT in this campaign?
   - New industries not previously targeted
   - New geographies
   - Different company profiles
   - Different personas

2. Which existing data can be REUSED?
   - Qualified accounts that fit new criteria
   - Existing contacts with relevant titles

3. What NEW data sources are needed?
   - Best sources for new industries
   - Sources for new geographies
   - Sources for new personas

4. Recommended approach:
   - Can we filter existing qualified accounts?
   - Do we need full fresh scraping?
   - Hybrid approach?

Return a campaign data strategy.
```

### Phase 3: Company Sourcing

#### Option A: Filter Existing + New Scraping
If some existing qualified accounts fit:

1. **Query existing RevyOps data**:
   - Pull companies matching new criteria
   - Filter existing qualified_accounts by new ICP

2. **Identify gaps**:
   - What's missing from existing data?
   - Which segments need fresh scraping?

3. **Targeted scraping** for gaps only

#### Option B: Full Fresh Scraping
If entirely new market:

1. **Execute scraping** based on research:
   - [ ] Source 1: [specify]
   - [ ] Source 2: [specify]
   - [ ] Source 3: [specify]

2. **Collect in campaign folder**:
   ```
   campaigns/[campaign-name]/raw/
   ├── source1_export.csv
   ├── source2_export.csv
   └── source3_export.csv
   ```

### Phase 4: Company Processing
1. **Map fields** - normalize to standard schema

2. **Merge & deduplicate**:
   - Within new sources
   - Against existing client data (avoid re-contacting)

3. **Enrich** missing fields

4. **Output**: `campaign_draft_accounts.csv`

### Phase 5: Company Qualification

**Check if client has campaign-specific qualification rules**:
```
Does this campaign require different qualification criteria?
- Standard client ICP scoring?
- Modified criteria for new market?
- Campaign-specific qualification prompt?
```

1. **Run exclusion check**:
   - Standard exclusions
   - Previous campaign contacts (90-day rule)

2. **Score ICP fit**:
   - Use campaign-specific criteria if defined
   - Otherwise use standard client ICP

3. **Human review**:
   - Review edge cases
   - Confirm qualification decisions

4. **Push qualified companies to RevyOps**:
   - Tag with campaign name
   - Track separately from main list

5. **Output**: `campaign_qualified_accounts.csv`

### Phase 6: Persona & Contact Sourcing

1. **Define campaign personas**:
   - Are these different from standard personas?
   - New title patterns to search?
   - New seniority targets?

2. **Contact sourcing strategy**:
   ```
   Based on campaign personas:

   Persona 1: [Title pattern]
   - Source: Apollo/AI Ark/LinkedIn
   - Priority: P1

   Persona 2: [Title pattern]
   - Source: Apollo/AI Ark/LinkedIn
   - Priority: P2
   ```

3. **Execute contact scraping** (human-approved):
   - [ ] Apollo API
   - [ ] AI Ark API
   - [ ] LinkedIn via Clay

### Phase 7: Contact Qualification

1. **Normalize names**

2. **Score titles** against campaign personas:
   - May differ from standard client personas
   - Use campaign-specific title relevance

3. **Check against 90-day cooling period**:
   ```python
   # Check Airtable for recent contacts
   recent_contacts = get_contacts_contacted_within_days(90)
   new_contacts = filter_out_recent(campaign_contacts, recent_contacts)
   ```

4. **Validate emails**

5. **Verify LinkedIn** (optional based on volume)

6. **Output**: `campaign_qualified_contacts.csv`

### Phase 8: Campaign Delivery

1. **Store in Airtable**:
   - Tag with campaign name
   - Link to client record
   - Record source and date

2. **Push to EmailBison** (human-approved):
   - Create new sequence for campaign
   - Or add to existing sequence

3. **Update campaign tracking**:
   ```markdown
   ## Campaign Results
   - Companies scraped: X
   - Companies qualified: Y
   - Contacts scraped: Z
   - Contacts qualified: W
   - Sources used: [list]
   - Date completed: [date]
   ```

## Outputs

| File | Location | Description |
|------|----------|-------------|
| brief.md | campaigns/[campaign]/ | Campaign definition |
| campaign_draft_accounts.csv | campaigns/[campaign]/ | Raw company list |
| campaign_qualified_accounts.csv | campaigns/[campaign]/ | Qualified companies |
| campaign_qualified_contacts.csv | campaigns/[campaign]/ | Qualified contacts |

## Human Approval Checkpoints

- [ ] Campaign brief approved
- [ ] Data strategy approved (filter existing vs new scraping)
- [ ] Company qualification reviewed
- [ ] Persona strategy approved
- [ ] Contact scraping initiated
- [ ] Final contact list approved
- [ ] Push to EmailBison approved

## Usage

```bash
# Start new campaign for existing client
/buzzlead.new-campaign "ClientName" "Q1-Enterprise-Test"

# Claude will:
# 1. Create campaign folder
# 2. Guide through brief creation
# 3. Analyze delta from existing ICP
# 4. Coordinate data collection
# 5. Produce campaign-specific lists
```
