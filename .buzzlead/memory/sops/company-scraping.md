# SOP: Company Scraping

> Standard Operating Procedure for collecting company data from various sources.

## Overview

This SOP covers the end-to-end process for scraping company data from multiple sources and preparing it for qualification.

---

## Pre-Scraping Checklist

- [ ] Client ICP defined and approved
- [ ] Target industries/geographies confirmed
- [ ] Data sources selected based on market research
- [ ] Search queries/filters prepared
- [ ] Output folder structure created

---

## Source-Specific Procedures

### Crunchbase Scraping

**Tool**: Python script with browser cookies

**Pre-requisites**:
- Active Crunchbase login (Pro account preferred)
- Browser cookies exported
- Script located at: `.buzzlead/integrations/crunchbase_scraper.py`

**Procedure**:
1. Log into Crunchbase in browser
2. Export cookies to script
3. Define search parameters:
   ```python
   params = {
       "industries": ["SaaS", "Enterprise Software"],
       "employee_range": "51-200",
       "funding_status": "Series A-C",
       "locations": ["United States"]
   }
   ```
4. Run scraper with rate limiting (2-3 second delays)
5. Export results to CSV

**Output fields**:
- Company name, domain, description
- Industry, employee count
- Funding info, HQ location
- LinkedIn URL

**Rate limits**: Respect 2-3 second delays, max 500 companies per session

---

### Apollo Scraping

**Tool**: Manual export or Apify actor

**Procedure (Manual)**:
1. Log into Apollo
2. Build search with filters:
   - Industries
   - Employee count
   - Location
   - Technologies (if relevant)
3. Export to CSV (max 1000 per export)
4. Repeat for additional segments

**Procedure (Apify)**:
1. Use Apollo scraper actor
2. Configure search parameters
3. Run actor, download results
4. Note: Monitor for blocks/CAPTCHAs

**Output fields**:
- Company name, domain
- Industry, employee count
- Technologies, keywords
- LinkedIn URL

---

### Google Maps Scraping

**Tool**: Serper.dev API or Apify Google Maps actor

**Best for**: Local businesses, service companies

**Procedure**:
1. Define search queries:
   ```
   "[business type] in [city, state]"
   "best [business type] [location]"
   ```
2. Run search via API
3. Extract business details
4. Deduplicate by address/phone

**Output fields**:
- Business name, address
- Phone, website
- Rating, review count
- Category

**Notes**:
- May need multiple queries per location
- Results vary by query phrasing
- Good for SMB/local business campaigns

---

### LinkedIn Company Scraping

**Tool**: Clay.com or manual

**Procedure (via Clay)**:
1. Upload company list (domains or names)
2. Use LinkedIn Company enrichment
3. Export enriched data

**Procedure (Manual)**:
1. Search LinkedIn company pages
2. Export via Sales Navigator (if available)
3. Or manually collect key data points

**Output fields**:
- Company name, LinkedIn URL
- Industry, employee count
- HQ location, description
- Follower count

---

### Discolikes / AI Ark API

**Tool**: Direct API

**Procedure**:
1. Prepare API request with search parameters
2. Make API call
3. Parse JSON response
4. Convert to standard CSV format

**API Key Location**: `.buzzlead/secrets/api_keys.json`

---

## Post-Scraping Process

### 1. Initial Review
- [ ] Verify row count matches expectations
- [ ] Check for obvious errors/blank fields
- [ ] Confirm correct data source tag

### 2. Field Mapping
- Use Company CSV Dropbox or Field Mapper agent
- Map source columns to standard schema
- Note any missing required fields

### 3. Data Cleaning
- Remove obvious non-companies (test entries, spam)
- Clean domain field (remove http, www, paths)
- Standardize country/state names

### 4. Deduplication
- Dedupe by domain (primary key)
- Keep record with most complete data
- Log duplicates removed

### 5. Source Tagging
- Add "Source" column with data source name
- Add scrape date
- Add client name

---

## Output Requirements

### File Naming Convention
```
[client]_[source]_[date]_raw.csv
Example: acme_crunchbase_2024-01-15_raw.csv
```

### Required Columns
| Column | Required | Notes |
|--------|----------|-------|
| Domain | Yes | Clean, no http/www |
| Name | Yes | Company name |
| Source | Yes | Where scraped from |
| Industry | No | If available |
| Employee Count | No | If available |
| Location | No | City, State, Country |

### Storage Location
```
.buzzlead/clients/[client]/campaigns/[campaign]/raw/
```

---

## Quality Metrics

Track for each scraping session:
- Total records scraped
- Records after dedup
- % with complete required fields
- Time to complete
- Issues encountered

---

## Troubleshooting

### Common Issues

**Rate limiting/blocks**:
- Reduce scraping speed
- Use different IP/proxy
- Split into smaller batches

**Low result count**:
- Broaden search criteria
- Try different keyword variations
- Check if source has coverage for this niche

**Poor data quality**:
- Source may not be right for this ICP
- Consider enrichment from secondary source
- Flag for human review

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-24 | Initial SOP |
