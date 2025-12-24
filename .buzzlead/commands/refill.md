---
description: "Refill campaign with new contacts at existing qualified companies"
---

# /buzzlead.refill [client-name] [campaign-name]

> Use Case 3: Active Clients - Refill campaigns with data from main ICP criteria

## Purpose
When an existing campaign is performing well but needs more contacts, find new people at already-qualified companies who haven't been contacted recently.

## Prerequisites
- Client exists in `.buzzlead/clients/[client-name]/`
- Qualified company list exists in RevyOps
- Campaign has existing contact history in Airtable

## Key Principle
**No new company research needed** - we're finding new contacts at companies we've already qualified.

## Workflow

### Phase 1: Campaign Analysis
1. **Identify the campaign** to refill:
   - Which campaign is performing well?
   - What's the current contact volume?
   - How many more contacts needed?

2. **Load existing data**:
   ```
   - Qualified companies: from RevyOps
   - Previous contacts: from Airtable
   - Current personas: from client profile
   ```

3. **Determine refill parameters**:
   ```markdown
   ## Refill Request
   - Campaign: [name]
   - Target contact volume: [X new contacts]
   - Companies to target: [all qualified / specific segment]
   - Personas to target: [same / expanded]
   - 90-day check: Required
   ```

### Phase 2: Company Selection
1. **Pull qualified companies from RevyOps**:
   ```python
   from .buzzlead.integrations.revyops_api import verify_companies_in_revyops

   # Get all qualified companies for this client
   qualified_companies = get_client_companies(client_name, workspace)
   ```

2. **Filter companies** (if targeting subset):
   - By industry segment
   - By company size
   - By performance (if tracking company-level response rates)

3. **Calculate contact headroom**:
   ```
   For each company:
   - Total contacts previously scraped
   - Contacts already contacted
   - Estimated remaining contacts available
   - Priority score (companies with more headroom = higher priority)
   ```

### Phase 3: Contact Gap Analysis
1. **Load contact history from Airtable**:
   - All contacts ever contacted for this client
   - Filter to last 90 days for cooling period

2. **Identify contacted companies**:
   ```
   Companies with recent activity (< 90 days):
   - domain1.com: 5 contacts, last touch 30 days ago
   - domain2.com: 3 contacts, last touch 15 days ago

   Companies with stale activity (> 90 days):
   - domain3.com: 4 contacts, last touch 120 days ago → ELIGIBLE
   - domain4.com: 2 contacts, last touch 200 days ago → ELIGIBLE

   Companies never contacted:
   - domain5.com: qualified but no contacts yet → PRIORITY
   ```

3. **Prioritize companies for contact scraping**:
   - Priority 1: Qualified companies with zero contacts
   - Priority 2: Companies with stale contacts (>90 days)
   - Priority 3: Companies with recent contacts but different personas

### Phase 4: Contact Scraping

**Note**: We're looking for NEW contacts, not re-scraping the same people.

1. **Define scraping strategy**:
   ```
   Option A: Same personas, new people
   - Target same titles at more companies
   - Look for additional people at same companies

   Option B: Expanded personas
   - Add new title patterns
   - Target adjacent roles
   ```

2. **Execute contact scraping** (human-approved):

   For each priority company batch:
   - [ ] Apollo API - search by company domain + target titles
   - [ ] AI Ark - enrich with additional contacts
   - [ ] LinkedIn via Clay - fill gaps

3. **Deduplication against history**:
   ```python
   # Critical: Remove anyone we've already contacted
   existing_emails = load_airtable_contacts(client_name)
   new_contacts = scrape_results[~scrape_results['email'].isin(existing_emails)]
   ```

### Phase 5: Contact Qualification

1. **Score titles** against client personas:
   - Use standard client persona definitions
   - Same scoring as original campaign

2. **Validate emails**:
   - MillionVerifier bulk check
   - Debounce for catch-alls

3. **Verify LinkedIn** (optional):
   - Confirm current employment
   - Especially for contacts scraped from older data

4. **Final 90-day check**:
   ```python
   # Double-check against Airtable one more time
   # In case contacts were added during processing
   recently_contacted = get_contacts_contacted_within_days(90, client_name)
   final_contacts = remove_recently_contacted(qualified_contacts, recently_contacted)
   ```

5. **Output**: `refill_contacts.csv`

### Phase 6: Delivery

1. **Update Airtable**:
   - Add new contacts with campaign tag
   - Mark as "ready for outreach"
   - Record source and scrape date

2. **Push to EmailBison** (human-approved):
   - Add to existing campaign sequence
   - Or create refill batch within campaign

3. **Update campaign tracking**:
   ```markdown
   ## Refill: [date]
   - Companies targeted: X
   - New contacts found: Y
   - Contacts after dedup: Z
   - Contacts after qualification: W
   - Sources used: [list]
   ```

## Outputs

| File | Location | Description |
|------|----------|-------------|
| refill_contacts.csv | campaigns/[campaign]/ | New qualified contacts |
| refill_report.md | campaigns/[campaign]/ | Refill summary |

## Human Approval Checkpoints

- [ ] Refill parameters approved
- [ ] Company selection confirmed
- [ ] Contact scraping initiated
- [ ] Final contact list approved
- [ ] Push to EmailBison approved

## Quick Mode

For simple refills where you just need more of the same:

```bash
# Quick refill - same personas, target unfilled companies
/buzzlead.refill "ClientName" "MainCampaign" --quick --target 500

# Claude will:
# 1. Pull qualified companies from RevyOps
# 2. Filter out recently contacted
# 3. Scrape contacts using standard personas
# 4. Qualify and deduplicate
# 5. Output ready-to-send list
```

## Usage

```bash
# Standard refill with full workflow
/buzzlead.refill "ClientName" "CampaignName"

# Quick refill for specific volume
/buzzlead.refill "ClientName" "CampaignName" --quick --target 1000

# Refill with expanded personas
/buzzlead.refill "ClientName" "CampaignName" --expand-personas
```
