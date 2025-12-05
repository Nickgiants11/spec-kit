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

## Strategic Rationale (WHY This Campaign Works)

```yaml
strategic_rationale:
  why_this_trigger:
    timing_logic: "Post-funding creates a 60-90 day window where founders are actively seeking vendors to deploy capital. They have money, board pressure to show progress, and hiring timelines that don't match their ambitions."
    psychological_driver: "Pressure to show progress to investors creates urgency. Founders feel the clock ticking on their runway and need to demonstrate product milestones quickly."
    competitive_advantage: "Rabbit provides instant senior capacity (27 years avg) vs. 3-6 month hiring timeline. While competitors require discovery phases, Rabbit can start executing immediately."

  why_this_persona:
    decision_authority: "Founders at <50 employees make vendor decisions without procurement. Post-funding, they have explicit budget authority and board mandate to spend on product development."
    pain_ownership: "The founder IS the product - delays reflect directly on them. They personally feel every missed milestone and investor question about progress."
    budget_access: "Post-Series A companies typically have $50K-200K allocated for external product development. Seed rounds usually have $25K-75K available for design/engineering services."

  why_this_message:
    hook_psychology: "Congratulating on funding disarms sales resistance. Then pivoting to 'the real challenge ahead' creates authority - we've seen this pattern before."
    proof_selection: "'27 years experience' and '1,000+ products' address the fear of working with inexperienced freelancers. Specific numbers feel credible."
    objection_preemption: "'Without the 6-month hiring cycle' preempts the 'we'll hire our own team' objection. It frames Rabbit as a bridge, not a replacement."

  expected_conversion_logic:
    why_they_reply: "They're actively looking for solutions. Funding announcement + product development need = high-intent prospect. The email arrives when they're already thinking about this problem."
    why_they_meet: "Meeting offers potential shortcut to their biggest bottleneck. Even if they don't hire Rabbit, the conversation might provide valuable insight."
    why_they_buy: "Time pressure (investor expectations) + clear fit (hardware expertise) + reasonable cost (half of agencies) = fast decision. No lengthy evaluation process at this stage."
```

---

## List Building Methodology (HOW To Construct This List)

```yaml
list_building_methodology:
  step_1_source_identification:
    primary_source: "AI Arc company search with funding_status=funded and funding_date_min=2024-06-01"
    secondary_sources:
      - "Crunchbase funding announcements (filter: Hardware, IoT, Consumer Electronics categories)"
      - "TechCrunch hardware startup funding coverage"
      - "PR Newswire funding announcements"
    manual_sources:
      - "Y Combinator hardware company directory (recent batches)"
      - "SBIR.gov hardware awards (indicates serious development budget)"

  step_2_company_filtering:
    must_have_criteria:
      - "Funded in last 6 months (Seed to Series B)"
      - "US-based headquarters"
      - "Hardware/IoT/Consumer Electronics - makes physical products"
      - "5-100 employees (sweet spot: 10-50)"
    nice_to_have_criteria:
      - "Active job postings for engineers (signals growth)"
      - "Recently mentioned in tech press (signals momentum)"
      - "Product visible on website (validates hardware company)"
    exclusion_criteria:
      - "Enterprise companies (>100 employees) - different buying process"
      - "Automotive, aerospace, defense industries - excluded per client"
      - "Software-only companies (SaaS, apps) - no hardware need"
      - "Companies on competitor list (Gembah, Design 1st, etc.)"

  step_3_person_identification:
    target_titles_priority:
      tier_1: ["CEO", "Founder", "Co-Founder"]
      tier_2: ["CTO", "Chief Product Officer"]
      tier_3: ["VP Engineering", "VP Product"]
    max_contacts_per_company: 2
    title_selection_logic: "Prefer Founder/CEO (full budget authority). Add CTO only if Founder not found or company >30 employees."

  step_4_data_validation:
    email_requirements:
      minimum_confidence: 0.8
      required_format: "business email (not personal Gmail/Yahoo)"
      fallback_action: "Flag for LinkedIn outreach if no business email"
    company_validation:
      verify_website_live: true
      verify_company_active: true
      recency_check: "Funding announced within last 6 months"

  step_5_enrichment_sequence:
    order_of_operations:
      - "Pull company homepage with Jina for product context"
      - "Search Google News for funding announcement details (amount, investors, use of funds)"
      - "Verify Crunchbase data for funding round confirmation"
      - "Check LinkedIn for recent employee growth"
    cost_optimization: "Only enrich companies that pass step 2-4 validation. Batch enrichment in groups of 50."

  step_6_deduplication:
    dedupe_against:
      - "Rabbit Product Design DNC list"
      - "Previous campaign exports"
      - "Other campaigns in this batch (CES, Hiring Surge may overlap)"
    merge_logic: "Keep in Post-Funding campaign (highest priority). Remove from lower-priority campaigns if duplicate."
```

