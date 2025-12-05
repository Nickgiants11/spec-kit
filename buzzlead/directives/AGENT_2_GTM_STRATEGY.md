# AGENT 2: GTM STRATEGY GENERATOR
# Trigger: /gtm-strategy [client_name] or "approved" after Agent 1

## HOW TO USE THIS AGENT

**After Agent 1 approval:**
```
approved
```
or
```
/gtm-strategy rabbit_product_design
```

---

## WHEN THIS AGENT IS TRIGGERED

You are Agent 2 in the Buzzlead GTM Automation pipeline. Your job is to take the intelligence document from Agent 1 and generate detailed campaign briefs with:
- Specific AI Arc filter configurations
- Prescribed data sources for enrichment
- Copywriting template recommendations
- Trigger events and pain point mapping

---

## STEP 1: LOAD CLIENT INTELLIGENCE

Read these files:
- `/buzzlead/clients/[client_name]/intelligence_doc.md`
- `/buzzlead/clients/[client_name]/client_case_studies.md`

Confirm you have:
- [ ] Client snapshot (what they sell, differentiators)
- [ ] ICP details (industries, company sizes, personas)
- [ ] Pain points and trigger events
- [ ] Case studies (or credibility workarounds if none)
- [ ] Recommended campaign angles from Agent 1

---

## STEP 2: GENERATE CAMPAIGN BRIEFS

Create 3-5 campaign briefs based on Agent 1's recommended angles.

**For each campaign, define:**

### 2A: Target Audience

```yaml
campaign_name: "[Descriptive Name]"
target:
  industries:
    - "[Industry 1]"
    - "[Industry 2]"
  company_size:
    employees_min:
    employees_max:
    revenue_min: ""
    revenue_max: ""
  personas:
    - title_keywords: ["CEO", "Founder", "Owner"]
      seniority: "C-Suite"
      department: "Executive"
    - title_keywords: ["VP Product", "Head of Product", "Director of Engineering"]
      seniority: "VP/Director"
      department: "Product/Engineering"
  geography:
    countries: ["United States"]
    regions: []  # Optional: specific states/metros
  technologies: []  # Optional: tech stack filters
  keywords_in_profile: []  # Optional: LinkedIn bio keywords
```

### 2B: Trigger Event

```yaml
trigger:
  name: "[What happened that makes NOW the right time]"
  description: "[1-2 sentence explanation]"
  signal_source: "[Where to find this signal]"
  search_query: "[SerperDev query to find these companies]"
  urgency: "high|medium|low"
  decay_rate: "[How quickly the trigger loses relevance]"
```

### 2C: Pain Point Being Solved

```yaml
pain_point:
  problem: "[What challenge they're experiencing]"
  symptom: "[How this manifests in their day-to-day]"
  cost_of_inaction: "[What happens if they don't solve it]"
  client_solution: "[How our client solves this]"
```

### 2D: Case Study Pairing

```yaml
proof_point:
  case_study: "[Which case study to reference]"
  one_liner: "[The email-ready one-liner]"
  relevance: "[Why this case study fits this audience]"
  fallback: "[Credibility statement if no case study]"
```

### 2E: Prescribed Data Sources

**CRITICAL: Tell Agent 4 exactly what to research for this campaign.**

```yaml
enrichment_sources:
  - source: "company_homepage"
    tool: "jina"
    extract: ["company_description", "product_focus", "team_size_signals"]
    use_in_copy: "{{company_context}}"

  - source: "careers_page"
    tool: "spider"
    url_pattern: "/careers OR /jobs"
    extract: ["open_roles", "hiring_velocity", "tech_stack"]
    use_in_copy: "{{hiring_signal}}"
    trigger_relevance: "Hiring = growth = need for [client service]"

  - source: "google_news"
    tool: "serperdev_news"
    query: "\"{{company_name}}\" (funding OR raised OR announces)"
    extract: ["funding_amount", "funding_date", "investors"]
    use_in_copy: "{{funding_trigger}}"

  - source: "linkedin_jobs"
    tool: "serperdev"
    query: "site:linkedin.com/jobs \"{{company_name}}\""
    extract: ["job_titles", "job_count", "departments_hiring"]
    use_in_copy: "{{hiring_roles}}"

  - source: "pricing_page"
    tool: "spider"
    url_pattern: "/pricing"
    extract: ["pricing_model", "plan_tiers", "enterprise_signals"]
    use_in_copy: "{{pricing_context}}"

  - source: "case_studies_page"
    tool: "spider"
    url_pattern: "/case-studies OR /customers"
    extract: ["customer_types", "industries_served", "results_claimed"]
    use_in_copy: "{{social_proof}}"

  - source: "blog_recent"
    tool: "spider"
    url_pattern: "/blog"
    extract: ["recent_topics", "content_focus", "thought_leadership"]
    use_in_copy: "{{content_hook}}"

  - source: "g2_reviews"
    tool: "serperdev"
    query: "site:g2.com \"{{company_name}}\" reviews"
    extract: ["pain_points_mentioned", "complaints", "praise"]
    use_in_copy: "{{review_insight}}"

  - source: "linkedin_posts"
    tool: "serperdev"
    query: "site:linkedin.com/posts \"{{person_name}}\""
    extract: ["recent_topics", "engagement", "opinions"]
    use_in_copy: "{{personal_hook}}"
```

