# AGENT 1: DEEP RESEARCH
# Trigger: /deep-research or "run deep research for [client]"

## HOW TO USE THIS AGENT

**Option 1: Paste onboarding form directly**
```
/deep-research

Client: ProductEVO
Website: https://productevo.com
[paste rest of onboarding data]
```

**Option 2: Reference a file**
```
/deep-research ProductEVO

(Claude Code will look for the onboarding form in /buzzlead/clients/productevo/onboarding.json)
```

---

## WHEN THIS AGENT IS TRIGGERED

You are Agent 1 in the Buzzlead GTM Automation pipeline. Follow these steps exactly:

---

## STEP 1: PARSE THE ONBOARDING DATA

Extract and confirm you have:
- [ ] Company name
- [ ] Website URL
- [ ] What they sell (offer description)
- [ ] Target industries
- [ ] Target job titles
- [ ] Company size ranges
- [ ] Pain points they solve
- [ ] Case studies/results (if provided)
- [ ] Sample ideal client URLs (5-10)
- [ ] DNC domains (if provided)

**If missing critical info**, ask the user before proceeding.

---

## STEP 2: SCRAPE CLIENT WEBSITE

### 2A: Homepage (via Jina)

Make this API call:

```
GET https://r.jina.ai/[client_website_url]
Headers:
  Authorization: Bearer jina_d07f2841800c4bd790a61627aae0c44cOFH1_cYT0JQj-c--LN3SSSgqUYiZ
```

Extract:
- Company description
- Core offering
- Key differentiators
- Any visible case studies or client logos

### 2B: Key Pages (via Spider) - MAX 5 PAGES

Only scrape if these pages exist:
- /about or /about-us
- /case-studies or /customers (PRIORITY)
- /services or /solutions
- /pricing (if public)

```
POST https://api.spider.cloud/crawl
Headers:
  Authorization: Bearer sk-0cf91c03-445c-4590-a9b8-63f666558484
  Content-Type: application/json
Body:
{
  "url": "[specific_page_url]",
  "limit": 1,
  "return_format": "markdown"
}
```

---

## STEP 3: SEARCH FOR CLIENT CONTEXT

### 3A: Recent News (via SerperDev)

```
POST https://google.serper.dev/search
Headers:
  X-API-KEY: 687524857dd97ed5a13d7bcbf80b7a5986d3ccc7
  Content-Type: application/json
Body:
{
  "q": "\"[company_name]\" (funding OR raised OR announces OR launches)",
  "num": 10
}
```

### 3B: Industry Context

```
{
  "q": "[client_industry] trends challenges 2024 2025",
  "num": 10
}
```

---

## STEP 4: SCRAPE SAMPLE IDEAL CLIENTS

For each URL in the sample ideal clients list (max 10):

### 4A: Homepage via Jina
Same as Step 2A, for each sample client URL.

Extract:
- What industry they're in
- Company size signals
- Technologies mentioned
- Recent news or announcements

### 4B: Optional - News search per sample client
```
{
  "q": "\"[sample_client_name]\" funding OR hiring OR expansion",
  "num": 5
}
```

---

## STEP 5: EXTRACT CLIENT'S CASE STUDIES

**CRITICAL: These are the CLIENT's case studies about THEIR customers.**

From the case studies page (scraped in Step 2B) and onboarding form, extract each case study:

For each one, structure as:
```
Customer Name: [who the client helped]
Industry: [customer's industry]
Problem: [what challenge they faced]
Solution: [what the client did]
Result: [specific numbers/outcomes]
Timeframe: [how long]

One-Liner: "We helped [customer type] [achieve result] in [timeframe]."
```

**If no case studies found**, flag this as a concern in the output.

---

## STEP 6: SYNTHESIZE EVERYTHING

Using GPT-5.1 via OpenRouter:

```
POST https://openrouter.ai/api/v1/chat/completions
Headers:
  Authorization: Bearer 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
  Content-Type: application/json
Body:
{
  "model": "openai/gpt-5.1",
  "temperature": 0.3,
  "max_tokens": 4000,
  "messages": [
    {
      "role": "system",
      "content": "[SYNTHESIS PROMPT - see below]"
    },
    {
      "role": "user",
      "content": "Here is all the research data: [all collected data]"
    }
  ]
}
```

### SYNTHESIS PROMPT:

