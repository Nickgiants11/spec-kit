# Tasks: GTM Strategy - Merge Your Data

**Input**: Design documents from `/specs/001-gtm-strategy-merge-your-data/`
**Prerequisites**: plan.md (required), spec.md (required)

**Target**: Generate 20+ qualified meetings per month within 90 days

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Account setup, tool access, and foundational configurations

- [ ] T001 Set up Calendly Pro account for Dan Saavedra (dan@mergeyourdata.com)
- [ ] T002 Configure Calendly meeting type "Revenue Health Check Discovery" (30 min, Mon-Fri 9am-5pm EST)
- [ ] T003 [P] Add Calendly booking form fields (Name, Email, Company, Size dropdown, Main Challenge, Source)
- [ ] T004 [P] Connect Calendly to HubSpot CRM (auto-create contact, deal, log meeting)
- [ ] T005 [P] Connect Calendly to Slack channel C0A1FLHBUE8 for booking notifications
- [ ] T006 Set up outreach tool account (Apollo.io, Instantly, or Lemlist)
- [ ] T007 Configure email sending domain with SPF, DKIM, DMARC records
- [ ] T008 Begin email domain warmup process (if new domain)
- [ ] T009 [P] Set up LinkedIn Campaign Manager admin access
- [ ] T010 Import DNC.csv into outreach tool as suppression list
- [ ] T011 [P] Create HubSpot pipeline stages (Lead → Discovery → Proposal → Negotiation → Closed Won/Lost)
- [ ] T012 Configure UTM tracking schema in HubSpot for attribution

**Checkpoint**: All accounts connected, booking flow tested end-to-end

---

## Phase 2: Foundational (List Building & Targeting)

**Purpose**: Build initial prospect lists meeting ICP criteria

**CRITICAL**: Lists must be DNC-verified before any outreach

### Import & Clean Existing Data

- [ ] T013 Import hubspot-crm-exports-re-targets-2025-12-05.xlsx into outreach tool
- [ ] T014 Segment imported contacts by recency (Hot: 0-3mo, Warm: 3-6mo, Cool: 6-12mo, Dormant: 12+mo)
- [ ] T015 [P] Verify all imported emails against DNC list
- [ ] T016 [P] Validate email addresses (remove bounced/invalid)
- [ ] T017 Tag contacts by segment for sequence assignment

### Build New Prospect Lists

- [ ] T018 Configure ICP search filters in prospecting tool:
  - Company size: 21-200 employees
  - Revenue: $1M-$100M
  - Location: United States, Canada
  - Technology: HubSpot
  - Industries: B2B Services, Manufacturing (B2B Industrial), Healthcare Tech, B2B SaaS
- [ ] T019 [P] Configure exclusion filters:
  - Industries: Loan services, Real estate
  - Funding: Pre-seed, Seed, Series A
  - Keywords: "hubspot", "revops"
- [ ] T020 Build initial CEO prospect list (250 contacts)
- [ ] T021 [P] Build initial CRO prospect list (250 contacts)
- [ ] T022 [P] Build initial VP Sales/Marketing prospect list (250 contacts)
- [ ] T023 [P] Build initial CMO/Other prospect list (250 contacts)
- [ ] T024 Verify all new lists against DNC.csv (zero tolerance)
- [ ] T025 Enrich prospects with trigger signals (leadership changes, funding, job postings)
- [ ] T026 Score and prioritize prospects by signal strength (3+ points = priority tier)

**Checkpoint**: 1,000 verified prospects loaded, segmented by title and priority

---

## Phase 3: User Story 1 - Cold Outbound List Generation (Priority: P1)

**Goal**: Generate validated prospect lists matching ICP with 80%+ criteria match

**Independent Test**: Compare sample against known good-fit clients (SimWell, Dineline, Supreme Group)

### Quality Validation

- [ ] T027 [US1] Pull 50-prospect sample from each title segment
- [ ] T028 [US1] Manually review sample against ICP criteria (4/5 minimum match)
- [ ] T029 [US1] Document any pattern issues (wrong industries, wrong sizes)
- [ ] T030 [US1] Adjust search filters based on validation findings
- [ ] T031 [US1] Re-pull lists with refined filters if quality below 80%