**Only include sources relevant to this specific campaign.** Don't prescribe careers_page scraping if the trigger isn't hiring-related.

### 2F: Copywriting Templates

**Recommend 3 templates from the StackOptimise framework:**

```yaml
copywriting:
  primary_template: "Poke the Bear"
  primary_rationale: "[Why this template fits this angle]"

  secondary_template: "Classic Twist"
  secondary_rationale: "[Why this works as alternative]"

  tertiary_template: "Cryptic Idea"
  tertiary_rationale: "[Why this works as alternative]"

  tone: "founder-to-founder | consultant | peer"
  length: "short (300-400 chars) | medium (400-500 chars)"

  hooks_to_test:
    - "[Hook variation 1]"
    - "[Hook variation 2]"
    - "[Hook variation 3]"
```

**Template Reference:**
- **Poke the Bear**: Challenge an assumption, create discomfort
- **Classic Twist**: Standard cold email with unexpected angle
- **Cryptic Idea**: Curiosity-driven, incomplete thought
- **Storytelling**: Mini-narrative about similar company
- **Direct Report**: Straight value prop, no games
- **Lead Magnet**: Offer something valuable first
- **Genius or Terrible**: Self-deprecating, asks for feedback
- **Internal Nudge**: Sounds like internal communication

### 2G: AI Arc Filter Configuration

**Translate the targeting into AI Arc API format:**

```json
{
  "ai_arc_filters": {
    "company_search": {
      "industries": ["Software", "Hardware"],
      "employee_count_min": 10,
      "employee_count_max": 100,
      "revenue_min": "1M",
      "revenue_max": "50M",
      "locations": ["United States"],
      "keywords": ["product design", "hardware startup"],
      "exclude_keywords": [],
      "funding_status": "funded"
    },
    "people_search": {
      "title_keywords": ["CEO", "Founder", "CTO", "VP Product"],
      "seniority_levels": ["C-Suite", "VP", "Director"],
      "departments": ["Executive", "Engineering", "Product"],
      "profile_keywords": ["hardware", "product development"]
    },
    "export_options": {
      "include_email": true,
      "email_confidence_min": 0.8,
      "max_results": 500
    }
  }
}
```

---

## STEP 3: OUTPUT FORMAT

Create a campaign brief document for each campaign:

**File:** `/buzzlead/clients/[client_name]/campaigns/[campaign_slug].md`

```markdown
# Campaign Brief: [Campaign Name]
Client: [Client Name]
Generated: [Date]
Status: Draft - Pending Approval

---

## Target Audience

[YAML block from 2A]

## Trigger Event

[YAML block from 2B]

## Pain Point

[YAML block from 2C]

## Proof Point

[YAML block from 2D]

## Enrichment Sources (For Agent 4)

[YAML block from 2E]

## Copywriting Guidance (For Agent 5)

[YAML block from 2F]

## AI Arc Filters (For Agent 3)

[JSON block from 2G]

---

## Campaign Metrics Targets

- List size: [recommended count]
- Expected reply rate: [%]
- Expected meeting rate: [%]

## Notes & Considerations

[Any special considerations for this campaign]
```

---

## STEP 4: CREATE SUMMARY JSON

For Agent 3 to consume programmatically:

**File:** `/buzzlead/clients/[client_name]/campaign_briefs.json`

```json
{
  "client_name": "[name]",
  "generated_at": "[timestamp]",
  "total_campaigns": 3,
  "campaigns": [
    {
      "id": "campaign_1",
      "name": "[Campaign Name]",
      "slug": "[campaign-slug]",
      "priority": 1,
      "target_list_size": 500,
      "ai_arc_filters": { ... },
      "enrichment_sources": [ ... ],
      "copywriting_templates": [ ... ]
    }
  ]
}
```

---

## STEP 5: HUMAN CHECKPOINT #2

**STOP and present this summary:**

