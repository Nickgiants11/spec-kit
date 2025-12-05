# Campaign Brief: Design Firm Disaster Recovery
**Client:** Rabbit Product Design
**Generated:** December 5, 2024
**Status:** Draft - Pending Approval
**Priority:** 4 (Medium)

---

## Target Audience

```yaml
campaign_name: "Design Firm Disaster Recovery"
target:
  industries:
    - "Consumer Electronics"
    - "Smart Home / IoT"
    - "Hardware Startups"
    - "Consumer Products"
    - "Fitness Equipment"
    - "Outdoor Products"
  company_size:
    employees_min: 1
    employees_max: 100
    revenue_min: "$0"
    revenue_max: "$25M"
  personas:
    - title_keywords: ["CEO", "Founder", "Co-Founder"]
      seniority: "C-Suite/Founder"
      department: "Executive"
    - title_keywords: ["CTO", "VP Product", "Head of Product"]
      seniority: "C-Suite/VP"
      department: "Product/Engineering"
  geography:
    countries: ["United States"]
    regions: []
  technologies: []
  keywords_in_profile:
    - "hardware"
    - "product"
    - "startup"
    - "inventor"
```

---

## Trigger Event

```yaml
trigger:
  name: "Public Frustration with Design Firm or Failed Project"
  description: "Founder or product leader has posted about or mentioned bad experiences with design firms, failed prototypes, or wasted money on product development. They're actively looking for a better solution."
  signal_source: "LinkedIn posts, Twitter, Reddit (r/hwstartups, r/entrepreneur), Glassdoor reviews of competitors"
  search_query: '"design firm" (disappointed OR frustrated OR failed OR wasted money OR terrible) hardware'
  urgency: "high"
  decay_rate: "30-60 days - pain is fresh and they're actively seeking alternatives"
```

---

## Pain Point

```yaml
pain_point:
  problem: "Previous design firm delivered CAD files that looked good but failed in prototyping or manufacturing"
  symptom: "Wasted $20K+, multiple prototype iterations, delayed timeline, lost confidence in vendors"
  cost_of_inaction: "More wasted money, continued delays, potential project failure"
  client_solution: "DFM validation at every stage reduces rework by 50%. Production-grade prototypes, not 3D prints. Same senior engineer from design through manufacturing."
```

---

## Proof Point

```yaml
proof_point:
  case_study: "N/A - No B2B case studies available"
  one_liner: "N/A"
  relevance: "N/A"
  fallback: "We reduce prototype iterations by 50% through DFM validation at every stage. Our engineers average 27 years experience—they've seen (and solved) the mistakes other firms make."
```

---

## Enrichment Sources (For Agent 4)

```yaml
enrichment_sources:
  - source: "linkedin_posts"
    tool: "serperdev"
    query: 'site:linkedin.com/posts ("design firm" OR "product development") (frustrated OR disappointed OR failed OR "wasted money")'
    extract: ["post_content", "author_name", "company", "date"]
    use_in_copy: "{{frustration_reference}}"

  - source: "reddit_hwstartups"
    tool: "serperdev"
    query: 'site:reddit.com/r/hwstartups ("design firm" OR "product development company") (bad OR terrible OR scam OR avoid)'
    extract: ["post_content", "author", "date"]
    use_in_copy: "{{community_signal}}"

  - source: "company_homepage"
    tool: "jina"
    extract: ["company_description", "product_type", "stage"]
    use_in_copy: "{{company_context}}"

  - source: "linkedin_profile"
    tool: "serperdev"
    query: 'site:linkedin.com/in "{{person_name}}" {{company_name}}'
    extract: ["current_role", "background", "connections"]
    use_in_copy: "{{personal_context}}"
```

---

## Copywriting Guidance (For Agent 5)

```yaml
copywriting:
  primary_template: "Storytelling"
  primary_rationale: "Reference their frustration empathetically, share that many founders face the same issue, position Rabbit as the fix"

  secondary_template: "Poke the Bear"
  secondary_rationale: "Validate their frustration, challenge the status quo of typical design firms"

  tertiary_template: "Direct Report"
  tertiary_rationale: "If they've posted publicly, they may want solutions not sympathy—get to the point"

  tone: "founder-to-founder"
  length: "medium (400-500 chars)"

  hooks_to_test:
    - "Saw your post about [design firm frustration]. We work with a lot of founders who've been through the same thing..."
    - "Most hardware founders I talk to have the same story: beautiful CAD files that fail in production. It's why we validate for manufacturability at every stage..."
    - "After you've already spent $20K on a design that doesn't work, the last thing you want is another vendor pitch. So I'll keep this short..."
```

---

## AI Arc Filters (For Agent 3)

```json
{
  "ai_arc_filters": {
    "company_search": {
      "industries": ["Consumer Electronics", "Hardware", "IoT", "Consumer Products", "Fitness", "Outdoor"],
      "employee_count_min": 1,
      "employee_count_max": 100,
      "revenue_min": "0",
      "revenue_max": "25M",
      "locations": ["United States"],
      "keywords": ["hardware", "product", "startup", "inventor", "prototype"],
      "exclude_keywords": ["software", "SaaS", "automotive", "aerospace", "defense"]
    },
    "people_search": {
      "title_keywords": ["CEO", "Founder", "Co-Founder", "CTO", "VP Product"],
      "seniority_levels": ["C-Suite", "Founder", "VP"],
      "departments": ["Executive", "Product", "Engineering"],
      "profile_keywords": ["hardware", "product", "startup", "inventor"]
    },
    "export_options": {
      "include_email": true,
      "email_confidence_min": 0.8,
      "max_results": 300
    }
  }
}
```

---

## Campaign Metrics Targets

- **List size:** 300 contacts
- **Expected reply rate:** 3-5% (higher due to active pain)
- **Expected meeting rate:** 65-75% of replies
- **Estimated meetings:** 6-11

---

## Notes & Considerations

1. **This campaign requires manual curation** - Not every frustrated post is a fit
2. **Verify they're hardware** - Many "design firm" complaints are about branding/marketing agencies
3. **Reference their specific frustration** - Generic "I know the struggle" is weak; specific reference is powerful
4. **Time-sensitive** - Respond within 1-2 weeks of their post for highest impact
5. **Consider competitors' negative reviews:**
   - Gembah G2/Clutch reviews
   - Glassdoor reviews mentioning client issues
   - Reddit threads about product development companies
6. **The fallback proof is strong here** - "We reduce rework by 50% through DFM validation" directly addresses their pain
7. **Longer email OK** - They've already posted publicly; they want to be heard first
