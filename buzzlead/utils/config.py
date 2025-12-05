"""
Buzzlead GTM Automation - Configuration Management
Loads API keys and settings from environment variables.
"""

import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

# Try to load dotenv if available
try:
    from dotenv import load_dotenv
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False


@dataclass
class Config:
    """Configuration container for Buzzlead GTM Automation."""

    # Research & Scraping
    jina_api_key: str
    jina_base_url: str
    spider_api_key: str
    spider_base_url: str
    serper_api_key: str
    serper_base_url: str

    # LLM Processing
    openrouter_api_key: str
    openrouter_base_url: str
    research_model: str
    scripting_model: str

    # List Building
    ai_arc_api_key: Optional[str] = None
    ai_arc_base_url: Optional[str] = None

    # Clay Integration
    clay_api_key: Optional[str] = None
    clay_base_url: Optional[str] = None

    # Email Verification
    millionverifier_api_key: Optional[str] = None
    bounceban_api_key: Optional[str] = None

    # Additional Data Sources
    lead_magic_api_key: Optional[str] = None
    findymail_api_key: Optional[str] = None

    # Paths
    base_path: Path = Path(__file__).parent.parent
    clients_path: Path = None
    knowledge_path: Path = None

    def __post_init__(self):
        """Set derived paths after initialization."""
        if self.clients_path is None:
            self.clients_path = self.base_path / "clients"
        if self.knowledge_path is None:
            self.knowledge_path = self.base_path / "knowledge"

    @classmethod
    def from_env(cls, env_file: Optional[Path] = None) -> "Config":
        """
        Load configuration from environment variables.

        Args:
            env_file: Optional path to .env file. If not provided,
                     looks for .env in the secrets directory.
        """
        # Load .env file if available
        if HAS_DOTENV:
            if env_file is None:
                env_file = Path(__file__).parent.parent / "secrets" / ".env"
            if env_file.exists():
                load_dotenv(env_file)

        # Required keys - will raise if missing
        required_keys = {
            "jina_api_key": "JINA_API_KEY",
            "spider_api_key": "SPIDER_API_KEY",
            "serper_api_key": "SERPER_DEV_API_KEY",
            "openrouter_api_key": "OPENROUTER_API_KEY",
        }

        missing = [env_var for env_var in required_keys.values()
                   if not os.getenv(env_var)]

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}. "
                f"Please copy secrets/.env.example to secrets/.env and fill in your API keys."
            )

        return cls(
            # Research & Scraping
            jina_api_key=os.getenv("JINA_API_KEY", ""),
            jina_base_url=os.getenv("JINA_BASE_URL", "https://r.jina.ai"),
            spider_api_key=os.getenv("SPIDER_API_KEY", ""),
            spider_base_url=os.getenv("SPIDER_BASE_URL", "https://api.spider.cloud"),
            serper_api_key=os.getenv("SERPER_DEV_API_KEY", ""),
            serper_base_url=os.getenv("SERPER_DEV_BASE_URL", "https://google.serper.dev"),

            # LLM Processing
            openrouter_api_key=os.getenv("OPENROUTER_API_KEY", ""),
            openrouter_base_url=os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1"),
            research_model=os.getenv("RESEARCH_MODEL", "openai/gpt-4.5-preview"),
            scripting_model=os.getenv("SCRIPTING_MODEL", "anthropic/claude-3-haiku"),

            # Optional keys
            ai_arc_api_key=os.getenv("AI_ARC_API_KEY"),
            ai_arc_base_url=os.getenv("AI_ARC_BASE_URL"),
            clay_api_key=os.getenv("CLAY_API_KEY"),
            clay_base_url=os.getenv("CLAY_BASE_URL"),
            millionverifier_api_key=os.getenv("MILLIONVERIFIER_API_KEY"),
            bounceban_api_key=os.getenv("BOUNCEBAN_API_KEY"),
            lead_magic_api_key=os.getenv("LEAD_MAGIC_API_KEY"),
            findymail_api_key=os.getenv("FINDYMAIL_API_KEY"),
        )

    def get_client_path(self, client_name: str) -> Path:
        """Get the path for a specific client's data."""
        # Sanitize client name for filesystem
        safe_name = "".join(c if c.isalnum() or c in "._- " else "_"
                          for c in client_name).strip()
        safe_name = safe_name.replace(" ", "_").lower()
        path = self.clients_path / safe_name
        path.mkdir(parents=True, exist_ok=True)
        return path
