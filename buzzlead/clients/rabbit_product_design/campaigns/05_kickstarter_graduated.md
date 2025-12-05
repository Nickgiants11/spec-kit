# Campaign Brief: Kickstarter/Indiegogo Graduated
**Client:** Rabbit Product Design
**Generated:** December 5, 2024
**Status:** Draft - Pending Approval
**Priority:** 5 (Medium)

---

## Target Audience

```yaml
campaign_name: "Kickstarter/Indiegogo Graduated Founders"
target:
  industries:
    - "Consumer Electronics"
    - "Smart Home / IoT"
    - "Outdoor Products"
    - "Fitness Equipment"
    - "Kitchen Appliances"
    - "Travel Accessories"
    - "Tools"
  company_size:
    employees_min: 1
    employees_max: 20
    revenue_min: "$0"
    revenue_max: "$5M"
  personas:
    - title_keywords: ["Founder", "Co-Founder", "CEO", "Creator"]
      seniority: "Founder"
      department: "Executive"
  geography:
    countries: ["United States"]
    regions: []
  technologies: []
  keywords_in_profile:
    - "kickstarter"
    - "crowdfunding"
    - "inventor"
    - "hardware"
    - "product"
```

---

## Trigger Event

```yaml
trigger:
  name: "Successfully Funded Crowdfunding Campaign"
  description: "Hardware project raised $50K+ on Kickstarter or Indiegogo and now needs to transition from prototype to production. This is often where first-time hardware founders get stuck."
  signal_source: "Kickstarter Technology/Hardware category, Indiegogo Tech, Crowdfunding news"
  search_query: 'site:kickstarter.com (funded OR successful) hardware OR electronics'
  urgency: "medium-high"
  decay_rate: "6 months - window to reach out while they're figuring out manufacturing"
```

---

## Pain Point

```yaml
pain_point:
  problem: "Successfully funded campaign but now need to actually manufacture the product at scale—most first-time founders don't know how"
  symptom: "Getting inconsistent quotes from factories, prototype worked but design isn't manufacturable, backers are waiting"
  cost_of_inaction: "Angry backers, refund demands, reputation damage, product never ships"
  client_solution: "End-to-end support from prototype to production tooling and ramp-up, with the same senior engineer handling the entire journey"
```

---

## Proof Point

```yaml
proof_point:
  case_study: "N/A - No B2B case studies available"
  one_liner: "N/A"
  relevance: "N/A"
  fallback: "We handle tooling and ramp-up with the same engineer who designed it—no handoffs, no surprises. Our engineers have brought 1,000+ products to market."
```

---

## Enrichment Sources (For Agent 4)

```yaml
enrichment_sources:
  - source: "kickstarter_campaign"
    tool: "jina"
    url: "https://www.kickstarter.com/projects/{{creator}}/{{project}}"
    extract: ["funding_amount", "backer_count", "project_description", "creator_name", "delivery_date"]
    use_in_copy: "{{campaign_details}}"

  - source: "indiegogo_campaign"
    tool: "jina"
    url: "https://www.indiegogo.com/projects/{{project}}"
    extract: ["funding_amount", "backer_count", "project_description", "team_info"]
    use_in_copy: "{{campaign_details}}"

  - source: "linkedin_profile"
    tool: "serperdev"
    query: 'site:linkedin.com/in "{{creator_name}}" (kickstarter OR indiegogo OR founder)'
    extract: ["background", "location", "experience"]
    use_in_copy: "{{founder_context}}"

  - source: "campaign_updates"
    tool: "serperdev"
    query: '"{{project_name}}" (update OR manufacturing OR production OR delay)'
    extract: ["recent_updates", "production_status", "challenges_mentioned"]
    use_in_copy: "{{project_status}}"
```

---

## Copywriting Guidance (For Agent 5)