### Signal Enrichment

- [ ] T032 [US1] Configure trigger event monitoring in prospecting tool:
  - Leadership changes (past 6 months)
  - Job postings (RevOps, Sales Ops, Marketing Ops)
  - Funding announcements
  - Company expansion news
- [ ] T033 [US1] Tag high-signal prospects (score 3+) for priority outreach
- [ ] T034 [US1] Create saved searches for ongoing list building

### Reference Client Comparison

- [ ] T035 [US1] Research SimWell, Dineline, Supreme Group profiles
- [ ] T036 [US1] Document key characteristics that made them good fits
- [ ] T037 [US1] Create "ideal prospect" template based on reference clients
- [ ] T038 [US1] Score existing lists against ideal prospect template

**Checkpoint**: 1,000+ prospects verified, 80%+ ICP match, priority tier identified

---

## Phase 4: User Story 2 - Multi-Channel Outreach Sequences (Priority: P2)

**Goal**: Create personalized sequences by persona with pain-point messaging

**Independent Test**: Launch initial sequences, measure open rate 40%+, reply rate 5%+

### Email Sequence Creation

- [ ] T039 [US2] Write Email 1 (Pain Hook) - 3 subject line variants for A/B testing
- [ ] T040 [P] [US2] Write Email 2 (Case Study) - Supreme Group version
- [ ] T041 [P] [US2] Write Email 2 (Case Study) - Dineline version
- [ ] T042 [P] [US2] Write Email 2 (Case Study) - SimWell version
- [ ] T043 [US2] Write Email 3 (Trigger-Based) template with merge fields
- [ ] T044 [US2] Write Email 4 (Objection Handling) - competitor differentiation
- [ ] T045 [US2] Write Email 5 (Breakup) - final touchpoint

### Persona-Specific Messaging

- [ ] T046 [US2] Customize sequence for CEOs (pain: "leaving money on table")
- [ ] T047 [P] [US2] Customize sequence for CROs (pain: "embarrassed to show HubSpot")
- [ ] T048 [P] [US2] Customize sequence for VP Sales (pain: "deals slipping through cracks")
- [ ] T049 [P] [US2] Customize sequence for VP Marketing (pain: "can't calculate ROI")
- [ ] T050 [P] [US2] Customize sequence for CMOs (pain: "half database unengaged")

### Sequence Configuration

- [ ] T051 [US2] Build 7-touchpoint sequence in outreach tool:
  - Day 1: Email 1
  - Day 3: Email 2
  - Day 5: LinkedIn connection
  - Day 8: Email 3
  - Day 12: Email 4
  - Day 16: LinkedIn message
  - Day 21: Email 5
- [ ] T052 [US2] Configure A/B testing for Email 1 subject lines
- [ ] T053 [US2] Set up reply detection to pause sequence on response
- [ ] T054 [US2] Configure Calendly link insertion in all emails
- [ ] T055 [US2] Set sending limits (50/day initial, scale to 100/day after warmup)

### LinkedIn Connection Strategy

- [ ] T056 [US2] Write LinkedIn connection request note (under 300 characters)
- [ ] T057 [US2] Write LinkedIn follow-up message template
- [ ] T058 [US2] Configure LinkedIn outreach limits (20-25 connections/day)

### Launch & Monitor

- [ ] T059 [US2] Enroll first 100 prospects (CEO segment) in sequence
- [ ] T060 [US2] Monitor Day 1 metrics (deliverability, opens)
- [ ] T061 [US2] Scale to remaining segments if metrics healthy
- [ ] T062 [US2] Set up weekly reporting dashboard (sent, opened, replied, meetings)

**Checkpoint**: All sequences live, 40%+ open rate, 5%+ reply rate achieved

---

## Phase 5: User Story 3 - Pipeline Re-Engagement Campaign (Priority: P3)

**Goal**: Reactivate dormant contacts from existing database for quick wins

**Independent Test**: Book 10+ meetings from re-engagement within 30 days

