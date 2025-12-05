# Campaign Brief: CES & Trade Show Deadline
**Client:** Rabbit Product Design
**Generated:** December 5, 2024
**Status:** Draft - Pending Approval
**Priority:** 2 (High)

---

## Target Audience

```yaml
campaign_name: "CES & Trade Show Deadline"
target:
  industries:
    - "Consumer Electronics"
    - "Smart Home / IoT"
    - "Outdoor Products"
    - "Fitness Equipment"
    - "Kitchen Appliances"
    - "Home Goods"
  company_size:
    employees_min: 10
    employees_max: 200
    revenue_min: "$1M"
    revenue_max: "$50M"
  personas:
    - title_keywords: ["VP Product", "VP Engineering", "Director of Product", "Director of Engineering"]
      seniority: "VP/Director"
      department: "Product/Engineering"
    - title_keywords: ["Head of Innovation", "Head of R&D", "Chief Product Officer"]
      seniority: "VP/C-Suite"
      department: "Product/Innovation"
  geography:
    countries: ["United States"]
    regions: []
  technologies: []
  keywords_in_profile:
    - "product development"
    - "hardware"
    - "prototype"
    - "manufacturing"
```

---

## Trigger Event

```yaml
trigger:
  name: "Exhibiting at Upcoming Trade Show (CES, Outdoor Retailer, MD&M, etc.)"
  description: "Company is committed to exhibiting at a major trade show and needs a working prototype or new product to display. Fixed deadline creates urgency."
  signal_source: "CES Exhibitor Gallery, Outdoor Retailer exhibitor list, MD&M West exhibitors, company announcements"
  search_query: '"[company_name]" (CES OR "Outdoor Retailer" OR "trade show" OR exhibiting)'
  urgency: "high"
  decay_rate: "Date-specific - urgency increases as show approaches"
```

---

## Pain Point

```yaml
pain_point:
  problem: "Need a working prototype or production-ready product for trade show display, running out of time"
  symptom: "Internal team scrambling, cutting corners on quality, stress about making the deadline"
  cost_of_inaction: "Embarrassing display at show, missed customer/investor opportunities, wasted booth investment"
  client_solution: "Production-grade prototypes in as little as 1-2 weeks, machined from real materials (not 3D prints)"
```

---

## Proof Point

```yaml
proof_point:
  case_study: "N/A - No B2B case studies available"
  one_liner: "N/A"
  relevance: "N/A"
  fallback: "We deliver production-grade prototypes in 1-2 weeks—machined from real materials, not 3D printed. Our senior engineers have shipped 1,000+ products to market."
```

---

## Enrichment Sources (For Agent 4)

```yaml
enrichment_sources:
  - source: "exhibitor_list"
    tool: "manual_scrape"
    url: "CES Exhibitor Gallery, Outdoor Retailer, MD&M West"
    extract: ["company_name", "booth_number", "product_category"]
    use_in_copy: "{{trade_show_reference}}"

  - source: "company_homepage"
    tool: "jina"
    extract: ["company_description", "current_products", "team_size"]
    use_in_copy: "{{company_context}}"

  - source: "google_news"
    tool: "serperdev_news"
    query: '"{{company_name}}" (CES OR launch OR new product OR announcement)'
    extract: ["recent_announcements", "product_launches"]
    use_in_copy: "{{recent_news}}"

  - source: "linkedin_posts"
    tool: "serperdev"
    query: 'site:linkedin.com/posts "{{company_name}}" (CES OR trade show OR prototype)'
    extract: ["recent_posts", "trade_show_mentions"]
    use_in_copy: "{{social_signal}}"
```

---

## Copywriting Guidance (For Agent 5)

```yaml
copywriting:
  primary_template: "Classic Twist"
  primary_rationale: "Reference the specific trade show to demonstrate research, then pivot to deadline pressure solution"

  secondary_template: "Direct Report"
  secondary_rationale: "Time-pressed product leaders appreciate brevity and clear value prop"

  tertiary_template: "Cryptic Idea"
  tertiary_rationale: "Create curiosity about rapid prototyping capabilities"

  tone: "peer"
  length: "short (300-400 chars)"

  hooks_to_test:
    - "Noticed [company] is exhibiting at CES. If you're racing to have a working prototype by then..."
    - "CES is [X] weeks away. If your prototype isn't where it needs to be yet..."
    - "Most teams exhibiting at [show] tell us the same thing: the booth is booked but the product isn't ready..."
```

---

## AI Arc Filters (For Agent 3)

```json
{
  "ai_arc_filters": {
    "company_search": {
      "industries": ["Consumer Electronics", "Hardware", "IoT", "Smart Home", "Outdoor", "Fitness"],
      "employee_count_min": 10,
      "employee_count_max": 200,
      "revenue_min": "1M",
      "revenue_max": "50M",
      "locations": ["United States"],
      "keywords": ["consumer electronics", "hardware", "product", "smart home", "outdoor", "fitness"],
      "exclude_keywords": ["software", "SaaS", "automotive", "aerospace", "defense"]
    },
    "people_search": {
      "title_keywords": ["VP Product", "VP Engineering", "Director Product", "Director Engineering", "Head of Innovation", "Head of R&D", "CPO"],
      "seniority_levels": ["VP", "Director"],
      "departments": ["Product", "Engineering", "R&D", "Innovation"],
      "profile_keywords": ["product development", "hardware", "prototype"]
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
- **Expected reply rate:** 2-4% (higher due to deadline urgency)
- **Expected meeting rate:** 60-70% of replies
- **Estimated meetings:** 5-11

---

## Notes & Considerations

1. **Time the outreach carefully** - 3-6 months before show for best results, 6-8 weeks is still viable
2. **Key shows to track:**
   - CES (January) - Scrape exhibitor list in August-October
   - Outdoor Retailer (June/January) - 4-5 months ahead
   - MD&M West (February) - October-November
   - Toy Fair (February) - October-November
3. **Reference specific show and booth** if available from exhibitor list
4. **Emphasize speed** - "1-2 weeks for production-grade prototype" is the key differentiator
5. **Consider LinkedIn ads** to exhibitor companies as supplement to cold email
