# Buzzlead GTM Automation System

A conversational B2B lead generation system that runs through Claude Code. No Python scripts, no terminal commands - just directives that Claude Code follows.

## How It Works

1. You trigger an agent (e.g., `/deep-research`)
2. You paste the client onboarding data
3. Claude Code reads the directive and executes each step
4. Claude Code makes API calls, scrapes websites, synthesizes research
5. Claude Code outputs the results and waits for your approval

## Agent Pipeline

| Agent | Trigger | Description | Status |
|-------|---------|-------------|--------|
| 1 | `/deep-research` | Comprehensive client and market research | Ready |
| 2 | `/gtm-strategy` | Campaign brief creation | Planned |
| 3 | `/build-list` | Lead list generation | Planned |
| 4 | `/enrich-data` | Contact enrichment | Planned |
| 5 | `/generate-copy` | Email copy creation | Planned |

## Quick Start

### Run Agent 1: Deep Research

```
/deep-research

Client: ProductEVO
Website: https://productevo.com
Industry: Manufacturing / Product Sourcing
What they sell: Helps companies source and manufacture products overseas
Target industries: DTC Brands, Hardware Startups, E-commerce
Target titles: Founder, CEO, VP Operations, Head of Supply Chain
Company size: 10-100 employees
Pain points: Need to scale manufacturing, quality issues with suppliers, high costs
Sample ideal clients: https://allbirds.com, https://away.com, https://casper.com
```

Claude Code will then:
1. Scrape the client website
2. Search for news and market context
3. Analyze sample ideal clients
4. Extract case studies
5. Synthesize into an intelligence document
6. Present a summary for your approval

## Directory Structure

```
buzzlead/
├── directives/           # Agent instruction files
│   └── AGENT_1_DEEP_RESEARCH.md
├── clients/              # Client data and outputs
│   ├── .templates/       # Onboarding examples
│   └── [client_name]/    # Generated per client
│       ├── intelligence_doc.md
│       └── client_case_studies.md
├── knowledge/            # Reference materials
│   ├── buzzlead_proof_points.md
│   └── copywriting_templates.md
├── secrets/              # API keys (gitignored)
│   └── api_keys.env
└── README.md
```

## APIs Used

- **Jina** - Homepage scraping (~$0.001/call)
- **Spider** - Deep page scraping (~$0.01/page)
- **SerperDev** - Google search/news (~$0.001/search)
- **OpenRouter** - GPT-5.1 synthesis (~$0.02/call)

Estimated cost per client: **$2-5**

## Human Checkpoints

Each agent stops for approval before proceeding:

```
## Deep Research Complete: ProductEVO

### Top 3 Campaign Angles
1. Post-Funding Trigger - targeting Founders
2. Scale Pain - targeting VPs of Operations
3. Cost Reduction - targeting Supply Chain leads

### Ready for Agent 2?
Type "approved" to proceed, or provide feedback.
```
