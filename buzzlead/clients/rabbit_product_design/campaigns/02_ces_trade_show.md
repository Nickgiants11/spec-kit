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

## Strategic Rationale (WHY This Campaign Works)

```yaml
strategic_rationale:
  why_this_trigger:
    timing_logic: "Trade shows create immovable deadlines. CES is January 7-10, 2025 - companies exhibiting MUST have something to show. This deadline creates 3-6 month urgency window where procrastination isn't an option."
    psychological_driver: "Fear of embarrassment at the booth. Investors, press, and customers will be there. Showing up with a non-working prototype or missing key features is a public failure."
    competitive_advantage: "Rabbit's 1-2 week prototype turnaround is the killer differentiator. Most agencies need 6-8 weeks minimum. When deadline is 4 weeks away, Rabbit is the only viable option."

  why_this_persona:
    decision_authority: "VP/Director of Product or Engineering owns the trade show prototype deliverable. They have budget allocated for the show and authority to engage vendors."
    pain_ownership: "This person's job is on the line if the booth is empty or underwhelming. They personally feel the pressure as the deadline approaches."
    budget_access: "Trade show budgets are already approved - booth space costs $10K-$100K+. Spending $15K-$30K on a working prototype is an easy justify vs. wasting the booth investment."

  why_this_message:
    hook_psychology: "Referencing the specific show (CES, Outdoor Retailer) proves research. Mentioning the deadline creates shared urgency - 'we both know the clock is ticking.'"
    proof_selection: "'Production-grade prototypes in 1-2 weeks' directly addresses the time constraint. 'Machined from real materials, not 3D printed' addresses quality concerns for investor/press demos."
    objection_preemption: "'Our senior engineers have shipped 1,000+ products' preempts the 'can we trust you with something this important?' objection."

  expected_conversion_logic:
    why_they_reply: "They're already stressed about the deadline. Email arrives offering exactly what they need (speed + quality). Relief is a powerful motivator."
    why_they_meet: "Low risk to take a call when deadline is looming. Even if Rabbit isn't the right fit, they might learn something useful."
    why_they_buy: "Immovable deadline + working solution + reasonable cost = fast decision. No time for lengthy vendor evaluation when the show is 6 weeks away."
```

---

## List Building Methodology (HOW To Construct This List)

```yaml
list_building_methodology:
  step_1_source_identification:
    primary_source: "CES Exhibitor Gallery (https://www.ces.tech/exhibitor-directory/) - scrape company names from Consumer Electronics, Smart Home, Fitness, Outdoor categories"
    secondary_sources:
      - "Outdoor Retailer exhibitor list"
      - "MD&M West (medical device/manufacturing) exhibitor list"
      - "Toy Fair exhibitor list"
    manual_sources:
      - "Direct scrape of exhibitor PDFs (often available 3-4 months before show)"
      - "LinkedIn posts mentioning 'excited to exhibit at CES' or 'see you at [show]'"

  step_2_company_filtering:
    must_have_criteria:
      - "Confirmed exhibitor at upcoming trade show"
      - "Hardware/physical product company (not pure software)"
      - "10-200 employees (larger companies have internal teams)"
      - "US-based or US presence"
    nice_to_have_criteria:
      - "Show is 2-5 months away (sweet spot for urgency)"
      - "Company has posted about preparing for the show"
      - "New product launch planned for the show"
    exclusion_criteria:
      - "Enterprise companies (>200 employees)"
      - "Automotive, aerospace, defense"
      - "Pure software/SaaS companies"
      - "Companies already working with competitor design firms"

  step_3_person_identification:
    target_titles_priority:
      tier_1: ["VP Product", "VP Engineering", "Director of Product", "Director of Engineering"]
      tier_2: ["Head of Innovation", "Head of R&D", "CPO", "CTO"]
      tier_3: ["Product Manager", "Engineering Manager"]
    max_contacts_per_company: 2
    title_selection_logic: "Target VP/Director level first - they own trade show deliverables. Avoid C-suite unless company <30 employees."

  step_4_data_validation:
    email_requirements:
      minimum_confidence: 0.8
      required_format: "business email"
      fallback_action: "LinkedIn outreach if no email - trade show urgency warrants multi-channel"
    company_validation:
      verify_website_live: true
      verify_company_active: true
      recency_check: "Confirm exhibitor status is current year"

  step_5_enrichment_sequence:
    order_of_operations:
      - "Confirm exhibitor status and booth number if available"
      - "Pull company homepage for product context"
      - "Search Google News for any trade show announcements"
      - "Check LinkedIn for recent posts about show preparation"
    cost_optimization: "Only enrich confirmed exhibitors. Focus on shows 2-5 months out."

  step_6_deduplication:
    dedupe_against:
      - "Rabbit DNC list"
      - "Post-Funding campaign (may overlap with recently funded exhibitors)"
    merge_logic: "Keep in CES campaign if show <4 months away. Otherwise keep in higher-priority campaign."
```

