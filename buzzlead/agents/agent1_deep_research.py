"""
Buzzlead GTM Automation - Agent 1: Deep Research
=================================================

This agent conducts comprehensive research on a new client and their target market,
then synthesizes everything into a Company Intelligence Document for Agent 2.

Usage:
    from buzzlead.agents import DeepResearchAgent

    agent = DeepResearchAgent.from_env()
    result = agent.run(onboarding_data)
"""

import json
import logging
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

from ..utils.config import Config
from ..utils.api_clients import JinaClient, SpiderClient, SerperClient, OpenRouterClient
from ..utils.cost_tracker import CostTracker

logger = logging.getLogger(__name__)


# System prompt for research synthesis
SYNTHESIS_SYSTEM_PROMPT = """You are a senior GTM strategist at Buzzlead, a B2B lead generation agency that has generated $8M+ in client revenue across 50+ companies.

Your task is to synthesize raw research data into a structured Company Intelligence Document that will be used to create cold email campaigns.

## OUTPUT FORMAT

Create a document with these exact sections:

### 1. CLIENT SNAPSHOT
- Company name and one-line description
- Core offering (what they sell)
- Pricing model and range
- Key differentiators (3-5 bullets)
- Guarantee or risk reversal (if any)

### 2. IDEAL CLIENT PROFILE (ICP)
Based on the sample ideal clients analyzed:

**Company Characteristics:**
- Industries (ranked by fit)
- Company size (employees)
- Revenue range
- Geographic focus
- Technologies commonly used
- Growth stage (startup, scaling, mature)

**Decision Maker Personas:**
For each persona, include:
- Job titles
- Typical responsibilities
- Pain points they experience
- What success looks like for them
- How they evaluate solutions

### 3. PAIN POINTS & TRIGGERS
Map specific pain points to trigger events:

| Pain Point | Trigger Event | Signal Source | Urgency Level |
|------------|---------------|---------------|---------------|
| [pain] | [what happened] | [where to find] | High/Med/Low |

### 4. COMPETITIVE LANDSCAPE
- Direct competitors (who else solves this problem)
- How client differentiates
- Weaknesses of alternatives
- Why client wins

### 5. PROOF POINTS
Structure case studies for cold email use:

**Case Study 1: [Client Name]**
- Industry/Company Type:
- Problem they faced:
- Solution provided:
- Result achieved (specific numbers):
- One-sentence version for emails:

### 6. MARKET CONTEXT
- Industry trends affecting target market
- Regulatory or economic factors
- Timing considerations (seasonality, budget cycles)

### 7. MESSAGING THEMES
Based on all research, identify:
- Primary value proposition (one sentence)
- Secondary angles (3-5 alternatives)
- Words/phrases to use
- Words/phrases to avoid
- Tone recommendations

### 8. RECOMMENDED CAMPAIGN ANGLES
Suggest 3-5 distinct campaign angles:

**Angle 1: [Name]**
- Target: [specific persona/segment]
- Trigger: [what prompts outreach]
- Hook: [opening angle]
- Proof: [which case study to reference]

### 9. DATA COLLECTION RECOMMENDATIONS
For each campaign angle, specify:
- Additional data sources needed
- Specific pages to scrape
- SerperDev queries to run
- Enrichment requirements

### 10. RED FLAGS & EXCLUSIONS
- Companies/people to avoid
- Signals that indicate poor fit
- DNC patterns to watch for

---

## QUALITY STANDARDS

- Be specific, not generic. Use actual company names, numbers, and examples.
- Every claim should trace back to research data.
- Pain points should be real problems, not marketing speak.
- Case study summaries must include specific results (numbers, timeframes).
- Trigger events should be observable and searchable.
- Messaging themes should feel like founder-to-founder conversation, not corporate speak.
"""