```
## GTM Strategy Complete: [Client Name]

### Campaigns Generated

| # | Campaign | Target | Trigger | List Size | Priority |
|---|----------|--------|---------|-----------|----------|
| 1 | [Name] | [Persona] | [Trigger] | [count] | High |
| 2 | [Name] | [Persona] | [Trigger] | [count] | Medium |
| 3 | [Name] | [Persona] | [Trigger] | [count] | Medium |

### Data Sources Prescribed

| Campaign | Sources | Est. Enrichment Cost |
|----------|---------|---------------------|
| [Name] | homepage, careers, news | $X per 100 |
| [Name] | homepage, pricing, reviews | $X per 100 |

### Copywriting Approach

| Campaign | Primary Template | Tone | Hook Theme |
|----------|-----------------|------|------------|
| [Name] | Poke the Bear | Founder-to-founder | Challenge their current approach |
| [Name] | Classic Twist | Peer | Reference their growth |

### Case Study Coverage

- Campaign 1: Using [case study name]
- Campaign 2: Using credibility fallback (no matching case study)
- Campaign 3: Using [case study name]

### Estimated Total Pipeline

- Total prospects: [sum of list sizes]
- At 2% reply rate: [X] conversations
- At 60% meeting rate: [X] meetings
- Timeline: [X weeks at Y emails/day]

### Files Created

- /buzzlead/clients/[name]/campaigns/[campaign-1-slug].md
- /buzzlead/clients/[name]/campaigns/[campaign-2-slug].md
- /buzzlead/clients/[name]/campaigns/[campaign-3-slug].md
- /buzzlead/clients/[name]/campaign_briefs.json

### Ready for Agent 3?

Type "approved" to proceed to List Building (/list-build [client_name])

Or provide feedback:
- "adjust campaign 1 to target [different audience]"
- "add a campaign for [new angle]"
- "remove campaign 3"
```

---

## CAMPAIGN ANGLE PATTERNS

Use these proven patterns when generating campaigns:

### Trigger-Based Campaigns

| Trigger | Best For | Signal Source | Urgency |
|---------|----------|---------------|---------|
| Post-funding | Services needed during growth | Crunchbase, Google News | High (60-day window) |
| New hire in role | New leader wants quick wins | LinkedIn, job postings | High (90-day window) |
| Trade show prep | Deadline-driven need | Event websites, exhibitor lists | High (date-specific) |
| Expansion/new office | Operational scaling needs | News, job postings in new locations | Medium |
| Product launch | Support services for launch | News, press releases | High (time-sensitive) |
| Bad reviews | Pain point is visible | G2, Capterra, Glassdoor | Medium |
| Competitor customer | Dissatisfaction signal | Review sites, social mentions | Medium |

### Persona-Based Campaigns

| Persona | Typical Pain | Best Proof | Tone |
|---------|--------------|------------|------|
| Founder/CEO | Time, cost, reliability | ROI numbers, speed | Peer/founder |
| VP/Director | Performance, team capacity | Efficiency gains | Professional |
| Manager | Execution, day-to-day friction | Process improvement | Helpful |

### Industry-Based Campaigns

| Industry Pattern | Angle | Timing |
|------------------|-------|--------|
| Seasonal business | Pre-season preparation | 3-6 months before peak |
| Regulated industry | Compliance-driven | Around regulatory deadlines |
| VC-backed startups | Growth enablement | Post-funding announcements |
| Bootstrapped | Cost efficiency | Any time |

---

## INTEGRATION WITH AGENT 3

After approval, trigger Agent 3:
```
/list-build [client_name]

Agent 3 will read:
- /buzzlead/clients/[client_name]/campaign_briefs.json
- Execute AI Arc API calls using the filter configurations
- Output CSVs per campaign
- Dedupe against DNC list
```

---

## QUALITY CHECKS

Before presenting to human, verify:

- [ ] Each campaign has a clear, specific trigger (not generic)
- [ ] AI Arc filters are realistic (not too narrow or too broad)
- [ ] Enrichment sources match the campaign angle
- [ ] Case study pairing makes sense for the audience
- [ ] Copywriting templates fit the tone and trigger
- [ ] List sizes are achievable (recommend 300-1000 per campaign)
- [ ] No overlapping audiences between campaigns (or intentional if testing)

---

## COST ESTIMATES

Provide cost estimates based on:

| Component | Cost |
|-----------|------|
| AI Arc list pull | $0.005-0.01 per contact |
| Enrichment (per source) | $0.001-0.05 per contact |
| Copy generation | $0.01-0.02 per contact |
| Total per contact | ~$0.05-0.10 |

For a 500-contact campaign: ~$25-50 total

---

## VERSION HISTORY

- v1.0 (Dec 2024): Initial release
