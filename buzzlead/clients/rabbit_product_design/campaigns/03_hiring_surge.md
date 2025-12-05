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

## Strategic Rationale (WHY This Campaign Works)

```yaml
strategic_rationale:
  why_this_trigger:
    timing_logic: "Multiple hardware engineering job postings = capacity gap NOW. They're hiring because they need help, but hiring takes 3-6 months. The gap between 'we need engineers' and 'we have engineers' is where Rabbit wins."
    psychological_driver: "Engineering leaders posting multiple roles are underwater. Their team is likely stressed, deadlines are slipping, and every week without help makes it worse. They're actively seeking solutions."
    competitive_advantage: "Rabbit offers instant senior capacity (27 years avg) without the hiring timeline or long-term commitment. It's a bridge solution that doesn't require HR approval or headcount increase."

  why_this_persona:
    decision_authority: "VP/Director of Engineering owns the hiring budget. When they're trying to fill 3+ roles, they have explicit authority to engage contractors/consultants to fill gaps."
    pain_ownership: "This person is accountable for project delivery. When their team is stretched thin, they personally feel every missed deadline and quality issue. The pain is immediate and personal."
    budget_access: "Hiring budget is already allocated. If they're trying to hire 3 senior engineers at $150K+ each, engaging a $50K project with Rabbit is actually a cost savings."

  why_this_message:
    hook_psychology: "Referencing their specific open roles proves research. It says 'I see you're struggling' without being condescending. The pivot to 'while you're ramping up' is empathetic, not salesy."
    proof_selection: "'27 years average experience' addresses the 'we need senior people' pain. It's not about junior freelancers - it's about seasoned professionals who can execute immediately."
    objection_preemption: "'No commitment to keep them on payroll' preempts the 'we don't want another permanent vendor' objection. Positions Rabbit as temporary surge capacity."

  expected_conversion_logic:
    why_they_reply: "They're actively in pain. The job postings prove it. Email arrives with a potential short-term solution to their current problem."
    why_they_meet: "Low-risk conversation. They might learn something useful about their hiring approach or find a bridge solution."
    why_they_buy: "Current pain (overworked team) + clear solution (senior capacity) + no long-term commitment = easy yes. It's a tactical decision, not a strategic one."
```

---

## List Building Methodology (HOW To Construct This List)

```yaml
list_building_methodology:
  step_1_source_identification:
    primary_source: "LinkedIn Jobs API - search for companies with 3+ hardware/mechanical/product engineering roles open"
    secondary_sources:
      - "Indeed hardware engineering job postings"
      - "Greenhouse/Lever job boards (often public)"
      - "Company careers pages (direct scrape)"
    manual_sources:
      - "LinkedIn company page job counts"
      - "Tech job aggregators (AngelList, Built In, etc.)"

  step_2_company_filtering:
    must_have_criteria:
      - "3+ hardware-related job postings open simultaneously"
      - "Hardware/consumer electronics/IoT company (not pure software)"
      - "20-200 employees (smaller have no budget, larger have internal recruiting)"
      - "US-based"
    nice_to_have_criteria:
      - "Job postings are recent (last 30 days)"
      - "Roles include 'senior' or 'lead' titles (indicates quality bar)"
      - "Company recently funded (combines with Trigger 1)"
    exclusion_criteria:
      - "Software-only companies"
      - "Automotive, aerospace, defense"
      - "Enterprise (>200 employees) - different procurement"
      - "Already working with competitor design firms"

  step_3_person_identification:
    target_titles_priority:
      tier_1: ["VP Engineering", "VP Product", "Director of Engineering"]
      tier_2: ["Director of Product Development", "Head of Hardware", "Head of R&D"]
      tier_3: ["Engineering Manager", "Product Development Manager"]
    max_contacts_per_company: 2
    title_selection_logic: "Target VP Engineering first (owns hiring). Add Director if VP not found. Avoid C-suite - they're too far from the daily pain."

  step_4_data_validation:
    email_requirements:
      minimum_confidence: 0.8
      required_format: "business email"
      fallback_action: "LinkedIn outreach with job posting reference"
    company_validation:
      verify_website_live: true
      verify_company_active: true
      recency_check: "Job postings still open (not filled)"

  step_5_enrichment_sequence:
    order_of_operations:
      - "Confirm job postings are current (LinkedIn Jobs check)"
      - "Count and categorize open roles (mechanical, electrical, firmware)"
      - "Pull company homepage for product context"
      - "Check for recent funding (Crunchbase) - compounds the signal"
    cost_optimization: "Only enrich companies with 3+ verified open hardware roles"

  step_6_deduplication:
    dedupe_against:
      - "Rabbit DNC list"
      - "Post-Funding campaign (hiring surge often follows funding)"
      - "CES campaign (may be hiring for product launch)"
    merge_logic: "Keep in Hiring Surge if 3+ roles open. Otherwise keep in higher-priority campaign."
```

