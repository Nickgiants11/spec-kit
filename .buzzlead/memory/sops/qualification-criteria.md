# SOP: Qualification Criteria

> Standard Operating Procedure for qualifying companies and contacts.

## Overview

This SOP defines the standard qualification process and criteria for evaluating companies and contacts before they enter campaigns.

---

## Company Qualification

### Qualification Stages

```
Raw Data → Exclusion Check → ICP Scoring → Human Review → Qualified
```

### Stage 1: Exclusion Check

**Automatic Disqualification** (no review needed):
- Existing customers of the client
- Direct competitors
- Companies in excluded geographies
- Companies in excluded industries
- Companies that are closed/bankrupt
- Shell companies or holding companies

**Soft Disqualification** (human review):
- Indirect competitors
- Edge cases on size criteria
- Recently acquired companies
- Ambiguous company types

### Stage 2: ICP Scoring

Use ICP Fit Scorer agent with client-specific criteria.

**Scoring Components**:
| Component | Weight | Description |
|-----------|--------|-------------|
| Industry Fit | 25% | Match to target industries |
| Company Size | 25% | Employee count within range |
| Geography | 20% | Location match |
| Business Type | 15% | B2B, B2C, etc. |
| Additional | 15% | Client-specific criteria |

**Score Thresholds**:
| Score | Classification | Action |
|-------|---------------|--------|
| 85-100 | Excellent Fit | Auto-qualify |
| 70-84 | Strong Fit | Qualify |
| 55-69 | Moderate Fit | Human review |
| 40-54 | Weak Fit | Human review |
| 0-39 | Poor Fit | Auto-disqualify |

### Stage 3: Human Review

Review queue for:
- Companies scoring 40-69
- Companies flagged by exclusion check
- Companies with incomplete data
- Edge cases

**Review Decision Options**:
- QUALIFY - Add to qualified list
- DISQUALIFY - Remove from list
- NEEDS INFO - Research needed before decision
- ESCALATE - Unusual case, needs discussion

### Stage 4: Final Qualified List

Companies that:
- Passed exclusion check
- Score 70+ on ICP fit
- Or manually approved in human review

---

## Contact Qualification

### Qualification Stages

```
Raw Contacts → Title Scoring → Email Validation → LinkedIn Check → 90-Day Check → Qualified
```

### Stage 1: Title Relevance Scoring

Use Title Relevance Scorer agent with client personas.

**Score Thresholds**:
| Score | Classification | Action |
|-------|---------------|--------|
| 85-100 | High Priority | First tier outreach |
| 70-84 | Include | Standard outreach |
| 55-69 | Consider | Include if needed |
| 0-54 | Exclude | Do not include |

### Stage 2: Email Validation

Required for ALL contacts before campaign inclusion.

**Validation Flow**:
1. MillionVerifier bulk check
2. Debounce for catch-all/unknown
3. Final categorization

**Email Status Actions**:
| Status | Action |
|--------|--------|
| Valid | Include |
| Catch-all (verified) | Include with caution |
| Catch-all (unverified) | Exclude |
| Invalid | Exclude |
| Disposable | Exclude |
| Unknown | Exclude |

### Stage 3: LinkedIn Verification (Optional)

Use LinkedIn Verifier agent to:
- Confirm profile exists
- Verify current employment
- Check profile activity

**Priority for LinkedIn check**:
- All P1 contacts
- P2 contacts if time permits
- Skip for high-volume campaigns

### Stage 4: 90-Day Cooling Period

**Rule**: Do not contact anyone who was contacted within the last 90 days.

**Check Process**:
1. Pull contact history from Airtable
2. Filter contacts where last_contact_date > 90 days ago
3. Exclude recently contacted

**Exceptions** (require approval):
- Client specifically requests re-contact
- New offer/campaign substantially different
- Contact engaged positively but didn't convert

---

## Client-Specific Qualifications

Some clients have unique qualification requirements. Check client profile for:

### Custom Qualification Prompts
```
Location: .buzzlead/clients/[client]/profile.md
Section: Custom Prompts > Company Qualification Prompt
```

### Custom Exclusion Rules
```
Location: .buzzlead/clients/[client]/exclusions.md
```

### Modified Thresholds
Some clients may have:
- Higher/lower ICP score thresholds
- Additional required fields
- Specific industry requirements
- Custom persona definitions

---

## Qualification Metrics

Track for each campaign:

### Company Qualification
- Total companies scraped
- Excluded (auto): X (Y%)
- Excluded (manual): X (Y%)
- Qualified: X (Y%)
- Qualification rate: Z%

### Contact Qualification
- Total contacts scraped
- Title excluded: X (Y%)
- Email invalid: X (Y%)
- 90-day excluded: X (Y%)
- Final qualified: X (Y%)
- Qualification rate: Z%

---

## Quality Assurance

### Spot Checks
- Randomly review 10% of auto-qualified companies
- Verify exclusions are correctly applied
- Check for obvious misses

### Feedback Loop
- Track campaign performance by qualification score
- Adjust thresholds based on response rates
- Update ICP criteria based on learnings

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12-24 | Initial SOP |