```yaml
copywriting:
  primary_template: "Storytelling"
  primary_rationale: "First-time founders respond well to stories of others who faced the same post-campaign manufacturing challenge"

  secondary_template: "Classic Twist"
  secondary_rationale: "Congratulate on the campaign success, then pivot to the real challenge ahead"

  tertiary_template: "Lead Magnet"
  tertiary_rationale: "Offer a free DFM review or manufacturing readiness checklist—high value for first-timers"

  tone: "founder-to-founder"
  length: "medium (400-500 chars)"

  hooks_to_test:
    - "Congrats on the successful campaign! The hard part is just starting—going from prototype to production is where most first-time hardware founders get stuck..."
    - "Saw [project name] crushed it on Kickstarter. Now comes the part nobody warns you about: actually manufacturing it..."
    - "Most crowdfunded hardware projects that miss their delivery date do so because the design wasn't production-ready. It's preventable..."
```

---

## AI Arc Filters (For Agent 3)

```json
{
  "ai_arc_filters": {
    "company_search": {
      "industries": ["Consumer Electronics", "Hardware", "IoT", "Outdoor", "Fitness", "Kitchen", "Travel"],
      "employee_count_min": 1,
      "employee_count_max": 20,
      "revenue_min": "0",
      "revenue_max": "5M",
      "locations": ["United States"],
      "keywords": ["kickstarter", "indiegogo", "crowdfunding", "hardware", "product"],
      "exclude_keywords": ["software", "SaaS", "app", "game", "film"]
    },
    "people_search": {
      "title_keywords": ["Founder", "Co-Founder", "CEO", "Creator", "Inventor"],
      "seniority_levels": ["Founder", "C-Suite"],
      "departments": ["Executive"],
      "profile_keywords": ["kickstarter", "crowdfunding", "inventor", "hardware", "product"]
    },
    "export_options": {
      "include_email": true,
      "email_confidence_min": 0.7,
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
    timing_logic: "Successfully funded crowdfunding campaigns create a 1-6 month window where founders have money, pressure from backers, and usually zero manufacturing experience. They've proven market demand but now face the hardest part."
    psychological_driver: "Post-campaign euphoria quickly turns to panic. Backers are waiting, the clock is ticking, and most first-time hardware founders realize they have no idea how to actually manufacture their product. Fear of public failure is intense."
    competitive_advantage: "Rabbit's end-to-end service (same engineer from design through manufacturing) directly addresses the handoff problems that kill crowdfunded products. 'No handoffs, no surprises' is exactly what they need."

  why_this_persona:
    decision_authority: "Crowdfunding creators are typically solo founders or tiny teams. The person who ran the campaign makes all vendor decisions. No procurement, no committee."
    pain_ownership: "They personally promised backers a product. Every delay, every missed update, every refund request lands on them personally. The pain is existential—their reputation is on the line."
    budget_access: "They literally have the money in hand from the campaign. A $200K campaign has budget for $30-50K in product development. The challenge is they don't know how to allocate it."

  why_this_message:
    hook_psychology: "Congratulating on the campaign validates their achievement. Then 'the hard part is just starting' creates alliance—we're not dismissing their success, we're warning them about the next challenge."
    proof_selection: "'Same engineer from design through manufacturing' addresses the nightmare scenario of multiple handoffs and finger-pointing. 'No handoffs, no surprises' is the promise."
    objection_preemption: "Offering a free DFM review or lead magnet lowers the barrier. First-timers don't know what they don't know. Education-first approach builds trust."

  expected_conversion_logic:
    why_they_reply: "They're overwhelmed and grateful for specific guidance. Most outreach they get is from overseas factories with unclear quality. Domestic expertise is refreshing."
    why_they_meet: "Low risk - they might learn something useful even if they don't hire. The DFM review/checklist offer gives them concrete value from the conversation."
    why_they_buy: "Backer pressure + fear of failure + reasonable cost + single point of accountability = motivated buyer. They want someone to guide them through the scary parts."
```

---

## List Building Methodology (HOW To Construct This List)

