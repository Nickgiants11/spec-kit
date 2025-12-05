# Campaign Brief: Post-Funding Hardware Startups
**Client:** Rabbit Product Design
**Generated:** December 5, 2024
**Status:** Draft - Pending Approval
**Priority:** 1 (Highest)

---

## Target Audience

```yaml
campaign_name: "Post-Funding Hardware Startups"
target:
  industries:
    - "Consumer Electronics"
    - "Smart Home / IoT"
    - "Fitness Equipment"
    - "Kitchen Appliances"
    - "Outdoor Products"
  company_size:
    employees_min: 5
    employees_max: 100
    revenue_min: "$0"
    revenue_max: "$25M"
  personas:
    - title_keywords: ["CEO", "Founder", "Co-Founder"]
      seniority: "C-Suite"
      department: "Executive"
    - title_keywords: ["CTO", "Chief Product Officer", "VP Engineering"]
      seniority: "C-Suite/VP"
      department: "Product/Engineering"
  geography:
    countries: ["United States"]
    regions: []
  technologies:
    - "SolidWorks"
    - "Arduino"
    - "Shopify"
  keywords_in_profile:
    - "hardware"
    - "product development"
    - "IoT"
    - "consumer electronics"
```

---

## Trigger Event

```yaml
trigger:
  name: "Recent Funding Round (Seed to Series B)"
  description: "Hardware startup just raised funding and will need to scale product development, manufacturing, and engineering capacity. Post-funding is when design-to-manufacturing becomes the bottleneck."
  signal_source: "Crunchbase, TechCrunch, PR Newswire, Google News"
  search_query: '"[company_name]" (funding OR raised OR Series A OR Series B OR seed round) hardware'
  urgency: "high"
  decay_rate: "60 days - founders are most receptive in first 2 months post-funding"
```

---

## Pain Point

```yaml
pain_point:
  problem: "Need to scale product development rapidly after funding but lack senior engineering capacity"
  symptom: "Hiring takes 3-6 months, current team is overwhelmed, investors expect faster progress"
  cost_of_inaction: "Missed milestones, delayed product launch, investor pressure, burn runway without progress"
  client_solution: "Instant access to senior engineers (27 years avg experience) who can execute immediately without hiring timeline"
```

---

## Proof Point

```yaml
proof_point:
  case_study: "N/A - No B2B case studies available"
  one_liner: "N/A"
  relevance: "N/A"
  fallback: "Our engineers have brought 1,000+ products to market, averaging 27 years experience. We provide the senior firepower you need now—without the 6-month hiring cycle."
```

---

## Enrichment Sources (For Agent 4)

```yaml
enrichment_sources:
  - source: "google_news"
    tool: "serperdev_news"
    query: '"{{company_name}}" (funding OR raised OR Series)'
    extract: ["funding_amount", "funding_date", "investors", "use_of_funds"]
    use_in_copy: "{{funding_trigger}}"

  - source: "company_homepage"
    tool: "jina"
    extract: ["company_description", "product_type", "team_size_signals"]
    use_in_copy: "{{company_context}}"

  - source: "crunchbase"
    tool: "serperdev"
    query: 'site:crunchbase.com "{{company_name}}"'
    extract: ["funding_total", "investors", "employee_count"]
    use_in_copy: "{{company_stage}}"

  - source: "linkedin_company"
    tool: "serperdev"
    query: 'site:linkedin.com/company "{{company_name}}"'
    extract: ["employee_count", "recent_hires", "company_description"]
    use_in_copy: "{{company_linkedin}}"
```

---

## Copywriting Guidance (For Agent 5)

```yaml
copywriting:
  primary_template: "Classic Twist"
  primary_rationale: "Congratulatory opening disarms, then pivot to the real challenge they're about to face (scaling hardware development)"

  secondary_template: "Direct Report"
  secondary_rationale: "Post-funding founders are busy; respect their time with straight value prop"

  tertiary_template: "Storytelling"
  tertiary_rationale: "Reference similar hardware companies that faced scaling challenges post-funding"

  tone: "founder-to-founder"
  length: "short (300-400 chars)"

  hooks_to_test:
    - "Congrats on the raise. When hardware teams scale post-funding, design-to-manufacturing usually becomes the bottleneck..."
    - "Saw the funding news. Most hardware founders I talk to post-raise say hiring senior engineers is taking longer than expected..."
    - "After raising, hardware startups usually hit the same wall: great idea, not enough engineering bandwidth to execute..."
```

---

## AI Arc Filters (For Agent 3)

```json
{
  "ai_arc_filters": {
    "company_search": {
      "industries": ["Consumer Electronics", "Hardware", "IoT", "Smart Home", "Fitness", "Outdoor"],
      "employee_count_min": 5,
      "employee_count_max": 100,
      "revenue_min": "0",
      "revenue_max": "25M",
      "locations": ["United States"],
      "keywords": ["hardware", "product", "IoT", "consumer electronics", "smart home", "connected device"],
      "exclude_keywords": ["software only", "SaaS", "app", "automotive", "aerospace", "defense"],
      "funding_status": "funded",
      "funding_date_min": "2024-06-01"
    },
    "people_search": {
      "title_keywords": ["CEO", "Founder", "Co-Founder", "CTO", "Chief Product Officer"],
      "seniority_levels": ["C-Suite", "Founder"],
      "departments": ["Executive", "Engineering", "Product"],
      "profile_keywords": ["hardware", "product development", "startup"]
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

## Campaign Metrics Targets

- **List size:** 500 contacts
- **Expected reply rate:** 2-3%
- **Expected meeting rate:** 50-60% of replies
- **Estimated meetings:** 5-9

---

## Notes & Considerations

1. **Timing is critical** - Reach out within 60 days of funding announcement for highest response
2. **Personalize the funding reference** - Mention specific amount, investors, or announced use of funds
3. **No case studies** - Lean heavily on credibility statements (27 years, 1,000+ products)
4. **Watch for exclusions** - Skip if they mention automotive, aerospace, defense in their description
5. **Supplement with Crunchbase data** - Use funding amount to gauge project budget capacity
