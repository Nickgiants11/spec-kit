# Streamlit App Bridge

> Integration documentation for the Company CSV Dropbox Streamlit app.

## Overview

The Company CSV Dropbox app (https://company-csv-dropbox.streamlit.app/) is a web tool that handles:

1. **Header Mapping** - Maps inconsistent CSV column headers to standard format
2. **Data Merging** - Combines multiple data sources into one file
3. **Normalization** - Standardizes data formats
4. **Deduplication** - Removes duplicate records
5. **RevyOps Push** - Pushes clean data to RevyOps workspaces
6. **CSV Export** - Downloads clean, organized company lists

## Integration with List Intelligence System

### Workflow Position

```
Raw Scraped Files (multiple sources)
            │
            ▼
┌────────────────────────────┐
│   Company CSV Dropbox      │
│   (Streamlit App)          │
│   - Upload multiple CSVs   │
│   - Map headers            │
│   - Merge & dedupe         │
│   - Push to RevyOps        │
│   - Export clean CSV       │
└────────────────────────────┘
            │
            ▼
Qualification Layer (Agents in Claude)
```

### Data Handoff

**From Streamlit to Claude:**
1. Export merged CSV from Streamlit app
2. Save to `.buzzlead/clients/[client]/campaigns/[campaign]/companies/`
3. Run qualification agents in Claude

**From Claude to Streamlit:**
1. Generate CSV files from Claude workflows
2. Upload to Streamlit for merging with other sources
3. Push to RevyOps via Streamlit

## Standard Field Mapping

The Streamlit app and Claude agents use the same standard schema:

| Standard Field | Description |
|---------------|-------------|
| Domain | Company domain (primary key) |
| Name | Company name |
| LinkedIn URL | Company LinkedIn page |
| Industry | Primary industry |
| Subindustry | Specific segment |
| Employee Count | Number or range |
| Description | Company description |
| City | HQ city |
| State | HQ state |
| Country | HQ country |
| Source | Data source name |
| Client | Client name |

## Streamlit App Features

### 1. Header Mapping Interface
- Upload CSV with any column headers
- Visual mapping to standard fields
- Save mappings for source reuse

### 2. Multi-Source Merge
- Upload multiple CSV files
- Merge based on domain matching
- Keep best data from each source

### 3. Deduplication
- Domain-based deduplication
- Configurable merge strategy
- Keep record with most complete data

### 4. RevyOps Integration
- Select target workspace
- Push companies to RevyOps API
- View push results and errors

### 5. Export Options
- Download clean CSV
- Configurable column selection
- Standard naming convention

## API Keys for Streamlit

The Streamlit app requires RevyOps API keys. Configure in the app or use environment variables:

```
REVYOPS_KEY_BUZZLEAD=RO-xxx
REVYOPS_KEY_PRODUCT_EVO=RO-xxx
REVYOPS_KEY_INCENTIVE=RO-xxx
REVYOPS_KEY_INTERDEPENDENCE=RO-xxx
REVYOPS_KEY_MASTER=RO-xxx
```

## Future Integration Opportunities

### Direct Claude ↔ Streamlit

**Option 1: API Layer**
- Add API endpoints to Streamlit app
- Claude calls Streamlit API for merging
- Results returned to Claude

**Option 2: Shared Storage**
- Use shared cloud storage (S3, GCS)
- Claude uploads files
- Streamlit processes and returns

**Option 3: MCP Server**
- Build MCP server for Streamlit functions
- Claude accesses via MCP protocol
- Real-time integration

### Recommended Approach

For immediate use:
1. Continue using Streamlit UI for merging
2. Export CSV to local files
3. Process in Claude with qualification agents

For future automation:
1. Build API layer in Streamlit
2. Integrate as MCP server
3. Enable fully automated pipelines

## Repository Information

- **App URL**: https://company-csv-dropbox.streamlit.app/
- **GitHub Repo**: [Add your repository URL]
- **Tech Stack**: Streamlit, Python, Pandas

## Usage in Workflow

### During Client Onboarding

```
1. Scrape from multiple sources → Raw CSVs
2. Upload all CSVs to Streamlit app
3. Map headers for each source
4. Merge and deduplicate
5. Export clean CSV
6. Save to campaign folder
7. Run qualification agents in Claude
8. Push qualified list to RevyOps
```

### During Campaign Refill

```
1. Scrape new contacts
2. If from multiple sources → Use Streamlit
3. If single source → Process directly in Claude
4. Qualify in Claude
5. Push to Airtable/EmailBison
```

## Troubleshooting

### Common Issues

**Header mapping not saving:**
- Clear browser cache
- Ensure source name is unique
- Check for special characters in headers

**Merge not working correctly:**
- Verify domain column is mapped
- Check domain formatting (no http/www)
- Review merge logs for conflicts

**RevyOps push failing:**
- Verify API key is correct
- Check workspace selection
- Ensure required fields present (Domain, Name)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-24 | Initial documentation |