---

## Sample Validation (Before Full Pull)

```yaml
sample_validation:
  purpose: "Test that exhibitor lists yield relevant hardware companies with reachable decision-makers"

  sample_size: 8 companies

  validation_checklist:
    - question: "Is this company actually exhibiting at the trade show?"
      pass_criteria: "Listed in official exhibitor directory with booth number"
      fail_example: "Company mentioned wanting to exhibit but isn't confirmed"

    - question: "Do they make physical hardware products?"
      pass_criteria: "Product visible on website, not pure software/platform"
      fail_example: "Software company with 'IoT' in name but no physical products"

    - question: "Is the show timeline relevant?"
      pass_criteria: "Show is 2-6 months away - urgent but not impossible"
      fail_example: "Show is next week (too late) or 9 months away (no urgency)"

    - question: "Is the contact relevant to product development?"
      pass_criteria: "VP/Director of Product, Engineering, or R&D"
      fail_example: "Marketing or Sales executive"

    - question: "Would they benefit from rapid prototyping?"
      pass_criteria: "Company size and stage suggests they need external help"
      fail_example: "Large company (500+ employees) with internal design team"

  sample_companies:
    - company_name: "Ring (Amazon)"
      why_they_fit: "Smart home security, CES exhibitor"
      contact_name: "N/A"
      contact_title: "N/A"
      trigger_evidence: "CES exhibitor"
      validation_status: "FAIL - Owned by Amazon, too large"

    - company_name: "Wyze Labs"
      why_they_fit: "Smart home cameras/devices, frequent CES exhibitor"
      contact_name: "Dave Crosby"
      contact_title: "VP of Product"
      trigger_evidence: "CES exhibitor, consumer hardware"
      validation_status: "NEEDS REVIEW - Check employee count"

    - company_name: "Anker Innovations"
      why_they_fit: "Consumer electronics, CES exhibitor"
      contact_name: "N/A"
      contact_title: "N/A"
      trigger_evidence: "CES exhibitor"
      validation_status: "FAIL - Too large (1000+ employees)"

    - company_name: "Nanoleaf"
      why_they_fit: "Smart lighting, CES exhibitor, design-focused"
      contact_name: "Gimmy Chu"
      contact_title: "CEO & Co-Founder"
      trigger_evidence: "CES exhibitor, consumer hardware, ~100 employees"
      validation_status: "PASS - Ideal fit"

    - company_name: "Ecobee"
      why_they_fit: "Smart thermostat, CES exhibitor"
      contact_name: "Stuart Lombard"
      contact_title: "CEO & Founder"
      trigger_evidence: "CES exhibitor, smart home"
      validation_status: "NEEDS REVIEW - May have internal team"

    - company_name: "LIFX"
      why_they_fit: "Smart lighting, CES exhibitor"
      contact_name: "N/A"
      contact_title: "N/A"
      trigger_evidence: "CES exhibitor, consumer hardware"
      validation_status: "PASS - Right size and segment"

    - company_name: "Pavlok"
      why_they_fit: "Wearable behavior change device, smaller hardware startup"
      contact_name: "Maneesh Sethi"
      contact_title: "CEO & Founder"
      trigger_evidence: "Hardware startup, wearables"
      validation_status: "PASS - Ideal startup size"

    - company_name: "Whoop"
      why_they_fit: "Fitness wearable, frequent trade show exhibitor"
      contact_name: "Will Ahmed"
      contact_title: "CEO & Founder"
      trigger_evidence: "Fitness hardware, consumer electronics"
      validation_status: "NEEDS REVIEW - Check recent funding/size"

  go_no_go_decision:
    pass_threshold: "6 of 8 samples must pass all criteria"
    if_pass: "Proceed with full 400-contact pull"
    if_fail: "Adjust filters: tighten employee count, focus on specific product categories"
    common_filter_adjustments:
      - "Filter to 10-150 employees only"
      - "Exclude 'platform' companies"
      - "Focus on specific categories: Smart Home, Fitness, Outdoor"
      - "Prioritize first-time or smaller booth exhibitors"
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
