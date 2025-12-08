# AI Arc API Filter Reference
# AGENT 3 MUST USE ONLY THESE EXACT VALUES

## Request File Format

```json
{
  "source": "ai_arc",
  "audience_name": "descriptive-name-here",
  "filters": {
    "seniority": [],
    "industries": [],
    "company_size": "",
    "location": ""
  },
  "limit": 100,
  "requested_by": "Agent 3",
  "notes": "Campaign context"
}
```

---

## VALID FILTER VALUES

### Seniority (lowercase, exact)
```
"founder"
"c_suite"
"executive"
"director"
"manager"
"entry"
"intern"
```

### Company Size (exact strings)
```
"1-10"
"1-50"
"1-100"
"11-50"
"51-200"
"201-500"
"501-1000"
"1001-5000"
"5000+"
```

### Location (country name)
```
"United States"
"Canada"
"United Kingdom"
```

---

## INDUSTRIES - USE EXACT NAMES ONLY

**CRITICAL: Do NOT use generic terms like "SaaS", "IoT", "Hardware", "Tech", "Fintech"**

### Technology & Software
```
"software development"
"technology, information and internet"
"it services and it consulting"
"computer and network security"
"computer networking products"
"computer games"
"computer hardware manufacturing"
"computers and electronics manufacturing"
"semiconductor manufacturing"
"nanotechnology research"
"biotechnology research"
```

### Financial
```
"financial services"
"investment banking"
"investment management"
"capital markets"
"banking"
"insurance"
"venture capital and private equity principals"
```

### Business Services
```
"business consulting and services"
"professional training and coaching"
"staffing and recruiting"
"advertising services"
"market research"
"design services"
"legal services"
"accounting"
"human resources services"
```

### Healthcare & Medical
```
"hospitals and health care"
"medical practices"
"medical equipment manufacturing"
"pharmaceutical manufacturing"
"mental health care"
"wellness and fitness services"
"alternative medicine"
```

### Manufacturing
```
"automation machinery manufacturing"
"industrial machinery manufacturing"
"appliances, electrical, and electronics manufacturing"
"motor vehicle manufacturing"
"aviation and aerospace component manufacturing"
"defense and space manufacturing"
"chemical manufacturing"
"plastics manufacturing"
"food and beverage manufacturing"
"beverage manufacturing"
"personal care product manufacturing"
"furniture and home furnishings manufacturing"
"textile manufacturing"
"packaging and containers manufacturing"
"paper and forest product manufacturing"
"glass, ceramics and concrete manufacturing"
```

### Consumer & Retail
```
"consumer services"
"retail"
"retail apparel and fashion"
"retail luxury goods and jewelry"
"retail groceries"
"retail office equipment"
"retail art supplies"
"wholesale"
"wholesale building materials"
"wholesale import and export"
"e-learning providers"
```

### Media & Entertainment
```
"entertainment providers"
"movies, videos, and sound"
"animation and post-production"
"online audio and video media"
"broadcast media production and distribution"
"newspaper publishing"
"book and periodical publishing"
"performing arts"
"spectator sports"
"musicians"
"artists and writers"
"photography"
"graphic design"
```

### Real Estate & Construction
```
"real estate"
"leasing non-residential real estate"
"construction"
"architecture and planning"
"civil engineering"
```

### Transportation & Logistics
```
"transportation, logistics, supply chain and storage"
"truck transportation"
"freight and package transportation"
"maritime transportation"
"airlines and aviation"
"railroad equipment manufacturing"
"shipbuilding"
"warehousing and storage"
```

### Energy & Utilities
```
"oil and gas"
"utilities"
"renewable energy semiconductor manufacturing"
"mining"
```

### Education
```
"higher education"
"primary and secondary education"
"education administration programs"
```

### Government & Non-Profit
```
"government administration"
"government relations services"
"public policy offices"
"public safety"
"law enforcement"
"administration of justice"
"armed forces"
"legislative offices"
"non-profit organizations"
"philanthropic fundraising services"
"civic and social organizations"
"religious institutions"
"international affairs"
"international trade and development"
"think tanks"
"political organizations"
```

### Food & Hospitality
```
"food and beverage services"
"restaurants"
"hospitality"
"travel arrangements"
"recreational facilities"
"gambling facilities and casinos"
```

### Agriculture
```
"farming"
"ranching"
"dairy product manufacturing"
"fisheries"
```