@dataclass
class OnboardingData:
    """Structured client onboarding data."""

    company_name: str
    website: str
    industry: str = ""
    offer_summary: str = ""
    pricing_range: str = ""
    guarantee: str = ""
    differentiators: List[str] = field(default_factory=list)

    # ICP
    target_industries: List[str] = field(default_factory=list)
    employee_range: str = ""
    revenue_range: str = ""
    job_titles: List[str] = field(default_factory=list)
    geographic_focus: List[str] = field(default_factory=list)
    technologies: List[str] = field(default_factory=list)
    pain_points: List[str] = field(default_factory=list)

    # Proof
    case_studies: List[Dict[str, str]] = field(default_factory=list)
    results_achieved: List[str] = field(default_factory=list)
    client_logos: List[str] = field(default_factory=list)

    # Research inputs
    sample_ideal_clients: List[str] = field(default_factory=list)
    dnc_domains: List[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "OnboardingData":
        """Create from dictionary/JSON data."""
        # Handle nested structure from onboarding form
        client = data.get("client", {})
        icp = data.get("icp", {})
        proof = data.get("proof", {})

        return cls(
            company_name=client.get("company_name", data.get("company_name", "")),
            website=client.get("website", data.get("website", "")),
            industry=client.get("industry", data.get("industry", "")),
            offer_summary=client.get("offer_summary", data.get("offer_summary", "")),
            pricing_range=client.get("pricing_range", data.get("pricing_range", "")),
            guarantee=client.get("guarantee", data.get("guarantee", "")),
            differentiators=client.get("differentiators", data.get("differentiators", [])),
            target_industries=icp.get("industries", data.get("target_industries", [])),
            employee_range=icp.get("company_sizes", {}).get("employee_range", data.get("employee_range", "")),
            revenue_range=icp.get("company_sizes", {}).get("revenue_range", data.get("revenue_range", "")),
            job_titles=icp.get("job_titles", data.get("job_titles", [])),
            geographic_focus=icp.get("geographic_focus", data.get("geographic_focus", [])),
            technologies=icp.get("technologies", data.get("technologies", [])),
            pain_points=icp.get("pain_points", data.get("pain_points", [])),
            case_studies=proof.get("case_studies", data.get("case_studies", [])),
            results_achieved=proof.get("results_achieved", data.get("results_achieved", [])),
            client_logos=proof.get("client_logos", data.get("client_logos", [])),
            sample_ideal_clients=data.get("sample_ideal_clients", []),
            dnc_domains=data.get("dnc_domains", []),
        )

    @classmethod
    def from_json_file(cls, path: Path) -> "OnboardingData":
        """Load from JSON file."""
        with open(path) as f:
            return cls.from_dict(json.load(f))


@dataclass
class ResearchResult:
    """Container for all research data collected."""

    client_homepage: str = ""
    client_pages: Dict[str, str] = field(default_factory=dict)
    client_news: List[Dict] = field(default_factory=list)
    market_research: List[Dict] = field(default_factory=list)
    sample_client_data: Dict[str, Dict] = field(default_factory=dict)
    case_studies_extracted: List[Dict] = field(default_factory=list)
    sources_scraped: List[str] = field(default_factory=list)
    queries_run: List[str] = field(default_factory=list)


class DeepResearchAgent:
    """
    Agent 1: Deep Research

    Conducts comprehensive research on a new client and their target market,
    producing a Company Intelligence Document for campaign generation.
    """

    # Pages to attempt scraping on client website
    KEY_PAGES = [
        "/about",
        "/about-us",
        "/services",
        "/solutions",
        "/case-studies",
        "/customers",
        "/pricing",
    ]

    # Maximum Spider calls per client (cost control)
    MAX_SPIDER_CALLS = 5

    def __init__(
        self,
        config: Config,
        jina: JinaClient,
        spider: SpiderClient,
        serper: SerperClient,
        openrouter: OpenRouterClient,
    ):
        self.config = config
        self.jina = jina
        self.spider = spider
        self.serper = serper
        self.openrouter = openrouter

    @classmethod
    def from_env(cls, env_file: Optional[Path] = None) -> "DeepResearchAgent":
        """Create agent with configuration from environment."""
        config = Config.from_env(env_file)
        return cls(
            config=config,
            jina=JinaClient(config.jina_api_key, config.jina_base_url),
            spider=SpiderClient(config.spider_api_key, config.spider_base_url),
            serper=SerperClient(config.serper_api_key, config.serper_base_url),
            openrouter=OpenRouterClient(
                config.openrouter_api_key,
                config.openrouter_base_url,
                config.research_model,
            ),
        )

    def run(
        self,
        onboarding: OnboardingData,
        skip_synthesis: bool = False,
    ) -> Dict[str, Any]:
        """
        Execute full deep research workflow.

        Args:
            onboarding: Structured client onboarding data
            skip_synthesis: If True, skip LLM synthesis (for testing)

        Returns:
            Dictionary containing:
            - intelligence_doc_md: Narrative document (markdown)
            - intelligence_doc_json: Structured document (dict)
            - case_studies_md: Client case studies (markdown)
            - cost_summary: Cost tracking data
            - checkpoint_summary: Human review summary
        """
        logger.info(f"Starting deep research for {onboarding.company_name}")

        # Initialize tracking
        cost_tracker = CostTracker(client_name=onboarding.company_name)
        research = ResearchResult()
        output_path = self.config.get_client_path(onboarding.company_name)

        # Step 1: Scrape client website
        logger.info("Step 1: Scraping client website...")
        self._scrape_client_website(onboarding.website, research, cost_tracker)

        # Step 2: Research client context
        logger.info("Step 2: Researching client context...")
        self._research_client_context(onboarding, research, cost_tracker)

        # Step 3: Scrape sample ideal clients
        logger.info("Step 3: Analyzing sample ideal clients...")
        self._analyze_sample_clients(onboarding.sample_ideal_clients, research, cost_tracker)

        # Step 4: Extract case studies
        logger.info("Step 4: Extracting case studies...")
        self._extract_case_studies(onboarding, research)

        # Step 5: Synthesize research
        if not skip_synthesis:
            logger.info("Step 5: Synthesizing research with LLM...")
            intelligence_doc = self._synthesize_research(onboarding, research, cost_tracker)
        else:
            intelligence_doc = self._create_placeholder_doc(onboarding, research)

        # Step 6: Generate outputs
        logger.info("Step 6: Generating output files...")
        cost_tracker.complete()

        # Generate case studies markdown
        case_studies_md = self._generate_case_studies_md(onboarding, research)

        # Generate structured JSON
        intelligence_json = self._create_intelligence_json(onboarding, research, intelligence_doc)

        # Save all outputs
        self._save_outputs(
            output_path,
            intelligence_doc,
            intelligence_json,
            case_studies_md,
            cost_tracker,
        )

        # Generate checkpoint summary
        checkpoint_summary = self._generate_checkpoint_summary(
            onboarding, research, intelligence_json, cost_tracker
        )

        return {
            "intelligence_doc_md": intelligence_doc,
            "intelligence_doc_json": intelligence_json,
            "case_studies_md": case_studies_md,
            "cost_summary": cost_tracker.to_dict(),
            "checkpoint_summary": checkpoint_summary,
            "output_path": str(output_path),
        }

    def _scrape_client_website(
        self,
        website: str,
        research: ResearchResult,
        cost_tracker: CostTracker,
    ):
        """Scrape client homepage and key pages."""
        # Normalize URL
        if not website.startswith(("http://", "https://")):
            website = f"https://{website}"
        website = website.rstrip("/")

        # Step 2A: Homepage via Jina
        result = self.jina.scrape_url(website)
        if result.success:
            research.client_homepage = result.data
            research.sources_scraped.append(website)
            cost_tracker.track_jina(result.estimated_cost)
            logger.info(f"Successfully scraped homepage: {website}")
        else:
            logger.warning(f"Failed to scrape homepage: {result.error}")
            # Fallback to Spider
            result = self.spider.crawl_page(website)
            if result.success:
                research.client_homepage = str(result.data)
                research.sources_scraped.append(website)
                cost_tracker.track_spider(result.estimated_cost)

        # Step 2B: Key pages via Spider (limited calls)
        spider_calls = 0
        for page in self.KEY_PAGES:
            if spider_calls >= self.MAX_SPIDER_CALLS:
                logger.info(f"Reached Spider call limit ({self.MAX_SPIDER_CALLS})")
                break

            page_url = f"{website}{page}"
            result = self.spider.crawl_page(page_url)

            if result.success and result.data:
                # Check if we actually got content (not 404)
                content = str(result.data)
                if len(content) > 200 and "404" not in content[:100].lower():
                    research.client_pages[page] = content
                    research.sources_scraped.append(page_url)
                    spider_calls += 1
                    cost_tracker.track_spider(result.estimated_cost)
                    logger.info(f"Scraped {page}")

    def _research_client_context(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
        cost_tracker: CostTracker,
    ):
        """Research client news and market context."""
        client_name = onboarding.company_name
        industry = onboarding.industry or onboarding.target_industries[0] if onboarding.target_industries else ""

        # Client news queries
        news_queries = [
            f'"{client_name}" (funding OR raised OR announces OR launches OR partnership)',
            f'"{client_name}" site:linkedin.com/posts',
        ]

        # Market context queries
        market_queries = [
            f'"{industry}" trends 2024 2025',
            f'"{industry}" challenges pain points',
            f'"{industry}" top companies',
        ]

        if onboarding.offer_summary:
            offer_type = onboarding.offer_summary.split()[0:3]
            market_queries.append(f'"{" ".join(offer_type)}" market size trends')

        # Execute searches
        for query in news_queries:
            result = self.serper.search_news(query)
            if result.success:
                research.client_news.extend(result.data.get("news", []))
                research.queries_run.append(query)
                cost_tracker.track_serper(result.estimated_cost)

        for query in market_queries:
            result = self.serper.search(query)
            if result.success:
                research.market_research.append({
                    "query": query,
                    "results": result.data.get("organic", [])[:5],
                })
                research.queries_run.append(query)
                cost_tracker.track_serper(result.estimated_cost)

    def _analyze_sample_clients(
        self,
        sample_clients: List[str],
        research: ResearchResult,
        cost_tracker: CostTracker,
    ):
        """Analyze sample ideal client websites."""
        for url in sample_clients[:10]:  # Max 10 samples
            if not url.startswith(("http://", "https://")):
                url = f"https://{url}"

            # Scrape homepage
            result = self.jina.scrape_url(url)
            if result.success:
                research.sample_client_data[url] = {
                    "homepage": result.data,
                    "news": [],
                }
                research.sources_scraped.append(url)
                cost_tracker.track_jina(result.estimated_cost)

                # Quick news search for this sample
                company_name = self._extract_company_name(url)
                if company_name:
                    news_result = self.serper.search_news(f'"{company_name}" funding OR hiring OR news')
                    if news_result.success:
                        research.sample_client_data[url]["news"] = news_result.data.get("news", [])[:3]
                        cost_tracker.track_serper(news_result.estimated_cost)
            else:
                logger.warning(f"Failed to analyze sample client: {url}")

    def _extract_company_name(self, url: str) -> Optional[str]:
        """Extract likely company name from URL."""
        # Remove protocol and www
        domain = url.replace("https://", "").replace("http://", "").replace("www.", "")
        # Get base domain
        domain = domain.split("/")[0].split(".")[0]
        # Clean up
        if len(domain) > 2:
            return domain.title()
        return None

    def _extract_case_studies(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
    ):
        """Extract and structure case studies from research data."""
        # Start with case studies from onboarding form
        for cs in onboarding.case_studies:
            if isinstance(cs, dict):
                research.case_studies_extracted.append(cs)
            elif isinstance(cs, str):
                research.case_studies_extracted.append({
                    "raw_text": cs,
                    "customer_name": "Unknown",
                    "needs_enrichment": True,
                })

        # Extract from case studies page if scraped
        case_study_content = ""
        for page, content in research.client_pages.items():
            if "case-stud" in page or "customer" in page:
                case_study_content += content

        if case_study_content:
            # Simple extraction - in production would use LLM
            research.case_studies_extracted.append({
                "source": "website",
                "raw_content": case_study_content[:5000],
                "needs_enrichment": True,
            })

    def _synthesize_research(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
        cost_tracker: CostTracker,
    ) -> str:
        """Use LLM to synthesize research into intelligence document."""
        # Compile all research data
        research_data = self._compile_research_data(onboarding, research)

        # Call OpenRouter for synthesis
        result = self.openrouter.synthesize_research(
            research_data=research_data,
            system_prompt=SYNTHESIS_SYSTEM_PROMPT,
        )

        if result.success:
            cost_tracker.track_openrouter(
                result.estimated_cost,
                tokens_in=result.tokens_used // 2,  # Approximate split
                tokens_out=result.tokens_used // 2,
            )
            return result.data
        else:
            logger.error(f"Synthesis failed: {result.error}")
            return self._create_placeholder_doc(onboarding, research)

    def _compile_research_data(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
    ) -> str:
        """Compile all research data into a string for synthesis."""
        sections = []

        # Onboarding data
        sections.append("## CLIENT ONBOARDING DATA")
        sections.append(f"Company: {onboarding.company_name}")
        sections.append(f"Website: {onboarding.website}")
        sections.append(f"Industry: {onboarding.industry}")
        sections.append(f"Offer: {onboarding.offer_summary}")
        sections.append(f"Pricing: {onboarding.pricing_range}")
        sections.append(f"Target Industries: {', '.join(onboarding.target_industries)}")
        sections.append(f"Target Titles: {', '.join(onboarding.job_titles)}")
        sections.append(f"Company Size: {onboarding.employee_range}")
        sections.append(f"Pain Points: {', '.join(onboarding.pain_points)}")

        # Homepage content
        if research.client_homepage:
            sections.append("\n## CLIENT HOMEPAGE CONTENT")
            sections.append(research.client_homepage[:3000])

        # Key pages
        for page, content in research.client_pages.items():
            sections.append(f"\n## CLIENT PAGE: {page}")
            sections.append(content[:2000])

        # News
        if research.client_news:
            sections.append("\n## RECENT NEWS")
            for news in research.client_news[:5]:
                sections.append(f"- {news.get('title', '')}: {news.get('snippet', '')}")

        # Market research
        if research.market_research:
            sections.append("\n## MARKET RESEARCH")
            for item in research.market_research:
                sections.append(f"\nQuery: {item['query']}")
                for result in item["results"][:3]:
                    sections.append(f"- {result.get('title', '')}")

        # Sample clients
        if research.sample_client_data:
            sections.append("\n## SAMPLE IDEAL CLIENTS")
            for url, data in list(research.sample_client_data.items())[:5]:
                sections.append(f"\n### {url}")
                sections.append(data.get("homepage", "")[:1000])

        # Case studies
        if research.case_studies_extracted:
            sections.append("\n## CASE STUDIES FROM CLIENT")
            for cs in research.case_studies_extracted:
                sections.append(str(cs))

        return "\n".join(sections)

    def _create_placeholder_doc(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
    ) -> str:
        """Create placeholder document when synthesis is skipped or fails."""
        return f"""# Company Intelligence Document: {onboarding.company_name}

Generated: {datetime.utcnow().isoformat()}

## 1. CLIENT SNAPSHOT
- **Company:** {onboarding.company_name}
- **Website:** {onboarding.website}
- **Industry:** {onboarding.industry}
- **Offer:** {onboarding.offer_summary}

## 2. RESEARCH DATA COLLECTED

### Sources Scraped
{chr(10).join('- ' + s for s in research.sources_scraped)}

### Queries Run
{chr(10).join('- ' + q for q in research.queries_run)}

---

*This document requires synthesis. Run with synthesis enabled for full analysis.*
"""

    def _generate_case_studies_md(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
    ) -> str:
        """Generate case studies markdown document."""
        lines = [
            f"# {onboarding.company_name} Case Study Library",
            f"# For use in cold email campaigns",
            f"# Generated: {datetime.utcnow().isoformat()}",
            "",
            "---",
            "",
        ]

        for i, cs in enumerate(research.case_studies_extracted, 1):
            lines.append(f"## CASE STUDY {i}: {cs.get('customer_name', 'TBD')}")
            lines.append("")
            lines.append(f"**Industry:** {cs.get('customer_industry', 'TBD')}")
            lines.append(f"**Company Size:** {cs.get('customer_size', 'TBD')}")
            lines.append(f"**Challenge:** {cs.get('problem_faced', 'TBD')}")
            lines.append(f"**Solution:** {cs.get('solution_provided', 'TBD')}")
            lines.append(f"**Result:** {cs.get('result_achieved', 'TBD')}")
            lines.append(f"**Timeframe:** {cs.get('timeframe', 'TBD')}")

            if cs.get("quote"):
                lines.append(f'**Quote:** "{cs["quote"]}"')

            lines.append("")
            lines.append("### One-Liner for Emails:")
            one_liner = cs.get("one_liner", f'"We helped a similar company achieve great results."')
            lines.append(f'"{one_liner}"')
            lines.append("")
            lines.append("---")
            lines.append("")

        if not research.case_studies_extracted:
            lines.append("*No case studies extracted. Please provide case study data in onboarding form.*")
            lines.append("")
            lines.append("**IMPORTANT:** Cold emails without proof points perform significantly worse.")
            lines.append("Consider building case studies before scaling campaigns.")

        return "\n".join(lines)

    def _create_intelligence_json(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
        intelligence_doc: str,
    ) -> Dict[str, Any]:
        """Create structured JSON intelligence document."""
        return {
            "client_name": onboarding.company_name,
            "generated_at": datetime.utcnow().isoformat(),
            "version": "1.0",
            "client_snapshot": {
                "company_name": onboarding.company_name,
                "website": onboarding.website,
                "one_liner": onboarding.offer_summary,
                "core_offering": onboarding.offer_summary,
                "pricing": onboarding.pricing_range,
                "differentiators": onboarding.differentiators,
                "guarantee": onboarding.guarantee,
            },
            "icp": {
                "industries": [
                    {"name": ind, "fit_score": 8, "reasoning": "From onboarding"}
                    for ind in onboarding.target_industries
                ],
                "company_sizes": {
                    "employee_range": onboarding.employee_range,
                    "revenue_range": onboarding.revenue_range,
                },
                "personas": [
                    {
                        "title_patterns": [title],
                        "seniority": "Manager+",
                        "department": "",
                        "pain_points": onboarding.pain_points,
                        "success_metrics": [],
                    }
                    for title in onboarding.job_titles
                ],
                "geographic_focus": onboarding.geographic_focus,
                "technologies": onboarding.technologies,
            },
            "pain_trigger_map": [
                {
                    "pain_point": pain,
                    "trigger_event": "TBD - needs synthesis",
                    "signal_source": "TBD",
                    "urgency": "medium",
                    "search_query": f'"{pain}" site:linkedin.com/posts',
                }
                for pain in onboarding.pain_points
            ],
            "proof_points": research.case_studies_extracted,
            "campaign_angles": [],  # Filled by synthesis or Agent 2
            "messaging": {
                "primary_value_prop": onboarding.offer_summary,
                "secondary_angles": [],
                "words_to_use": [],
                "words_to_avoid": [],
                "tone": "founder-to-founder, direct, specific",
            },
            "exclusions": {
                "dnc_domains": onboarding.dnc_domains,
                "red_flag_signals": [],
                "poor_fit_indicators": [],
            },
            "research_metadata": {
                "sources_scraped": research.sources_scraped,
                "serper_queries_run": research.queries_run,
                "sample_clients_analyzed": list(research.sample_client_data.keys()),
            },
        }

    def _save_outputs(
        self,
        output_path: Path,
        intelligence_doc: str,
        intelligence_json: Dict,
        case_studies_md: str,
        cost_tracker: CostTracker,
    ):
        """Save all output files."""
        output_path.mkdir(parents=True, exist_ok=True)

        # Intelligence document (markdown)
        with open(output_path / "intelligence_doc.md", "w") as f:
            f.write(intelligence_doc)

        # Intelligence document (JSON)
        with open(output_path / "intelligence_doc.json", "w") as f:
            json.dump(intelligence_json, f, indent=2)

        # Case studies
        with open(output_path / "client_case_studies.md", "w") as f:
            f.write(case_studies_md)

        # Cost log
        cost_tracker.save(output_path / "cost_log.json")

        logger.info(f"All outputs saved to {output_path}")

    def _generate_checkpoint_summary(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
        intelligence_json: Dict,
        cost_tracker: CostTracker,
    ) -> str:
        """Generate human checkpoint summary for approval."""
        # Calculate data quality score
        score = self._calculate_quality_score(onboarding, research)

        # Identify concerns
        concerns = []
        if not research.case_studies_extracted:
            concerns.append("No case studies found - cold emails will be less effective")
        if len(research.sources_scraped) < 3:
            concerns.append("Limited website data scraped")
        if not research.client_news:
            concerns.append("No recent news found about client")
        if not onboarding.pain_points:
            concerns.append("No pain points specified in onboarding")

        # Get top campaign angles
        angles = intelligence_json.get("campaign_angles", [])
        if not angles:
            angles = [
                {"name": "Pain-Based", "description": "Target based on pain points"},
                {"name": "Trigger-Based", "description": "Target based on trigger events"},
                {"name": "Industry-Specific", "description": "Vertical-focused messaging"},
            ]

        summary = f"""
============================================
HUMAN CHECKPOINT #1: Research Review
============================================

CLIENT: {onboarding.company_name}
WEBSITE: {onboarding.website}

EXECUTIVE SUMMARY:
{onboarding.offer_summary or 'No offer summary provided'}

TARGET MARKET:
- Industries: {', '.join(onboarding.target_industries[:3]) or 'Not specified'}
- Titles: {', '.join(onboarding.job_titles[:3]) or 'Not specified'}
- Size: {onboarding.employee_range or 'Not specified'}

DATA QUALITY SCORE: {score}/10

RESEARCH STATS:
- Pages scraped: {len(research.sources_scraped)}
- Queries run: {len(research.queries_run)}
- Sample clients analyzed: {len(research.sample_client_data)}
- Case studies found: {len(research.case_studies_extracted)}

TOP 3 RECOMMENDED CAMPAIGN ANGLES:
{chr(10).join(f'{i+1}. {a["name"]}: {a.get("description", a.get("target_persona", ""))}' for i, a in enumerate(angles[:3]))}

{'CONCERNS:' if concerns else 'NO MAJOR CONCERNS'}
{chr(10).join(f'- {c}' for c in concerns)}

{cost_tracker.summary()}

============================================
DECISION REQUIRED:
Does this intelligence document accurately represent {onboarding.company_name}?

[ ] APPROVE - Proceed to Agent 2 (GTM Strategy Generator)
[ ] REVISE - Make adjustments before proceeding
[ ] REJECT - Gather more information first
============================================
"""
        return summary

    def _calculate_quality_score(
        self,
        onboarding: OnboardingData,
        research: ResearchResult,
    ) -> int:
        """Calculate data quality score (1-10)."""
        score = 5  # Base score

        # Positive factors
        if research.client_homepage:
            score += 1
        if len(research.client_pages) >= 2:
            score += 1
        if research.case_studies_extracted:
            score += 1
        if len(research.sample_client_data) >= 3:
            score += 1
        if onboarding.pain_points:
            score += 0.5
        if onboarding.job_titles:
            score += 0.5

        # Negative factors
        if not research.case_studies_extracted:
            score -= 2
        if not onboarding.pain_points:
            score -= 1

        return min(10, max(1, int(score)))