```yaml
list_building_methodology:
  step_1_source_identification:
    primary_source: "Kickstarter Technology/Design/Hardware categories - filter for successfully funded, $50K+ raised, campaign ended in last 6 months"
    secondary_sources:
      - "Indiegogo Tech & Gadgets - same filters"
      - "BackerKit or crowdfunding success announcements"
      - "Tech press coverage of successful crowdfunding campaigns"
    manual_sources:
      - "Kickstarter 'Projects We Love' in hardware categories"
      - "Product Hunt hardware launches that started on Kickstarter"
      - "YouTube crowdfunding campaign reviews"

  step_2_company_filtering:
    must_have_criteria:
      - "Hardware/physical product (not game, film, app, book)"
      - "Successfully funded ($50K+ to indicate serious project)"
      - "Campaign ended 1-6 months ago (optimal timing window)"
      - "US-based creator or US shipping"
    nice_to_have_criteria:
      - "Campaign updates mention manufacturing challenges"
      - "First-time creator (more likely to need help)"
      - "Complex product (electronics, multiple materials)"
    exclusion_criteria:
      - "Games, films, music, books, art projects"
      - "Simple products that don't need engineering (t-shirts, etc.)"
      - "Campaigns that already shipped (past the need)"
      - "Creator has professional manufacturing background"

  step_3_person_identification:
    target_titles_priority:
      tier_1: ["Creator", "Founder", "Inventor"]
      tier_2: ["CEO", "Co-Founder"]
      tier_3: ["N/A - crowdfunding creators are typically sole decision-makers"]
    max_contacts_per_company: 1
    title_selection_logic: "Target the campaign creator directly. This is always the decision-maker for crowdfunded projects."

  step_4_data_validation:
    email_requirements:
      minimum_confidence: 0.7
      required_format: "business OR personal email (many don't have company domains yet)"
      fallback_action: "Kickstarter message system, LinkedIn, or personal email"
    company_validation:
      verify_website_live: true
      verify_company_active: true
      recency_check: "Campaign ended within 6 months, product not yet shipped"

  step_5_enrichment_sequence:
    order_of_operations:
      - "Pull full Kickstarter campaign page (funding amount, backer count, timeline)"
      - "Read recent campaign updates for manufacturing status"
      - "Find creator LinkedIn profile for background"
      - "Check if they have a company website beyond Kickstarter"
    cost_optimization: "Kickstarter pages are free to scrape. Focus enrichment on promising leads only."

  step_6_deduplication:
    dedupe_against:
      - "Rabbit DNC list"
      - "Post-Funding campaign (some may have raised VC after crowdfunding)"
    merge_logic: "Keep in Kickstarter campaign - the crowdfunding angle is more specific and relatable."
```

---

## Sample Validation (Before Full Pull)

