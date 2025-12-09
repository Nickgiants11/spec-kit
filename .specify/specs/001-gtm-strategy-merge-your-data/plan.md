# Implementation Plan: GTM Strategy - Merge Your Data

**Branch**: `001-gtm-strategy-merge-your-data` | **Date**: 2025-12-09 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-gtm-strategy-merge-your-data/spec.md`

---

## Summary

Implement a comprehensive go-to-market strategy for Merge Your Data, a HubSpot RevOps consultancy targeting B2B companies with undersized teams. The plan covers prospect list generation, multi-channel outreach sequences, pipeline re-engagement, Calendly setup, and LinkedIn advertising to generate 20+ qualified meetings per month.

---

## Technical Context

**Campaign Platform**: Email outreach tool (TBD - recommend Apollo.io, Instantly, or Lemlist)
**CRM**: HubSpot (client expertise)
**Scheduling**: Calendly (to be set up)
**Advertising**: LinkedIn Campaign Manager
**Data Enrichment**: Apollo.io, ZoomInfo, or similar
**Communication**: Slack (Channel C0A1FLHBUE8)
**Target Platform**: Multi-channel B2B outreach
**Performance Goals**: 20+ qualified meetings/month, 40%+ email open rate, 5%+ reply rate
**Constraints**: DNC compliance, CAN-SPAM compliance, LinkedIn connection limits
**Scale/Scope**: North American B2B market, 21-200 employee companies, $1M-$100M revenue

---

## GTM Architecture Overview

```text
┌─────────────────────────────────────────────────────────────────────┐
│                        LEAD GENERATION ENGINE                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   LIST       │    │  OUTREACH    │    │   BOOKING    │          │
│  │  BUILDING    │───▶│  SEQUENCES   │───▶│   & CLOSE    │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│         │                   │                   │                   │
│         ▼                   ▼                   ▼                   │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │ - ICP Match  │    │ - Email      │    │ - Calendly   │          │
│  │ - Enrichment │    │ - LinkedIn   │    │ - HubSpot    │          │
│  │ - DNC Filter │    │ - Phone      │    │ - Slack      │          │
│  │ - Signals    │    │ - A/B Test   │    │ - Follow-up  │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
│                                                                     │
├─────────────────────────────────────────────────────────────────────┤
│                         SUPPORTING CHANNELS                          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │  LINKEDIN    │    │    RE-       │    │   CONTENT    │          │
│  │    ADS       │    │ ENGAGEMENT   │    │  & LANDING   │          │
│  └──────────────┘    └──────────────┘    └──────────────┘          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Phase 0: Research & Setup

### 0.1 Tool Selection & Access

| Component | Recommended Tool | Alternative | Purpose |
|-----------|-----------------|-------------|---------|
| Outreach | Apollo.io | Instantly, Lemlist | Email sequences, prospecting |
| Data Enrichment | Apollo.io | ZoomInfo, Clearbit | Company/contact data |
| Scheduling | Calendly Pro | HubSpot Meetings | Meeting booking |
| LinkedIn Ads | LinkedIn Campaign Manager | - | Paid social |
| CRM | HubSpot | - | Lead management |
| Tracking | HubSpot + UTM | Mixpanel | Attribution |

### 0.2 Account Setup Requirements

- [ ] Calendly Pro account for Dan Saavedra
- [ ] Email domain warmup (if using new sending domain)
- [ ] LinkedIn Campaign Manager admin access
- [ ] HubSpot API access for integrations
- [ ] Apollo.io or equivalent prospecting tool

---

## Phase 1: List Building Strategy

### 1.1 ICP Search Criteria

**Primary Filters:**
```text
Company Size: 21-200 employees
Revenue: $1M-$100M (prioritize $5M-$25M)
Location: United States, Canada
Technology: HubSpot (detected via technographics)
Industries:
  - B2B Services > Marketing Firms, Tech Consultants, Business Consulting
  - Manufacturing > B2B Industrial Equipment
  - Healthcare Technology > Healthcare SaaS/Services
  - B2B SaaS > Platform/Infrastructure Software
```