### Other Services
```
"research services"
"information services"
"environmental services"
"facilities services"
"security and investigations"
"events services"
"writing and editing"
"translation and localization"
"veterinary services"
"individual and family services"
"printing services"
"wireless services"
"telecommunications"
"libraries"
"museums, historical sites, and zoos"
```

---

## KEYWORDS FILTER (USE SPARINGLY)

Keywords search across LinkedIn profile text. Use simple, common terms.

**Good:**
```json
"keywords": ["hardware", "product", "startup", "software", "IoT", "connected device"]
```

**Bad:**
```json
"keywords": ["IoT solutions provider", "smart home ecosystem", "cutting-edge hardware"]
```

---

## DEPARTMENT FILTER (LESS TESTED)

```
"executive"
"engineering"
"product"
"sales"
"marketing"
"operations"
"finance"
"human_resources"
```

---

## INDUSTRY MAPPING GUIDE

When Agent 2 specifies a general industry, map to valid values:

| Campaign Says | Use These Industries |
|---------------|---------------------|
| "SaaS" | `"software development"` |
| "Fintech" | `"financial services"` + `"software development"` |
| "Hardware startups" | `"computer hardware manufacturing"` or `"computers and electronics manufacturing"` |
| "IoT" | `"computers and electronics manufacturing"` + keywords `["IoT", "connected device"]` |
| "HealthTech" | `"hospitals and health care"` + `"software development"` |
| "Consumer Electronics" | `"computers and electronics manufacturing"` + `"appliances, electrical, and electronics manufacturing"` |
| "Smart Home" | `"computers and electronics manufacturing"` + keywords `["smart home", "connected"]` |
| "Wearables" | `"computers and electronics manufacturing"` + keywords `["wearable", "fitness"]` |
| "Medical Devices" | `"medical equipment manufacturing"` |
| "Industrial IoT" | `"automation machinery manufacturing"` + `"industrial machinery manufacturing"` |
| "Robotics" | `"automation machinery manufacturing"` + keywords `["robotics", "robot"]` |
| "Clean Tech" | `"renewable energy semiconductor manufacturing"` + `"environmental services"` |
| "EdTech" | `"e-learning providers"` + `"software development"` |
| "MarTech" | `"advertising services"` + `"software development"` |
| "HR Tech" | `"human resources services"` + `"software development"` |
| "Legal Tech" | `"legal services"` + `"software development"` |
| "PropTech" | `"real estate"` + `"software development"` |
| "InsurTech" | `"insurance"` + `"software development"` |
| "Logistics Tech" | `"transportation, logistics, supply chain and storage"` + `"software development"` |
| "FoodTech" | `"food and beverage manufacturing"` + `"software development"` |
| "AgTech" | `"farming"` + `"software development"` |
| "Fitness" | `"wellness and fitness services"` |
| "Outdoor" | `"consumer services"` + `"retail"` |

---

## BEST PRACTICES

### 1. Start Simple
Use 2-3 filters max. More filters = fewer results.

### 2. Recommended Filter Combos (Tested Working)
```
seniority + location                           (broadest)
seniority + industries + location              (good)
seniority + company_size + location            (good)
seniority + industries + company_size          (may return 0 if too narrow)
```

### 3. Limits
- Max 100 per request
- Default to 50 for sample pulls
- Default to 100 for full pulls

### 4. Validation Before Commit
Before creating any request file, verify:
- [ ] All seniority values are lowercase and from valid list
- [ ] All industry values are exact matches from valid list
- [ ] Company size is exact string format
- [ ] Location is proper country name
- [ ] Keywords are simple single words (not phrases)

---

## EXAMPLE: RABBIT CAMPAIGN 1 (CORRECTED)

**Campaign Brief Says:**
- Target: Hardware startups, IoT, Consumer Electronics
- Company size: 10-100 employees
- Persona: Founders, C-Suite

**WRONG Request (invalid values):**
```json
{
  "filters": {
    "seniority": ["founder", "c_suite"],
    "industries": ["Consumer Electronics", "Hardware", "IoT", "Smart Home"],
    "company_size": "1-100"
  }
}
```

**CORRECT Request (valid values):**
```json
{
  "filters": {
    "seniority": ["founder", "c_suite"],
    "industries": [
      "computer hardware manufacturing",
      "computers and electronics manufacturing",
      "appliances, electrical, and electronics manufacturing"
    ],
    "company_size": "1-100",
    "location": "United States",
    "keywords": ["hardware", "IoT", "consumer", "startup"]
  },
  "limit": 50
}
```

---

## VERSION

- v1.0 (Dec 2024): Initial reference from AI Arc API testing
