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

## Strategic Rationale (WHY This Campaign Works)

```yaml
strategic_rationale:
  why_this_trigger:
    timing_logic: "Someone posting publicly about design firm frustration is actively seeking solutions. The pain is fresh (usually 30-60 days), they've already spent money, and they're emotionally ready to try something different."
    psychological_driver: "Burned founders are risk-averse but also desperate. They've lost trust in the category. Demonstrating understanding of their specific pain earns attention that generic outreach doesn't."
    competitive_advantage: "Rabbit's 'DFM validation at every stage' directly addresses the #1 failure mode: pretty CAD files that can't be manufactured. The 50% reduction in rework is a specific, believable claim."

  why_this_persona:
    decision_authority: "Founders who've been burned have full authority. They've already proven willingness to spend on product development. Now they need a better vendor."
    pain_ownership: "This is deeply personal. They likely feel embarrassed about wasting money, frustrated about lost time, and anxious about trying again. The pain is visceral."
    budget_access: "They've already budgeted for this. In fact, they've already spent $20K-$50K+ with the failed firm. They have money allocated; they just need a trustworthy vendor."

  why_this_message:
    hook_psychology: "Referencing their specific post ('Saw your post about...') proves you listened. Most vendors blast generic pitches. Personal acknowledgment of their pain builds instant rapport."
    proof_selection: "'50% fewer prototype iterations' is specific and addresses their exact failure. '27 years experience' suggests wisdom vs. the junior team that failed them."
    objection_preemption: "Leading with empathy ('We work with a lot of founders in the same situation') normalizes their experience and reduces shame. They're not stupid—they just hired the wrong firm."

  expected_conversion_logic:
    why_they_reply: "Someone finally understands their pain. The email doesn't feel like a sales pitch—it feels like someone who's seen this pattern before and might actually help."
    why_they_meet: "Low risk, high potential upside. They've already proven they'll invest in product development. A conversation might reveal whether Rabbit is different."
    why_they_buy: "Fear of another failure is high, but so is the sunk cost. If Rabbit can demonstrate credibility (27 years, DFM process, specific approach), they'll take the bet. Alternative is giving up on the project."
```

---

## List Building Methodology (HOW To Construct This List)

```yaml
list_building_methodology:
  step_1_source_identification:
    primary_source: "LinkedIn posts search - '\"design firm\" OR \"product development\" + (frustrated OR disappointed OR failed OR wasted money)'"
    secondary_sources:
      - "Reddit r/hwstartups and r/entrepreneur threads about bad design firm experiences"
      - "Twitter/X threads about product development failures"
      - "G2/Clutch negative reviews of competitor design firms"
    manual_sources:
      - "Glassdoor reviews mentioning client issues at Gembah, Design 1st, etc."
      - "HackerNews threads about hardware development"
      - "Founder community forums (Indie Hackers, etc.)"

  step_2_company_filtering:
    must_have_criteria:
      - "Posted about design firm frustration within last 60 days"
      - "Hardware/physical product company (verify from profile/company)"
      - "Founder, CEO, or product leader (not junior employee venting)"
      - "US-based or US market"
    nice_to_have_criteria:
      - "Specific dollar amount mentioned (indicates budget scope)"
      - "Specific failure described (more personalization opportunity)"
      - "Multiple posts about the issue (high frustration = high motivation)"
    exclusion_criteria:
      - "Complaints about branding/marketing agencies (not product development)"
      - "Software/SaaS companies"
      - "Automotive, aerospace, defense"
      - "Complaints about Rabbit or Adam Tavin specifically (obviously)"

  step_3_person_identification:
    target_titles_priority:
      tier_1: ["Founder", "CEO", "Co-Founder"]
      tier_2: ["CTO", "VP Product", "VP Engineering"]
      tier_3: ["Director of Product", "Head of Product"]
    max_contacts_per_company: 1
    title_selection_logic: "Target the person who posted. This is personal outreach, not company targeting."

  step_4_data_validation:
    email_requirements:
      minimum_confidence: 0.8
      required_format: "business email preferred, personal acceptable (founders often use personal)"
      fallback_action: "LinkedIn DM - this audience is more receptive to personal outreach"
    company_validation:
      verify_website_live: true
      verify_company_active: true
      recency_check: "Post is within 60 days"

  step_5_enrichment_sequence:
    order_of_operations:
      - "Capture full text of their frustration post (for personalization)"
      - "Verify company is hardware (not software)"
      - "Find company website and product description"
      - "Check if they mentioned specific firms or dollar amounts"
    cost_optimization: "This is a manual-heavy campaign. Budget time for individual research per lead."

  step_6_deduplication:
    dedupe_against:
      - "Rabbit DNC list"
      - "Other campaigns (unlikely overlap due to trigger specificity)"
    merge_logic: "Keep in Design Firm Recovery - this trigger overrides others."
```