**Exclusion Filters:**
```text
Industries: Loan services, Real estate, Financial services (lending)
Funding: Pre-seed, Seed, Series A
Keywords in company description: "hubspot", "revops", "revenue operations"
DNC List: Import and match against DNC.csv
```

**Title Targets (by priority):**
```text
Tier 1 (High): CEO, CRO, Chief Revenue Officer
Tier 2 (High): VP Sales, VP Marketing, VP Sales and Marketing
Tier 3 (Medium): CMO, Chief Marketing Officer
Tier 4 (Medium): Head of Sales, Head of Marketing, Director of RevOps
```

### 1.2 Signal-Based Prioritization

**Trigger Events to Monitor:**
1. Leadership change (VP Sales, VP Marketing, CRO, CEO) in last 6 months
2. Job posting for RevOps, Sales Ops, or Marketing Ops roles
3. Funding announcement with growth language
4. Company expansion/new market entry news
5. Active search for HubSpot help (Upwork, LinkedIn posts)

**Signal Scoring:**
- 3 points: Leadership change in target role
- 2 points: Active HubSpot help search
- 2 points: Funding with growth mentions
- 1 point: Job posting for ops roles
- 1 point: Company expansion news

Prioritize prospects with score 3+ for immediate outreach.

### 1.3 List Building Volumes

**Monthly Targets:**
- Week 1: 250 new prospects loaded
- Week 2: 250 new prospects loaded
- Week 3: 250 new prospects loaded
- Week 4: 250 new prospects loaded
- **Monthly Total**: 1,000 net new prospects

**Quality Gates:**
- All prospects verified against DNC list
- Email verification score 90%+
- Minimum 4/5 ICP criteria match

---

## Phase 2: Outreach Sequence Design

### 2.1 Primary Sequence: Cold Outbound (CEO/CRO Focus)

**Sequence Length**: 7 touchpoints over 21 days

| Day | Touchpoint | Channel | Purpose |
|-----|------------|---------|---------|
| 1 | Email 1 | Email | Pain hook + value prop |
| 3 | Email 2 | Email | Case study proof |
| 5 | LinkedIn | LinkedIn | Connection request + note |
| 8 | Email 3 | Email | Specific insight/trigger |
| 12 | Email 4 | Email | Objection handling |
| 16 | LinkedIn | LinkedIn | Engage with content/message |
| 21 | Email 5 | Email | Breakup email |

### 2.2 Email Templates Framework

**Email 1: Pain Hook**
```text
Subject Lines (A/B test):
A: "Your HubSpot is hiding $200K+ in pipeline"
B: "[Company] - quick question about your CRM"
C: "Reports don't match reality?"

Body Framework:
- Open with pain point ("Most [title]s I talk to say...")
- Quick proof (100+ companies, 22% revenue lift)
- Specific value prop (find $200K-$500K dormant pipeline week 1)
- Soft CTA (worth a 15-min chat?)
```

**Email 2: Case Study**
```text
Subject Lines:
A: "How [similar company] found $Xk in missed deals"
B: "Quick story about [industry] company like yours"

Body Framework:
- Reference Email 1
- Tell specific case study (Supreme Group, Dineline, SimWell)
- Quantified result
- CTA to Calendly
```

**Email 3: Trigger-Based**
```text
Subject Lines:
A: "Noticed [trigger event] - congrats!"
B: "[Company]'s growth + HubSpot"

Body Framework:
- Reference specific trigger (funding, new role, expansion)
- Connect to their likely challenges
- Position quick-start offer ($3K health check)
```

**Email 4: Objection Handling**
```text
Subject Lines:
A: "Not the typical HubSpot partner"
B: "Why we're different (quick read)"

Body Framework:
- Acknowledge likely objections (long engagements, unclear ROI)
- Counter with differentiators (2-week proof, revenue-focused)
- Reference competitor weaknesses
```

