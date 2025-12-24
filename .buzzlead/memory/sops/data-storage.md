# SOP: Data Storage

> Standard Operating Procedure for storing, organizing, and managing list building data.

## Overview

This SOP defines where and how data is stored across the Buzzlead systems.

---

## Storage Systems

### 1. RevyOps (Qualified Companies)

**Purpose**: Primary source of truth for qualified company data.

**What's Stored**:
- Qualified company records
- Company custom fields
- Client workspace assignment

**Organization**:
| Workspace | Clients |
|-----------|---------|
| Buzzlead | Buzzlead internal |
| Product EVO | Product EVO |
| Incentive Solutions Corp | Incentive Solutions |
| Interdependence | IDPR |
| Master Account | All other clients |

**Integration**: `.buzzlead/integrations/revyops_api.py`

**Push Process**:
```python
from integrations.revyops_api import push_companies_to_revyops
result = push_companies_to_revyops(df, workspace="ClientWorkspace")
```

---

### 2. Airtable (Contact History & Campaign Tracking)

**Purpose**: Historical tracking of contacts and campaigns.

**What's Stored**:
- All contacts ever created
- Contact status (contacted, responded, bounced)
- Campaign associations
- Last contact dates
- Source attribution

**Base Structure**:
```
Buzzlead Operations Base
├── Clients (table)
│   └── Client records with RevyOps workspace link
├── Campaigns (table)
│   └── Campaign records linked to clients
├── Contacts (table)
│   └── All contact records with campaign links
├── Companies (table)
│   └── Company reference for contact lookups
└── Contact History (table)
    └── Timestamped contact events
```

**Key Fields in Contacts**:
| Field | Purpose |
|-------|---------|
| Email | Primary identifier |
| First Name | Contact name |
| Last Name | Contact name |
| Company Domain | Links to company |
| Campaign | Which campaign |
| Source | Data source |
| Created Date | When added |
| Last Contacted | For 90-day rule |
| Status | active, bounced, unsubscribed |

**90-Day Rule Query**:
```
Filter: Last Contacted is before (today - 90 days)
```

---

### 3. EmailBison (Campaign Sequences)

**Purpose**: Active campaign execution.

**What's Stored**:
- Contacts ready for outreach
- Sequence steps and timing
- Engagement tracking

**Organization**:
- Each client has dedicated sequencer(s)
- Campaigns organized within client space

**Push Process**:
1. Export qualified contacts from Airtable
2. Import to EmailBison sequence
3. Activate campaign

---

### 4. Local File Storage (Working Data)

**Purpose**: Temporary storage during list building process.

**Location**: `.buzzlead/clients/[client]/campaigns/[campaign]/`

**Structure**:
```
campaigns/[campaign-name]/
├── brief.md              # Campaign definition
├── raw/                  # Raw scraped files
│   ├── source1.csv
│   └── source2.csv
├── companies/            # Processed company data
│   ├── draft_accounts.csv
│   └── qualified_accounts.csv
├── contacts/             # Processed contact data
│   ├── raw_contacts.csv
│   └── qualified_contacts.csv
└── reports/              # Campaign reports
    └── campaign_report.md
```

**Gitignore**:
- CSV files are gitignored (contain sensitive data)
- Only templates and documentation are committed

---

## Data Flow

### New Client Onboarding

```
1. Raw Scraping → Local: raw/
2. Merge/Dedupe → Local: companies/draft_accounts.csv
3. Qualification → Local: companies/qualified_accounts.csv
4. Push to RevyOps → RevyOps
5. Contact Scraping → Local: contacts/raw_contacts.csv
6. Contact Qualification → Local: contacts/qualified_contacts.csv
7. Push to Airtable → Airtable
8. Push to EmailBison → EmailBison
```

### Campaign Refill

```
1. Pull Qualified Companies → From RevyOps
2. Check Contact History → From Airtable
3. Scrape New Contacts → Local: contacts/
4. Dedupe vs History → Against Airtable
5. Push New Contacts → To Airtable
6. Push to EmailBison → To EmailBison
```

---

## Naming Conventions

### Files
```
[client]_[source]_[date]_[type].csv

Examples:
- acme_crunchbase_2024-01-15_raw.csv
- acme_merged_2024-01-15_draft.csv
- acme_2024-01-15_qualified.csv
- acme_contacts_2024-01-15_final.csv
```

### Campaigns
```
[objective]-[segment]-[date]

Examples:
- onboarding
- enterprise-q1-2024
- smb-test-2024-02
- refill-2024-03
```

---

## Backup & Retention

### RevyOps
- Data persisted in RevyOps cloud
- No local backup needed

### Airtable
- Data persisted in Airtable cloud
- Consider periodic exports for backup

### Local Files
- Raw files can be deleted after processing
- Keep qualified lists for reference
- Archive completed campaigns monthly

### Retention Policy
| Data Type | Retention |
|-----------|-----------|
| Raw scrapes | Delete after qualification |
| Qualified lists | Keep indefinitely |
| Contact history | Keep indefinitely (Airtable) |
| Campaign reports | Keep indefinitely |

---

## Access Control

### Secrets
- API keys in `.buzzlead/secrets/` (gitignored)
- Never commit credentials

### Client Data
- CSV files gitignored
- Client profiles may contain sensitive ICP data
- Share via secure channels only

### Team Access
- RevyOps: Add team members to workspace
- Airtable: Share base with team
- Local files: Team git access

---

## Troubleshooting

### Data Sync Issues

**RevyOps push failing**:
- Check API key validity
- Verify workspace name
- Check required fields present

**Airtable sync issues**:
- Verify API key
- Check base/table names
- Ensure field names match

### Data Quality Issues

**Duplicates appearing**:
- Run deduplication again
- Check for domain variations (www vs non-www)
- Verify merge logic

**Missing fields after push**:
- Check field mapping
- Verify source data has values
- Check RevyOps custom field names

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-24 | Initial SOP |
