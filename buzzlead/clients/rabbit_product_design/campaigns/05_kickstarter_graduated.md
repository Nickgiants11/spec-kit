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