### Re-Engagement Sequence Creation

- [ ] T063 [US3] Write Hot Contact sequence (0-3 months):
  - 3 touchpoints, 10 days
  - Reference previous conversation
  - New value angle (recent wins)
- [ ] T064 [P] [US3] Write Warm Contact sequence (3-6 months):
  - 5 touchpoints, 14 days
  - "Been a while" opener
  - Company update + case study
- [ ] T065 [P] [US3] Write Cool Contact sequence (6-12 months):
  - 4 touchpoints, 12 days
  - Re-introduction approach
  - Low-friction CTA (content first)
- [ ] T066 [P] [US3] Write Dormant Contact sequence (12+ months):
  - 4 touchpoints, 12 days
  - Near-cold with history reference
  - Major proof point lead

### Sequence Configuration

- [ ] T067 [US3] Build re-engagement sequences in outreach tool
- [ ] T068 [US3] Assign segmented contacts to appropriate sequences
- [ ] T069 [US3] Configure company change trigger monitoring for re-engagement list

### Launch Re-Engagement

- [ ] T070 [US3] Launch Hot Contact sequence first (highest probability)
- [ ] T071 [US3] Launch Warm Contact sequence after 3 days
- [ ] T072 [US3] Launch Cool/Dormant sequences after 7 days
- [ ] T073 [US3] Track meetings booked by segment
- [ ] T074 [US3] Document winning messaging for future use

**Checkpoint**: Re-engagement sequences live, 10+ meetings booked from database

---

## Phase 6: User Story 4 - Calendly Integration & Lead Capture (Priority: P4)

**Goal**: Frictionless booking with complete lead capture and notifications

**Independent Test**: Complete end-to-end booking flow, verify all integrations fire

### Booking Flow Optimization

- [ ] T075 [US4] Test Calendly booking flow from email link
- [ ] T076 [US4] Verify all required fields captured correctly
- [ ] T077 [US4] Test HubSpot contact/deal creation on booking
- [ ] T078 [US4] Test Slack notification to channel C0A1FLHBUE8
- [ ] T079 [US4] Configure email confirmation with prep questions

### Reminder System

- [ ] T080 [US4] Set up 24-hour reminder email
- [ ] T081 [US4] Set up 1-hour reminder email
- [ ] T082 [US4] Add reschedule option to reminders
- [ ] T083 [US4] Configure no-show follow-up sequence

### Lead Routing

- [ ] T084 [US4] Ensure all bookings assign to Dan Saavedra in HubSpot
- [ ] T085 [US4] Create HubSpot workflow for meeting follow-up tasks
- [ ] T086 [US4] Set up post-meeting outcome logging (Qualified, Not Qualified, No Show)

**Checkpoint**: Booking flow tested, all integrations working, notifications firing

---

## Phase 7: User Story 5 - LinkedIn Advertising (Priority: P5)

**Goal**: Launch LinkedIn ads targeting ICP for air cover and additional lead gen

**Independent Test**: Achieve CTR 0.5%+, CPL <$150, 5+ meetings/month from ads

### Campaign Setup

- [ ] T087 [US5] Create LinkedIn Campaign: "CEO Targeting" audience
  - Job Titles: CEO, Chief Executive Officer, Founder
  - Company Size: 21-200
  - Industries: ICP industries
  - Geography: US, Canada
- [ ] T088 [P] [US5] Create LinkedIn Campaign: "Revenue Leaders" audience
  - Job Titles: CRO, VP Sales, VP Marketing
  - Same company/geo filters
- [ ] T089 [P] [US5] Create LinkedIn Campaign: "Retargeting" audience
  - Website visitors (install LinkedIn Insight Tag)
  - Email list upload (engaged contacts)

### Ad Creative

- [ ] T090 [US5] Design ad creative: "Pain Agitation" concept
  - Image: Frustrated executive / messy dashboard
  - Copy: "$200K-$500K dormant pipeline" hook
- [ ] T091 [P] [US5] Design ad creative: "Proof-Led" concept
  - Image: Before/after stat highlight
  - Copy: "100+ companies, 22% revenue lift"