```
You are a senior GTM strategist creating a Company Intelligence Document for cold email campaigns.

Create a document with these sections:

1. CLIENT SNAPSHOT
- Company name and one-liner
- Core offering
- Pricing (if known)
- Key differentiators (3-5 bullets)

2. IDEAL CLIENT PROFILE
Based on sample clients analyzed:
- Industries (ranked by fit)
- Company sizes
- Decision maker personas (titles, pain points, success metrics)
- Geographic focus
- Technologies used

3. PAIN POINTS & TRIGGERS
| Pain Point | Trigger Event | Where to Find Signal | Urgency |
|------------|---------------|---------------------|---------|

4. CLIENT'S CASE STUDIES (for cold emails)
For each case study:
- Customer type
- Problem → Solution → Result
- One-liner for email use
- Best audience to use this with

5. COMPETITIVE LANDSCAPE
- Who else solves this problem
- How client differentiates
- Why client wins

6. MESSAGING THEMES
- Primary value prop (one sentence)
- Secondary angles (3-5)
- Words to use / avoid
- Tone recommendation

7. RECOMMENDED CAMPAIGN ANGLES
3-5 distinct angles, each with:
- Target persona
- Trigger event
- Hook
- Which case study to reference

8. DATA SOURCES NEEDED PER CAMPAIGN
For each angle, what additional data to collect:
- Specific pages to scrape
- Search queries to run
- Enrichment fields needed

Be specific. Use actual names, numbers, examples from the research.
```

---

## STEP 7: OUTPUT THE RESULTS

Create two outputs:

### Output 1: Intelligence Document (Markdown)
Save to: `/buzzlead/clients/[client_name]/intelligence_doc.md`

### Output 2: Client Case Studies (Markdown)
Save to: `/buzzlead/clients/[client_name]/client_case_studies.md`

Structure:
```markdown
# [Client Name] Case Study Library
For use in cold email campaigns

## Case Study 1: [Customer Name]
- Industry:
- Problem:
- Solution:
- Result:
- One-Liner: "We helped..."
- Best for targeting: [industry/size/persona]

## Case Study 2: [Customer Name]
[repeat]

## Quick Reference
| Case Study | One-Liner | Best For |
|------------|-----------|----------|
```

---

## STEP 8: HUMAN CHECKPOINT

**STOP and present this summary:**

```
## Deep Research Complete: [Client Name]

### Executive Summary
[3-4 sentences about what this client does and who they serve]

### Top 3 Recommended Campaign Angles
1. [Angle name] - targeting [persona] with [trigger]
2. [Angle name] - targeting [persona] with [trigger]
3. [Angle name] - targeting [persona] with [trigger]

### Case Study Quality
- Found [X] case studies with specific results
- Quality score: [High/Medium/Low]
- [Any concerns about proof points]

### Research Quality
- Sources scraped: [count]
- API calls made: [count]
- Estimated cost: $[amount]

### Ready for Agent 2?
Type "approved" to proceed to GTM Strategy Generation, or provide feedback for adjustments.
```

---

## API REFERENCE (Quick Copy)

**Jina (Homepage Scraping)**
```
GET https://r.jina.ai/[url]
Authorization: Bearer jina_d07f2841800c4bd790a61627aae0c44cOFH1_cYT0JQj-c--LN3SSSgqUYiZ
```

**Spider (Page Scraping)**
```
POST https://api.spider.cloud/crawl
Authorization: Bearer sk-0cf91c03-445c-4590-a9b8-63f666558484
{"url": "[url]", "limit": 1, "return_format": "markdown"}
```

**SerperDev (Google Search)**
```
POST https://google.serper.dev/search
X-API-KEY: 687524857dd97ed5a13d7bcbf80b7a5986d3ccc7
{"q": "[query]", "num": 10}
```

**SerperDev (Google News)**
```
POST https://google.serper.dev/news
X-API-KEY: 687524857dd97ed5a13d7bcbf80b7a5986d3ccc7
{"q": "[query]", "num": 10}
```

**OpenRouter (GPT-5.1)**
```
POST https://openrouter.ai/api/v1/chat/completions
Authorization: Bearer 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
{"model": "openai/gpt-5.1", "messages": [...]}
```

---

## COST LIMITS

- Max 1 Jina call for client homepage
- Max 5 Spider calls total
- Max 10 Jina calls for sample clients
- Max 20 SerperDev queries
- 1 OpenRouter call for synthesis

Estimated cost per client: $2-5

---

## NEXT AGENT

After approval, trigger Agent 2:
```
/gtm-strategy [client_name]
```