---

## Sample Validation (Before Full Pull)

```yaml
sample_validation:
  purpose: "Test that job posting signals yield companies actively seeking engineering capacity"

  sample_size: 8 companies

  validation_checklist:
    - question: "Does this company have 3+ hardware engineering roles open?"
      pass_criteria: "Verified via LinkedIn Jobs or company careers page"
      fail_example: "Only 1-2 roles, or roles are stale (posted 6+ months ago)"

    - question: "Are these genuine hardware roles (not software)?"
      pass_criteria: "Mechanical, electrical, firmware, product design engineering"
      fail_example: "Software engineer roles at a company with 'hardware' in description"

    - question: "Is the company size right for external help?"
      pass_criteria: "20-200 employees - large enough to have budget, small enough to need help"
      fail_example: "5-person startup (no budget) or 1000+ enterprise (internal team)"

    - question: "Is the VP/Director reachable?"
      pass_criteria: "Business email with 80%+ confidence"
      fail_example: "Only personal email or no contact info"

    - question: "Would Rabbit be a good fit?"
      pass_criteria: "Consumer hardware, US-based, not in excluded industries"
      fail_example: "Automotive, defense, or B2B industrial equipment"

  sample_companies:
    - company_name: "Oura Health"
      why_they_fit: "Wearables company, frequently hiring hardware engineers"
      contact_name: "N/A"
      contact_title: "VP Engineering"
      trigger_evidence: "Multiple hardware engineering postings"
      validation_status: "NEEDS REVIEW - Check current open roles count"

    - company_name: "Peloton"
      why_they_fit: "Fitness hardware, always hiring"
      contact_name: "N/A"
      contact_title: "N/A"
      trigger_evidence: "Large hardware team"
      validation_status: "FAIL - Too large, has internal team"

    - company_name: "Level Home"
      why_they_fit: "Smart lock company, hardware startup"
      contact_name: "John Martin"
      contact_title: "CEO & Co-Founder"
      trigger_evidence: "Hardware startup, smart home"
      validation_status: "PASS - Right size and segment"

    - company_name: "Eight Sleep"
      why_they_fit: "Smart mattress, hardware + software"
      contact_name: "Massimo Andreasi"
      contact_title: "CTO"
      trigger_evidence: "Hardware company, consumer product"
      validation_status: "PASS - Good ICP fit"

    - company_name: "Tempo"
      why_they_fit: "Connected fitness hardware"
      contact_name: "Moawia Eldeeb"
      contact_title: "CEO"
      trigger_evidence: "Fitness hardware"
      validation_status: "NEEDS REVIEW - Check funding/size"

    - company_name: "Latch"
      why_they_fit: "Smart access/building hardware"
      contact_name: "Luke Schoenfelder"
      contact_title: "CEO"
      trigger_evidence: "Smart building hardware"
      validation_status: "NEEDS REVIEW - May be too B2B/enterprise"

    - company_name: "Canary"
      why_they_fit: "Smart home security hardware"
      contact_name: "Chris Rill"
      contact_title: "CTO & Co-Founder"
      trigger_evidence: "Consumer hardware, smart home"
      validation_status: "PASS - Ideal fit"

    - company_name: "SimpliSafe"
      why_they_fit: "Home security hardware"
      contact_name: "N/A"
      contact_title: "N/A"
      trigger_evidence: "Consumer hardware"
      validation_status: "NEEDS REVIEW - Check size (may be too large)"

  go_no_go_decision:
    pass_threshold: "6 of 8 samples must pass all criteria"
    if_pass: "Proceed with full 400-contact pull"
    if_fail: "Adjust filters and re-sample"
    common_filter_adjustments:
      - "Require 4+ roles instead of 3+ if too many large companies"
      - "Add 'startup' or 'Series A/B' filter"
      - "Require postings less than 30 days old"
      - "Exclude companies with 'platform' or 'enterprise' in description"
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