---

## Sample Validation (Before Full Pull)

```yaml
sample_validation:
  purpose: "Test that frustration signals yield legitimate hardware founders with reachable contacts"

  sample_size: 8 companies

  validation_checklist:
    - question: "Is this a genuine hardware product company?"
      pass_criteria: "Physical product visible on website or described in post"
      fail_example: "Software company frustrated with agency, or branding complaint"

    - question: "Is the frustration about product development (not marketing/branding)?"
      pass_criteria: "Mentions CAD, prototyping, manufacturing, engineering"
      fail_example: "Unhappy with logo design or marketing campaign"

    - question: "Is the post recent enough to act on?"
      pass_criteria: "Posted within last 60 days"
      fail_example: "Frustration post from 2 years ago"

    - question: "Is the poster a decision-maker?"
      pass_criteria: "Founder, CEO, or product leader"
      fail_example: "Engineer venting about their company's vendor"

    - question: "Can we personalize outreach?"
      pass_criteria: "Specific details in post that can be referenced"
      fail_example: "Generic 'design firms suck' with no specifics"

  sample_companies:
    - company_name: "Example: Smart Home Startup"
      why_they_fit: "Founder posted on LinkedIn about wasting $25K on offshore design firm that delivered un-manufacturable CAD files"
      contact_name: "[From post author]"
      contact_title: "Founder"
      trigger_evidence: "LinkedIn post, 3 weeks ago, specific dollar amount and failure mode"
      validation_status: "PASS - High personalization opportunity"

    - company_name: "Example: Fitness Equipment Startup"
      why_they_fit: "CEO posted Reddit thread about prototype that failed in production"
      contact_name: "[From Reddit username/profile]"
      contact_title: "CEO"
      trigger_evidence: "Reddit r/hwstartups, mentions manufacturing failure"
      validation_status: "PASS - Clear hardware, specific pain"

    - company_name: "Example: IoT Sensor Company"
      why_they_fit: "Founder tweeted about third design firm in 2 years"
      contact_name: "[From Twitter/X]"
      contact_title: "Founder"
      trigger_evidence: "Twitter thread, mentions multiple firm failures"
      validation_status: "PASS - High frustration, ready to change"

    - company_name: "Example: DTC Brand"
      why_they_fit: "Posted about 'terrible experience' with product development"
      contact_name: "[From post]"
      contact_title: "Co-Founder"
      trigger_evidence: "LinkedIn post"
      validation_status: "NEEDS REVIEW - Verify it's hardware, not packaging/branding"

    - company_name: "Example: App Company"
      why_they_fit: "Frustrated with 'product agency'"
      contact_name: "[From post]"
      contact_title: "CEO"
      trigger_evidence: "LinkedIn post"
      validation_status: "FAIL - Software company, not hardware"

    - company_name: "Gembah 1-Star Reviewer"
      why_they_fit: "Left 1-star G2 review with detailed complaint"
      contact_name: "[From review if identifiable]"
      contact_title: "Unknown"
      trigger_evidence: "G2 review"
      validation_status: "NEEDS REVIEW - May not be identifiable"

    - company_name: "Example: Outdoor Gear Startup"
      why_they_fit: "HackerNews comment about design firm failures"
      contact_name: "[From HN username]"
      contact_title: "Founder"
      trigger_evidence: "HackerNews thread"
      validation_status: "PASS - Hardware, specific pain"

    - company_name: "Example: Consultant Complaining"
      why_they_fit: "Posted about client's bad experience"
      contact_name: "N/A"
      contact_title: "Consultant"
      trigger_evidence: "LinkedIn post"
      validation_status: "FAIL - Not the buyer, third party"

  go_no_go_decision:
    pass_threshold: "6 of 8 samples must pass all criteria"
    if_pass: "Proceed with full 300-contact pull (note: this is a slower, more manual campaign)"
    if_fail: "Refine search queries and source selection"
    common_filter_adjustments:
      - "Add 'prototype' or 'manufacturing' keywords to filter out branding complaints"
      - "Require company website verification before including"
      - "Focus on LinkedIn over Reddit (easier to identify/reach)"
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
