# Buzzlead GTM Automation System

A comprehensive B2B lead generation research and campaign automation system. This system automates the process of researching new clients, generating campaign strategies, building lead lists, and creating personalized cold email copy.

## Agent Pipeline

| Agent | Name | Description | Status |
|-------|------|-------------|--------|
| 1 | Deep Research | Comprehensive client and market research | Implemented |
| 2 | GTM Strategy Generator | Campaign brief creation with AI Arc filters | Planned |
| 3 | List Builder | Lead list generation via AI Arc | Planned |
| 4 | Data Enrichment | Contact enrichment and verification | Planned |
| 5 | Copy Generator | Personalized email copy creation | Planned |

## Quick Start

### 1. Setup API Keys

```bash
# Copy the example env file
cp buzzlead/secrets/.env.example buzzlead/secrets/.env

# Edit with your API keys
nano buzzlead/secrets/.env
```

Required API keys:

- `JINA_API_KEY` - For homepage scraping
- `SPIDER_API_KEY` - For deep page scraping
- `SERPER_DEV_API_KEY` - For Google search/news
- `OPENROUTER_API_KEY` - For LLM synthesis

### 2. Install Dependencies

```bash
pip install requests python-dotenv
```

### 3. Run Agent 1 (Deep Research)

**Option A: With onboarding file**

```bash
python -m buzzlead.run_agent1 --client "ProductEVO" --onboarding buzzlead/clients/.templates/productevo_example.json
```

**Option B: Interactive mode**

```bash
python -m buzzlead.run_agent1 --interactive
```

**Option C: Skip synthesis (for testing)**

```bash
python -m buzzlead.run_agent1 --client "TestCo" --onboarding data.json --skip-synthesis
```

## Directory Structure

```
buzzlead/
├── agents/                    # Agent implementations
│   ├── __init__.py
│   └── agent1_deep_research.py
├── clients/                   # Client-specific data and outputs
│   ├── .templates/           # Onboarding templates
│   │   ├── onboarding_template.json
│   │   └── productevo_example.json
│   └── [client_name]/        # Generated per client
│       ├── intelligence_doc.md
│       ├── intelligence_doc.json
│       ├── client_case_studies.md
│       └── cost_log.json
├── knowledge/                 # Knowledge base files
│   ├── buzzlead_proof_points.md
│   └── copywriting_templates.md
├── secrets/                   # API keys (gitignored)
│   ├── .env.example
│   └── .env                   # Your actual keys (create this)
├── utils/                     # Shared utilities
│   ├── __init__.py
│   ├── api_clients.py
│   ├── config.py
│   └── cost_tracker.py
├── __init__.py
├── run_agent1.py              # CLI entry point
└── README.md
```

## Agent 1: Deep Research

### Trigger

```
/deep-research [client_name]
```

### Inputs Required

1. **Client Onboarding Form** (JSON) containing:
   - Company name and website
   - What they sell (offer description)
   - Target industries
   - Target job titles/personas
   - Company size ranges
   - Geographic focus
   - Pain points they solve
   - Case studies/results achieved
   - Sample ideal client URLs (5-10)
   - DNC domains list

### Workflow

1. **Parse Onboarding Form** - Extract and structure client data
2. **Scrape Client Website** - Homepage via Jina, key pages via Spider
3. **Research Client Context** - News and market research via SerperDev
4. **Analyze Sample Clients** - Scrape and analyze ideal customer profiles
5. **Extract Case Studies** - Structure proof points for cold emails
6. **Synthesize Research** - Use LLM to create intelligence document
7. **Human Checkpoint** - Present summary for approval

### Outputs

| File | Description |
|------|-------------|
| `intelligence_doc.md` | Full narrative intelligence document |
| `intelligence_doc.json` | Structured data for Agent 2 |
| `client_case_studies.md` | Case studies formatted for cold emails |
| `cost_log.json` | API usage and cost tracking |

### Cost Estimates

| API | Cost per 1,000 contacts |
|-----|------------------------|
| Jina | ~$1 |
| Spider | ~$10 |
| SerperDev | ~$1-2 |
| OpenRouter | ~$15-20 |

## Onboarding Form Schema

See `buzzlead/clients/.templates/onboarding_template.json` for the full schema.

Minimum required fields:

```json
{
  "client": {
    "company_name": "Required",
    "website": "Required"
  }
}
```

## Human Checkpoints

Agent 1 includes a human checkpoint after research synthesis:

```
============================================
HUMAN CHECKPOINT #1: Research Review
============================================

CLIENT: ProductEVO
DATA QUALITY SCORE: 8/10

TOP 3 RECOMMENDED CAMPAIGN ANGLES:
1. Post-Funding Trigger
2. Scale Pain
3. Cost Reduction

DECISION REQUIRED:
[ ] APPROVE - Proceed to Agent 2
[ ] REVISE - Make adjustments
[ ] REJECT - Gather more information
============================================
```

## Integration with Agent 2

After approval, pass to Agent 2:

```
/gtm-strategy [client_name]
```

Agent 2 reads:

- `intelligence_doc.json`
- `client_case_studies.md`
- `knowledge/copywriting_templates.md`

## Error Handling

- **Jina fails**: Falls back to Spider for homepage
- **Spider fails**: Logs error, continues with available data
- **SerperDev fails**: Retries once, then skips query
- **OpenRouter fails**: Retries with lower max_tokens

Partial results are always saved - no data is lost due to single API failures.

## Development

### Running Tests

```bash
# Test without API calls
python -m buzzlead.run_agent1 --client "Test" --onboarding test.json --skip-synthesis
```

### Adding New Agents

1. Create agent file in `buzzlead/agents/`
2. Add to `buzzlead/agents/__init__.py`
3. Create CLI runner in `buzzlead/run_agentN.py`

## Version History

- **v1.0** (Dec 2024): Initial release with Agent 1 (Deep Research)
