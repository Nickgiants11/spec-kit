# Buzzlead List Building Tech Stack

> Complete reference for all tools, APIs, and integrations used in the list building process.

---

## Company Data Sources

### Crunchbase
- **Type**: Web scraping via Python script
- **Authentication**: Browser cookies (manual login required)
- **Script Location**: `integrations/crunchbase_scraper.py`
- **Best For**: Funded startups, tech companies, company funding data
- **Data Available**: Company name, domain, industry, funding rounds, employee count, founders, HQ location
- **Rate Limits**: Respect 2-3 second delays between requests
- **Notes**: Session cookies expire, need periodic re-authentication

### Discolikes
- **Type**: API
- **API Key**: See `secrets/api_keys.json`
- **Documentation**: [Add URL]
- **Best For**: [Add use case]
- **Data Available**: [Add fields]

### AI Ark
- **Type**: API
- **API Key**: See `secrets/api_keys.json`
- **Best For**: Company and contact data
- **Data Available**: Companies and contacts

### Apollo
- **Type**: Manual export + 3rd party API scrapers
- **Access**: Via Apify scrapers
- **Best For**: B2B company data, contact information
- **Data Available**: Company info, employee data, technographics
- **Notes**: Use Apify actors for automated scraping

### LinkedIn
- **Type**: Manual + Clay native features
- **Access**: Clay.com integration
- **Best For**: Company profiles, employee counts, job postings
- **Data Available**: Company page data, employee listings

### Google Maps
- **Type**: API (via Serper.dev or direct)
- **API Key**: See `secrets/api_keys.json`
- **Best For**: Local businesses, service companies, location-based searches
- **Data Available**: Business name, address, phone, website, ratings, reviews

---

## Contact Data Sources

### Apollo (Contacts)
- **Type**: API
- **API Key**: See `secrets/api_keys.json`
- **Best For**: B2B contact data with verified emails
- **Data Available**: Name, title, email, phone, LinkedIn URL, company

### AI Ark (Contacts)
- **Type**: API
- **API Key**: See `secrets/api_keys.json`
- **Best For**: Contact enrichment
- **Data Available**: Contact details, company association

### LinkedIn (via Clay)
- **Type**: Clay native LinkedIn enrichment
- **Access**: Clay.com UI or API
- **Best For**: Profile data, current employment verification
- **Data Available**: Full profile data, job history, connections

### Claygent
- **Type**: ChatGPT-powered search within Clay
- **Access**: Clay.com UI
- **Best For**: Custom research, finding specific information
- **Use Cases**: Finding specific contacts, researching companies

---

## Scraping & Automation Tools

### Apify
- **Type**: Cloud scraper rental platform
- **API Key**: See `secrets/api_keys.json`
- **Documentation**: https://docs.apify.com/
- **Common Actors Used**:
  - Apollo scraper
  - LinkedIn company scraper
  - Google Maps scraper
- **Best For**: Running scrapers at scale without infrastructure

### Serper.dev
- **Type**: Google SERP API
- **API Key**: See `secrets/api_keys.json`
- **Documentation**: https://serper.dev/docs
- **Best For**: Google search results, finding company websites
- **Rate Limits**: Based on plan

### Clay.com
- **Type**: Data enrichment & automation platform
- **API Key**: See `secrets/api_keys.json`
- **Access**: Primarily UI, API available
- **Documentation**: https://docs.clay.com/
- **Best For**:
  - LinkedIn data enrichment
  - Multi-source data waterfall
  - Claygent AI research
- **Notes**: Most work done in UI, API for automation

---

## Email Verification Tools

### MillionVerifier
- **Type**: Email verification API
- **API Key**: See `secrets/api_keys.json`
- **Documentation**: https://www.millionverifier.com/api-documentation
- **Best For**: Bulk email verification
- **Response Types**: ok, catch_all, unknown, invalid, disposable
- **Recommended**: Use for initial bulk verification

### Debounce
- **Type**: Email verification API
- **API Key**: See `secrets/api_keys.json`
- **Documentation**: https://debounce.io/api-documentation/
- **Best For**: Secondary verification, catch-all handling
- **Notes**: Good for verifying catch-all emails

### Findymail
- **Type**: Email finding + verification
- **API Key**: See `secrets/api_keys.json`
- **Best For**: Finding emails from LinkedIn profiles
- **Notes**: Higher accuracy than generic email guessing

### LeadMagic
- **Type**: Email enrichment
- **API Key**: See `secrets/api_keys.json`
- **Best For**: Finding business emails
- **Notes**: Good coverage for enterprise contacts

---

## Data Storage & CRM

### RevyOps
- **Type**: Internal company data management
- **API**: REST API
- **Documentation**: See `integrations/revyops_api.py`
- **Workspaces**:
  - Buzzlead
  - Product EVO
  - Incentive Solutions Corp
  - Interdependence
  - Master Account
- **API Keys**: See `secrets/revyops_keys.json`
- **Purpose**: Store qualified company lists per client

### Airtable
- **Type**: Database for historical tracking
- **API Key**: See `secrets/api_keys.json`
- **Purpose**:
  - Campaign history
  - Historical lead lists
  - Cross-reference for 90-day cooling period
- **Base Structure**: [Document base/table structure]

### EmailBison
- **Type**: Email sequencer
- **Purpose**: Store qualified leads for campaign execution
- **Notes**: Each client has dedicated sequencer

---

## Data Processing Tools

### Company CSV Dropbox
- **Type**: Streamlit web app
- **URL**: https://company-csv-dropbox.streamlit.app/
- **Repository**: [Add GitHub URL]
- **Purpose**:
  - Map inconsistent CSV headers to standard format
  - Merge multiple data sources
  - Normalize company data
  - Deduplicate records
  - Push to RevyOps
  - Export clean CSV

---

## API Key Reference

All API keys are stored in `secrets/api_keys.json` with the following structure:

```json
{
  "apify": "apify_api_xxx",
  "serper": "xxx",
  "apollo": "xxx",
  "clay": "xxx",
  "millionverifier": "xxx",
  "debounce": "xxx",
  "findymail": "xxx",
  "leadmagic": "xxx",
  "ai_ark": "xxx",
  "discolikes": "xxx",
  "airtable": "xxx"
}
```

RevyOps keys are separate in `secrets/revyops_keys.json`.

---

## Tool Selection Guide

| Need | Primary Tool | Backup |
|------|-------------|--------|
| Tech/Funded Companies | Crunchbase | Apollo |
| Local Businesses | Google Maps | - |
| B2B Companies | Apollo | AI Ark |
| Contact Emails | Apollo | Findymail |
| Email Verification | MillionVerifier | Debounce |
| LinkedIn Data | Clay | - |
| Custom Research | Claygent | Serper.dev |
| Bulk Scraping | Apify | - |