**Email 5: Breakup**
```text
Subject Lines:
A: "Closing your file"
B: "One last idea for [Company]"

Body Framework:
- Signal this is final outreach
- Summarize value left on table
- Leave door open
- Clear CTA or referral ask
```

### 2.3 Title-Specific Messaging Matrix

| Title | Primary Pain | Lead Message | Proof Point |
|-------|-------------|--------------|-------------|
| CEO | "Leaving money on table" | "Find dormant pipeline in week 1" | Revenue Recovery Sprint guarantee |
| CRO | "Embarrassed to show HubSpot" | "Clean data you can present to board" | Supreme Group consolidation |
| VP Sales | "Deals slipping through cracks" | "Zero deals lost to routing" | Speed-to-lead improvements |
| VP Marketing | "Can't calculate ROI" | "Attribution you can trust" | SimWell attribution case |
| CMO | "Half database unengaged" | "Reactivate dormant pipeline" | 22% revenue lift stat |

---

## Phase 3: Re-Engagement Campaign

### 3.1 Data Import Strategy

**Source**: hubspot-crm-exports-re-targets-2025-12-05.xlsx

**Segmentation Criteria:**
- **Hot (0-3 months)**: Recent activity, warm memory
- **Warm (3-6 months)**: Needs reminder of value
- **Cool (6-12 months)**: Requires re-introduction
- **Dormant (12+ months)**: Treat as near-cold with history reference

### 3.2 Re-Engagement Sequences

**Hot Contacts (0-3 months)**
- 3 touchpoints over 10 days
- Reference previous conversation
- New value angle (recent case study, new offer)
- Direct CTA to book

**Warm Contacts (3-6 months)**
- 5 touchpoints over 14 days
- "Been a while" opener
- Update on company growth
- Relevant case study
- Quick-start offer CTA

**Cool/Dormant Contacts (6+ months)**
- 4 touchpoints over 12 days
- Re-introduction approach
- Major proof point (100+ companies stat)
- Low-friction CTA (value-add content first)

### 3.3 Company Change Triggers

Monitor re-engagement list for:
- New funding rounds
- Leadership changes
- Company growth (headcount +20%)
- News mentions of expansion

Auto-trigger outreach when signals detected.

---

## Phase 4: Calendly Setup & Integration

### 4.1 Account Configuration

**Meeting Type**: Revenue Health Check Discovery Call
**Duration**: 30 minutes
**Availability**: Mon-Fri, 9am-5pm EST
**Buffer**: 15 minutes between meetings

### 4.2 Booking Form Fields

| Field | Type | Required |
|-------|------|----------|
| Name | Text | Yes |
| Email | Email | Yes |
| Company Name | Text | Yes |
| Company Size | Dropdown (1-20, 21-50, 51-200, 201+) | Yes |
| Main Challenge | Text Area | Yes |
| How did you hear about us? | Dropdown | No |
| Phone | Phone | No |

### 4.3 Integration Setup

**HubSpot Integration:**
- Auto-create contact on booking
- Create deal in pipeline
- Log meeting as activity
- Assign to Dan Saavedra

**Slack Integration:**
- Send notification to #C0A1FLHBUE8
- Include: Name, Company, Time, Challenge

**Email Confirmations:**
- Confirmation to booker with prep questions
- Notification to Dan with booking details
- Reminder 24 hours before
- Reminder 1 hour before

---

## Phase 5: LinkedIn Advertising

### 5.1 Campaign Structure

**Campaign Objective**: Lead Generation (LinkedIn Lead Gen Forms) + Website Traffic

**Audience Segments:**

**Segment A: CEOs**
```text
Job Titles: CEO, Chief Executive Officer, Founder, Co-Founder
Company Size: 21-200 employees
Industries: [ICP industries]
Geography: United States, Canada
```

