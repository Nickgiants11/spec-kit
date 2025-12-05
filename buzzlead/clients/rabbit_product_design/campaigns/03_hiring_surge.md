# Campaign Brief: Hiring Surge = Capacity Gap
**Client:** Rabbit Product Design
**Generated:** December 5, 2024
**Status:** Draft - Pending Approval
**Priority:** 3 (Medium-High)

---

## Target Audience

```yaml
campaign_name: "Hiring Surge Capacity Gap"
target:
  industries:
    - "Consumer Electronics"
    - "Smart Home / IoT"
    - "Fitness Equipment"
    - "Kitchen Appliances"
    - "Outdoor Products"
    - "Home Goods"
  company_size:
    employees_min: 20
    employees_max: 200
    revenue_min: "$5M"
    revenue_max: "$50M"
  personas:
    - title_keywords: ["VP Engineering", "VP Product", "Director of Engineering", "Director of Product Development"]
      seniority: "VP/Director"
      department: "Engineering/Product"
    - title_keywords: ["Head of Hardware", "Head of R&D", "Engineering Manager"]
      seniority: "Director/Manager"
      department: "Engineering/R&D"
  geography:
    countries: ["United States"]
    regions: []
  technologies:
    - "SolidWorks"
    - "Altium"
  keywords_in_profile:
    - "hardware"
    - "mechanical engineering"
    - "product development"
```

---

## Trigger Event

```yaml
trigger:
  name: "Multiple Hardware Engineering Job Postings (3+ in 30 days)"
  description: "Company is actively hiring multiple hardware engineers, indicating growth but also capacity constraints during the ramp-up period. Hiring takes 3-6 months; they need help now."
  signal_source: "LinkedIn Jobs, Indeed, Greenhouse, company careers page"
  search_query: 'site:linkedin.com/jobs "{{company_name}}" (mechanical engineer OR hardware engineer OR product designer)'
  urgency: "high"
  decay_rate: "90 days - once roles are filled, urgency decreases"
```

---

## Pain Point

```yaml
pain_point:
  problem: "Scaling hardware team but hiring takes 3-6 months; current team is underwater with projects"
  symptom: "Delayed projects, overworked engineers, quality slipping, missing deadlines"
  cost_of_inaction: "Product delays, team burnout, missed market window, competitors gain ground"
  client_solution: "Instant senior engineering capacity without the hiring timeline—engineers with 27 years avg experience ready to start now"
```

---

## Proof Point

```yaml
proof_point:
  case_study: "N/A - No B2B case studies available"
  one_liner: "N/A"
  relevance: "N/A"
  fallback: "Our engineers average 27 years experience—instant senior capacity without the 6-month hiring cycle. No commitment to keep them on payroll once the project is done."
```

---

## Enrichment Sources (For Agent 4)

```yaml
enrichment_sources:
  - source: "linkedin_jobs"
    tool: "serperdev"
    query: 'site:linkedin.com/jobs "{{company_name}}" (mechanical engineer OR hardware engineer OR product designer OR firmware)'
    extract: ["job_titles", "job_count", "posting_dates", "seniority_level"]
    use_in_copy: "{{hiring_roles}}"

  - source: "careers_page"
    tool: "spider"
    url_pattern: "/careers OR /jobs"
    extract: ["open_roles", "team_descriptions", "tech_stack"]
    use_in_copy: "{{hiring_signal}}"
    trigger_relevance: "Multiple hardware roles = capacity gap"

  - source: "company_homepage"
    tool: "jina"
    extract: ["company_description", "product_types", "team_size"]
    use_in_copy: "{{company_context}}"

  - source: "linkedin_company"
    tool: "serperdev"
    query: 'site:linkedin.com/company "{{company_name}}"'
    extract: ["employee_count", "recent_hires", "growth_rate"]
    use_in_copy: "{{company_growth}}"
```

---

## Copywriting Guidance (For Agent 5)

```yaml
copywriting:
  primary_template: "Classic Twist"
  primary_rationale: "Reference their hiring activity (shows research), then pivot to the capacity gap problem"

  secondary_template: "Direct Report"
  secondary_rationale: "Engineering leaders prefer direct communication without fluff"

  tertiary_template: "Internal Nudge"
  tertiary_rationale: "Frame as colleague-to-colleague suggestion about solving capacity problem"

  tone: "peer"
  length: "short (300-400 chars)"

  hooks_to_test:
    - "Looks like you're scaling the hardware team—saw several engineering roles open. While you're ramping up, we can provide senior firepower without the hiring timeline..."
    - "Noticed you're hiring [specific roles]. Most teams in that situation tell us the same thing: projects are stacking up faster than they can backfill..."
    - "3 mechanical engineering roles open usually means the team is underwater. We work with a lot of companies in the same spot..."
```

---

## AI Arc Filters (For Agent 3)

```json
{
  "ai_arc_filters": {
    "company_search": {
      "industries": ["Consumer Electronics", "Hardware", "IoT", "Smart Home", "Fitness", "Outdoor", "Kitchen Appliances"],
      "employee_count_min": 20,
      "employee_count_max": 200,
      "revenue_min": "5M",
      "revenue_max": "50M",
      "locations": ["United States"],
      "keywords": ["hardware", "product", "consumer electronics", "IoT"],
      "exclude_keywords": ["software", "SaaS", "automotive", "aerospace", "defense"],
      "hiring_status": "actively_hiring"
    },
    "people_search": {
      "title_keywords": ["VP Engineering", "VP Product", "Director Engineering", "Director Product", "Head of Hardware", "Head of R&D"],
      "seniority_levels": ["VP", "Director"],
      "departments": ["Engineering", "Product", "R&D"],
      "profile_keywords": ["hardware", "mechanical", "product development"]
    },
    "export_options": {
      "include_email": true,
      "email_confidence_min": 0.8,
      "max_results": 400
    }
  }
}
```

---

## Campaign Metrics Targets

- **List size:** 400 contacts
- **Expected reply rate:** 2-3%
- **Expected meeting rate:** 55-65% of replies
- **Estimated meetings:** 4-8

---

## Notes & Considerations

1. **Verify the job postings are current** - Stale postings reduce relevance
2. **Count the roles** - 3+ hardware roles = strong signal; 1-2 = weaker
3. **Identify specific roles** to reference in email (e.g., "Saw you're hiring a Senior Mechanical Engineer and Product Designer...")
4. **Best when combined with funding trigger** - Post-funding + hiring = very high intent
5. **Build list via LinkedIn Jobs search** - Filter by "hardware" OR "mechanical" OR "product designer" + company name
6. **Emphasize "no hiring commitment"** - They get senior capacity without adding to headcount long-term