- [ ] T092 [P] [US5] Design ad creative: "Speed Differentiator" concept
  - Image: Speed/clock visual
  - Copy: "Prove ROI in 2 weeks, not 12"
- [ ] T093 [US5] Create landing page for ad traffic with Revenue Health Check CTA

### Lead Gen Form Setup

- [ ] T094 [US5] Create LinkedIn Lead Gen Form with fields:
  - First Name, Last Name, Email
  - Company Name, Company Size
  - Job Title
- [ ] T095 [US5] Connect Lead Gen Form to HubSpot via integration or Zapier
- [ ] T096 [US5] Create HubSpot workflow for LinkedIn leads (tag source, create deal)

### Campaign Launch

- [ ] T097 [US5] Set initial budget: $100/day ($3,000/month)
- [ ] T098 [US5] Configure bidding: Maximum delivery (initial)
- [ ] T099 [US5] Launch CEO campaign first
- [ ] T100 [US5] Launch Revenue Leaders campaign after 3 days
- [ ] T101 [US5] Monitor CPL, adjust creative based on performance
- [ ] T102 [US5] Launch retargeting campaign once pixel has 1,000+ audience

**Checkpoint**: LinkedIn ads live, CPL tracking, initial performance data collected

---

## Phase 8: Polish & Optimization

**Purpose**: Continuous optimization and scaling based on results

### Reporting & Attribution

- [ ] T103 [P] Create weekly GTM performance dashboard in HubSpot:
  - Prospects added / Emails sent
  - Open rate / Reply rate
  - Meetings booked / Source breakdown
  - LinkedIn ad spend / CPL
- [ ] T104 Set up monthly ROI calculation report
- [ ] T105 Document attribution for all closed deals

### Sequence Optimization

- [ ] T106 Analyze A/B test results, pick winning subject lines
- [ ] T107 Review reply sentiment, adjust messaging for objections
- [ ] T108 Identify best-performing case studies by persona
- [ ] T109 Update sequences based on learnings

### List Scaling

- [ ] T110 Load 250 new prospects weekly (ongoing)
- [ ] T111 Refine ICP criteria based on meeting quality
- [ ] T112 Document prospect characteristics that convert best

### Performance Review

- [ ] T113 Week 4 review: Are we on track for 20 meetings/month?
- [ ] T114 Week 8 review: What's working, what needs adjustment?
- [ ] T115 Week 12 review: 90-day ROI assessment

**Checkpoint**: GTM engine running, 20+ meetings/month achieved, clear ROI demonstrated

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies - start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 accounts being active
- **Phases 3-7 (User Stories)**: All depend on Phase 2 list completion
- **Phase 8 (Polish)**: Ongoing after initial launch

### Parallel Execution

**Can run in parallel:**
- T003, T004, T005 (Calendly integrations)
- T009, T010, T011, T012 (HubSpot/LinkedIn setup)
- T020, T021, T022, T023 (List building by segment)
- T040, T041, T042 (Case study variants)
- T046, T047, T048, T049, T050 (Persona sequences)
- T063, T064, T065, T066 (Re-engagement sequences)
- T087, T088, T089 (LinkedIn audiences)
- T090, T091, T092 (Ad creative)

### Critical Path

1. T001-T012 (Setup) → blocks all outreach
2. T013-T026 (Lists) → blocks sequence launch
3. T039-T062 (Sequences) → must complete before scaling
4. T075-T086 (Calendly) → must work before heavy volume

---

## Success Metrics by Phase

| Phase | Target Metric | Due |
|-------|---------------|-----|
| Setup | All accounts connected | Week 1 |
| Lists | 1,000 verified prospects | Week 2 |
| Sequences | First 500 prospects enrolled | Week 3 |
| Re-engagement | 10 meetings from database | Week 4 |
| LinkedIn | Ads live, tracking working | Week 4 |
| Month 1 | 15+ meetings booked | Day 30 |
| Month 2 | 20+ meetings booked | Day 60 |
| Month 3 | 20+ meetings, clear ROI | Day 90 |