**Segment B: Revenue Leaders**
```text
Job Titles: CRO, Chief Revenue Officer, VP Sales, VP Marketing
Company Size: 21-200 employees
Industries: [ICP industries]
Geography: United States, Canada
```

**Segment C: Retargeting**
```text
Website visitors (last 90 days)
Email list upload (engaged contacts)
```

### 5.2 Ad Creative Framework

**Ad Format**: Single Image + Sponsored Content

**Creative Concepts:**

1. **Pain Agitation**
   - Image: Frustrated executive looking at confusing dashboard
   - Copy: "Your HubSpot is hiding revenue. We find $200K-$500K in dormant pipeline in week 1."
   - CTA: Learn More

2. **Proof-Led**
   - Image: Before/after dashboard or stat highlight
   - Copy: "100+ companies. 22% average revenue lift. See what's possible for [industry]."
   - CTA: Get Your Free Assessment

3. **Speed Differentiator**
   - Image: Clock/speed visual
   - Copy: "Most HubSpot partners take 8-12 weeks. We prove ROI in 2."
   - CTA: Book a Call

### 5.3 Budget & Bidding

**Initial Monthly Budget**: $3,000-$5,000
**Bidding Strategy**: Maximum delivery (initially), optimize to CPL
**Target CPL**: <$150
**Target Meetings from Ads**: 5+/month

---

## Phase 6: Tracking & Attribution

### 6.1 UTM Structure

```text
Source: linkedin, email, organic
Medium: paid, outbound, referral
Campaign: gtm-q1-2025, reengagement-q1-2025
Content: ceo-pain, cro-proof, case-study-simwell
```

### 6.2 HubSpot Pipeline Stages

| Stage | Definition | Exit Criteria |
|-------|------------|---------------|
| Lead | Booked meeting | Meeting completed |
| Discovery | Had initial call | Qualified for offer |
| Proposal | Received proposal | Verbal yes/no |
| Negotiation | Discussing terms | Agreement reached |
| Closed Won | Signed contract | - |
| Closed Lost | Declined | Reason captured |

### 6.3 KPI Dashboard

**Weekly Metrics:**
- Prospects added to sequences
- Emails sent / opened / replied
- Meetings booked / completed
- LinkedIn ad spend / impressions / clicks

**Monthly Metrics:**
- Total meetings booked
- Meeting-to-opportunity rate
- Opportunity-to-close rate
- Revenue attributed to GTM
- Cost per meeting / cost per opportunity

---

## Project Structure

### Documentation (this feature)

```text
specs/001-gtm-strategy-merge-your-data/
├── spec.md              # GTM strategy specification
├── plan.md              # This implementation plan
├── tasks.md             # Actionable task breakdown
├── sequences/           # Email sequence templates
│   ├── cold-outbound.md
│   ├── re-engagement-hot.md
│   ├── re-engagement-warm.md
│   └── re-engagement-cold.md
├── targeting/           # List building criteria
│   └── icp-filters.md
├── ads/                 # LinkedIn ad specs
│   └── creative-briefs.md
└── tracking/            # Attribution setup
    └── utm-schema.md
```

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low email deliverability | Medium | High | Domain warmup, low daily volume initially |
| DNC violations | Low | High | Automated DNC matching before every send |
| LinkedIn account restrictions | Medium | Medium | Stay under daily limits, warm up gradually |
| Low reply rates | Medium | Medium | A/B test continuously, iterate messaging |
| Calendly no-shows | Medium | Low | Reminders, confirmation flow, easy reschedule |

---

## Success Metrics

**90-Day Targets:**
- 1,000+ prospects loaded into sequences
- 60+ meetings booked (20/month)
- 40%+ email open rate
- 5%+ email reply rate
- 6+ opportunities from GTM
- 2+ closed deals ($6K+ revenue from quick-starts)

**Attribution Target:**
- Clear source tracking on 90%+ of meetings
- ROI calculation for all GTM spend
