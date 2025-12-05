"""
Buzzlead GTM Automation - API Client Implementations
Handles all external API integrations with error handling and retry logic.
"""

import time
import logging
from typing import Optional, Dict, Any, List
from dataclasses import dataclass, field

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


def create_session_with_retries(
    retries: int = 3,
    backoff_factor: float = 0.3,
    status_forcelist: tuple = (500, 502, 503, 504),
) -> requests.Session:
    """Create a requests session with retry logic."""
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


@dataclass
class APICallResult:
    """Result from an API call with metadata."""
    success: bool
    data: Any
    error: Optional[str] = None
    status_code: Optional[int] = None
    tokens_used: int = 0
    estimated_cost: float = 0.0


class JinaClient:
    """
    Client for Jina Reader API - used for homepage scraping.
    Cost: ~$0.001 per call
    """

    def __init__(self, api_key: str, base_url: str = "https://r.jina.ai"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = create_session_with_retries()
        self.cost_per_call = 0.001

    def scrape_url(self, url: str, timeout: int = 30) -> APICallResult:
        """
        Scrape a URL using Jina Reader API.

        Args:
            url: The URL to scrape
            timeout: Request timeout in seconds

        Returns:
            APICallResult with markdown content or error
        """
        try:
            jina_url = f"{self.base_url}/{url}"
            headers = {"Authorization": f"Bearer {self.api_key}"}

            response = self.session.get(jina_url, headers=headers, timeout=timeout)
            response.raise_for_status()

            return APICallResult(
                success=True,
                data=response.text,
                status_code=response.status_code,
                estimated_cost=self.cost_per_call,
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"Jina scrape failed for {url}: {e}")
            return APICallResult(
                success=False,
                data=None,
                error=str(e),
                status_code=getattr(e.response, "status_code", None) if hasattr(e, "response") else None,
            )


class SpiderClient:
    """
    Client for Spider API - used for deep page scraping.
    Cost: ~$0.01 per page
    """

    def __init__(self, api_key: str, base_url: str = "https://api.spider.cloud"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = create_session_with_retries()
        self.cost_per_page = 0.01

    def crawl_page(
        self,
        url: str,
        limit: int = 1,
        return_format: str = "markdown",
        timeout: int = 60,
    ) -> APICallResult:
        """
        Crawl a specific page using Spider API.

        Args:
            url: The URL to crawl
            limit: Number of pages to crawl (keep low for cost control)
            return_format: Output format (markdown, html, text)
            timeout: Request timeout in seconds

        Returns:
            APICallResult with page content or error
        """
        try:
            spider_url = f"{self.base_url}/crawl"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "url": url,
                "limit": limit,
                "return_format": return_format,
            }

            response = self.session.post(
                spider_url, headers=headers, json=payload, timeout=timeout
            )
            response.raise_for_status()

            return APICallResult(
                success=True,
                data=response.json(),
                status_code=response.status_code,
                estimated_cost=self.cost_per_page * limit,
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"Spider crawl failed for {url}: {e}")
            return APICallResult(
                success=False,
                data=None,
                error=str(e),
                status_code=getattr(e.response, "status_code", None) if hasattr(e, "response") else None,
            )


class SerperClient:
    """
    Client for SerperDev API - used for Google search and news.
    Cost: ~$0.001 per search (1000 searches = $1)
    """

    def __init__(self, api_key: str, base_url: str = "https://google.serper.dev"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = create_session_with_retries()
        self.cost_per_search = 0.001

    def search(
        self,
        query: str,
        search_type: str = "search",
        num_results: int = 10,
        timeout: int = 30,
    ) -> APICallResult:
        """
        Execute a search using SerperDev API.

        Args:
            query: Search query
            search_type: Type of search (search, news, images)
            num_results: Number of results to return
            timeout: Request timeout in seconds

        Returns:
            APICallResult with search results or error
        """
        try:
            url = f"{self.base_url}/{search_type}"
            headers = {
                "X-API-KEY": self.api_key,
                "Content-Type": "application/json",
            }
            payload = {"q": query, "num": num_results}

            response = self.session.post(
                url, headers=headers, json=payload, timeout=timeout
            )
            response.raise_for_status()

            return APICallResult(
                success=True,
                data=response.json(),
                status_code=response.status_code,
                estimated_cost=self.cost_per_search,
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"SerperDev search failed for '{query}': {e}")
            return APICallResult(
                success=False,
                data=None,
                error=str(e),
                status_code=getattr(e.response, "status_code", None) if hasattr(e, "response") else None,
            )

    def search_news(self, query: str, num_results: int = 10) -> APICallResult:
        """Search Google News."""
        return self.search(query, search_type="news", num_results=num_results)

    def batch_search(
        self, queries: List[str], delay_between: float = 0.5
    ) -> List[APICallResult]:
        """
        Execute multiple searches with rate limiting.

        Args:
            queries: List of search queries
            delay_between: Delay between searches in seconds

        Returns:
            List of APICallResult objects
        """
        results = []
        for i, query in enumerate(queries):
            if i > 0:
                time.sleep(delay_between)
            results.append(self.search(query))
        return results


class OpenRouterClient:
    """
    Client for OpenRouter API - used for LLM synthesis.
    Cost varies by model.
    """

    # Cost per 1K tokens (input, output) for common models
    MODEL_COSTS = {
        "openai/gpt-4.5-preview": (0.075, 0.15),
        "openai/gpt-4-turbo": (0.01, 0.03),
        "openai/gpt-3.5-turbo": (0.0005, 0.0015),
        "anthropic/claude-3-opus": (0.015, 0.075),
        "anthropic/claude-3-sonnet": (0.003, 0.015),
        "anthropic/claude-3-haiku": (0.00025, 0.00125),
    }

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://openrouter.ai/api/v1",
        default_model: str = "openai/gpt-4.5-preview",
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.default_model = default_model
        self.session = create_session_with_retries()

    def complete(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 4000,
        timeout: int = 120,
    ) -> APICallResult:
        """
        Generate a completion using OpenRouter.

        Args:
            messages: List of message dicts with 'role' and 'content'
            model: Model to use (defaults to configured research model)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            timeout: Request timeout in seconds

        Returns:
            APICallResult with completion or error
        """
        model = model or self.default_model

        try:
            url = f"{self.base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
            payload = {
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }

            response = self.session.post(
                url, headers=headers, json=payload, timeout=timeout
            )
            response.raise_for_status()

            data = response.json()

            # Calculate cost
            usage = data.get("usage", {})
            input_tokens = usage.get("prompt_tokens", 0)
            output_tokens = usage.get("completion_tokens", 0)

            input_cost, output_cost = self.MODEL_COSTS.get(model, (0.01, 0.03))
            estimated_cost = (
                (input_tokens / 1000) * input_cost +
                (output_tokens / 1000) * output_cost
            )

            return APICallResult(
                success=True,
                data=data["choices"][0]["message"]["content"],
                status_code=response.status_code,
                tokens_used=input_tokens + output_tokens,
                estimated_cost=estimated_cost,
            )

        except requests.exceptions.RequestException as e:
            logger.error(f"OpenRouter completion failed: {e}")
            return APICallResult(
                success=False,
                data=None,
                error=str(e),
                status_code=getattr(e.response, "status_code", None) if hasattr(e, "response") else None,
            )

    def synthesize_research(
        self,
        research_data: str,
        system_prompt: str,
        model: Optional[str] = None,
    ) -> APICallResult:
        """
        Synthesize research data into a structured document.

        Args:
            research_data: Raw research data to synthesize
            system_prompt: System prompt for synthesis
            model: Model to use

        Returns:
            APICallResult with synthesized document
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": f"Synthesize this research into a Company Intelligence Document:\n\n{research_data}",
            },
        ]
        return self.complete(messages, model=model, max_tokens=4000)