```yaml
sample_validation:
  purpose: "Test that crowdfunding filters yield hardware projects with reachable first-time creators"

  sample_size: 8 projects

  validation_checklist:
    - question: "Is this actually a hardware/physical product?"
      pass_criteria: "Physical product visible, requires manufacturing"
      fail_example: "Card game, mobile app, art book, music album"

    - question: "Did they raise enough to have budget for services?"
      pass_criteria: "$50K+ raised in campaign"
      fail_example: "$5K hobby project with no manufacturing budget"

    - question: "Is the timing right?"
      pass_criteria: "Campaign ended 1-6 months ago, product not yet shipped"
      fail_example: "Campaign ended 2 years ago (either shipped or dead)"

    - question: "Is the creator reachable?"
      pass_criteria: "Email findable or Kickstarter messages work"
      fail_example: "Anonymous creator with no contact info"

    - question: "Do they need product development help?"
      pass_criteria: "First-time creator or updates mention manufacturing challenges"
      fail_example: "Experienced product developer or factory owner running campaign"

  sample_companies:
    - company_name: "Peak Design"
      why_they_fit: "Iconic Kickstarter success, bags and camera gear"
      contact_name: "Peter Dering"
      contact_title: "Founder"
      trigger_evidence: "Multiple successful campaigns"
      validation_status: "FAIL - Established company, has internal manufacturing expertise"

    - company_name: "Coolest Cooler"
      why_they_fit: "One of biggest Kickstarter campaigns"
      contact_name: "Ryan Grepper"
      contact_title: "Creator"
      trigger_evidence: "$13M raised"
      validation_status: "FAIL - Historical example (2014), also had major manufacturing failures"

    - company_name: "[Recent smart home gadget]"
      why_they_fit: "Smart home device, $150K raised, 2 months post-campaign"
      contact_name: "[Creator name]"
      contact_title: "Founder"
      trigger_evidence: "First-time creator, electronics product, campaign ended recently"
      validation_status: "PASS - Ideal profile"

    - company_name: "[Recent outdoor gear project]"
      why_they_fit: "Outdoor gear, $80K raised, 3 months post-campaign"
      contact_name: "[Creator name]"
      contact_title: "Inventor"
      trigger_evidence: "Physical product, manufacturing needed"
      validation_status: "PASS - Good fit"

    - company_name: "[Recent fitness device]"
      why_they_fit: "Fitness tracker, $200K raised, updates mention supplier issues"
      contact_name: "[Creator name]"
      contact_title: "Creator"
      trigger_evidence: "Campaign updates show manufacturing struggles"
      validation_status: "PASS - High-intent prospect"

    - company_name: "[Recent kitchen gadget]"
      why_they_fit: "Kitchen tool, $60K raised, 4 months post-campaign"
      contact_name: "[Creator name]"
      contact_title: "Founder"
      trigger_evidence: "Physical product, first-time creator"
      validation_status: "PASS - Good fit"

    - company_name: "[Board game project]"
      why_they_fit: "Tabletop game"
      contact_name: "[Creator]"
      contact_title: "Creator"
      trigger_evidence: "N/A"
      validation_status: "FAIL - Not hardware, different manufacturing needs"

    - company_name: "[Recent wearable device]"
      why_they_fit: "Wearable tech, $500K raised, complex electronics"
      contact_name: "[Creator name]"
      contact_title: "Founder"
      trigger_evidence: "Electronics + firmware + manufacturing = complex"
      validation_status: "PASS - High-value prospect"

  go_no_go_decision:
    pass_threshold: "6 of 8 samples must pass all criteria"
    if_pass: "Proceed with full 300-contact pull"
    if_fail: "Refine category filters and funding thresholds"
    common_filter_adjustments:
      - "Exclude 'Games' and 'Publishing' categories entirely"
      - "Raise minimum funding to $75K if too many tiny projects"
      - "Focus on Technology, Design, and Hardware categories only"
      - "Add 'electronics' or 'manufacturing' keyword requirements"
```

---

## Campaign Metrics Targets

- **List size:** 300 contacts
- **Expected reply rate:** 2-3%
- **Expected meeting rate:** 50-60% of replies
- **Estimated meetings:** 3-5

---

## Notes & Considerations

1. **Filter for hardware only** - Many Kickstarter projects are games, films, apps—exclude these
2. **Funding threshold matters** - $50K+ raised = serious project with budget for services
3. **Timing window:**
   - Best: 1-3 months post-funding (still figuring things out)
   - Good: 3-6 months (may be hitting manufacturing walls)
   - Late: 6+ months (either figured it out or project is dead)
4. **Check campaign updates** for manufacturing struggles—great personalization opportunity
5. **Consider lead magnet approach** - Free "Manufacturing Readiness Checklist" or "DFM Review" could work well
6. **Sources to scrape:**
   - Kickstarter Technology category (funded, sorted by end date)
   - Kickstarter Hardware category
   - Indiegogo Tech & Gadgets
7. **Email may need to go to personal address** - Many crowdfunding creators don't have company domains yet
8. **Lower email confidence threshold (0.7)** - Founders often have less discoverable emails