---

## Sample Validation (Before Full Pull)

```yaml
sample_validation:
  purpose: "Test that filters return relevant recently-funded hardware startups before spending on full pull"

  sample_size: 8 companies

  validation_checklist:
    - question: "Does this company actually make physical hardware products?"
      pass_criteria: "Physical product visible on website, not pure software/SaaS"
      fail_example: "Company describes as 'IoT platform' but only sells software/APIs"

    - question: "Is the funding signal real and recent?"
      pass_criteria: "Funding announced within last 6 months, confirmable via Crunchbase/news"
      fail_example: "Last funding was 2 years ago, company just showed up in database refresh"

    - question: "Is the contact a decision-maker?"
      pass_criteria: "Founder, CEO, CTO, or VP-level with product authority"
      fail_example: "Marketing coordinator or junior engineer"

    - question: "Can we actually reach them?"
      pass_criteria: "Business email with 80%+ confidence"
      fail_example: "Only personal Gmail found, or email bounces"

    - question: "Would Rabbit want this client?"
      pass_criteria: "Consumer hardware, reasonable size (5-100), US-based"
      fail_example: "Defense contractor, automotive supplier, or 500+ employee enterprise"

  sample_companies:
    - company_name: "Ember Technologies"
      why_they_fit: "Smart mug/drinkware company, raised $23.5M Series C, exactly the kind of consumer hardware Rabbit serves"
      contact_name: "Clay Alexander"
      contact_title: "CEO & Founder"
      trigger_evidence: "Series C funding, 93 employees, consumer electronics"
      validation_status: "PASS - Ideal ICP match"

    - company_name: "Tonal Systems"
      why_they_fit: "Connected fitness equipment, raised $250M+, hardware + software + manufacturing"
      contact_name: "Aly Orady"
      contact_title: "CEO & Founder"
      trigger_evidence: "Major funding rounds, fitness hardware"
      validation_status: "PASS - but may be too large (check employee count)"

    - company_name: "June Life (June Oven)"
      why_they_fit: "Smart kitchen appliance, raised $29.5M, acquired by Weber - validates smart kitchen market"
      contact_name: "Acquired by Weber"
      contact_title: "N/A"
      trigger_evidence: "Historical example of ideal client type"
      validation_status: "FAIL - Acquired, not active prospect"

    - company_name: "Lomi (Pela)"
      why_they_fit: "Smart composter, hardware startup, consumer product"
      contact_name: "Matt Bertulli"
      contact_title: "CEO"
      trigger_evidence: "Successful hardware launch, DTC model"
      validation_status: "NEEDS REVIEW - Verify recent funding"

    - company_name: "Span.IO"
      why_they_fit: "Smart electrical panel, $90M+ raised, hardware + installation"
      contact_name: "Arch Rao"
      contact_title: "CEO"
      trigger_evidence: "Series B, smart home/energy"
      validation_status: "PASS - Strong ICP fit"

    - company_name: "Brilliant Home Technology"
      why_they_fit: "Smart home control panels, raised $50M+, consumer hardware"
      contact_name: "Aaron Emigh"
      contact_title: "CEO & Co-Founder"
      trigger_evidence: "Series B, smart home hardware"
      validation_status: "PASS - Ideal fit"

    - company_name: "Masonite Smart Doors"
      why_they_fit: "Smart door company"
      contact_name: "N/A"
      contact_title: "N/A"
      trigger_evidence: "Enterprise/industrial"
      validation_status: "FAIL - Too enterprise, wrong market segment"

    - company_name: "Oura Ring"
      why_they_fit: "Wearable hardware, raised $100M+, consumer electronics"
      contact_name: "Tom Hale"
      contact_title: "CEO"
      trigger_evidence: "Series C, wearables"
      validation_status: "NEEDS REVIEW - May be too large now"

  go_no_go_decision:
    pass_threshold: "6 of 8 samples must pass all criteria"
    if_pass: "Proceed with full 500-contact pull"
    if_fail: "Adjust filters and re-sample before full pull"
    common_filter_adjustments:
      - "Tighten employee count to 10-75 if too many large companies"
      - "Add 'consumer' keyword if B2B/enterprise appearing"
      - "Narrow funding date to last 90 days if signals too old"
      - "Exclude 'platform' or 'SaaS' if software companies appearing"
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
