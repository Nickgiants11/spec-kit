"""
Buzzlead GTM Automation - Cost Tracking
Tracks API usage and costs across all operations.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import Dict, Optional

logger = logging.getLogger(__name__)


@dataclass
class APIUsage:
    """Tracks usage for a single API."""
    count: int = 0
    tokens_in: int = 0
    tokens_out: int = 0
    est_cost: float = 0.0

    def add_call(
        self,
        cost: float = 0.0,
        tokens_in: int = 0,
        tokens_out: int = 0,
    ):
        """Record an API call."""
        self.count += 1
        self.tokens_in += tokens_in
        self.tokens_out += tokens_out
        self.est_cost += cost


@dataclass
class CostTracker:
    """
    Tracks all API usage and costs for a research session.
    """

    client_name: str
    jina: APIUsage = field(default_factory=APIUsage)
    spider: APIUsage = field(default_factory=APIUsage)
    serper: APIUsage = field(default_factory=APIUsage)
    openrouter: APIUsage = field(default_factory=APIUsage)
    started_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    completed_at: Optional[str] = None

    @property
    def total_estimated_cost(self) -> float:
        """Calculate total estimated cost across all APIs."""
        return (
            self.jina.est_cost +
            self.spider.est_cost +
            self.serper.est_cost +
            self.openrouter.est_cost
        )

    @property
    def total_api_calls(self) -> int:
        """Calculate total API calls across all APIs."""
        return (
            self.jina.count +
            self.spider.count +
            self.serper.count +
            self.openrouter.count
        )

    def track_jina(self, cost: float):
        """Track a Jina API call."""
        self.jina.add_call(cost=cost)
        logger.debug(f"Jina call tracked: ${cost:.4f}")

    def track_spider(self, cost: float):
        """Track a Spider API call."""
        self.spider.add_call(cost=cost)
        logger.debug(f"Spider call tracked: ${cost:.4f}")

    def track_serper(self, cost: float):
        """Track a SerperDev API call."""
        self.serper.add_call(cost=cost)
        logger.debug(f"SerperDev call tracked: ${cost:.4f}")

    def track_openrouter(
        self,
        cost: float,
        tokens_in: int = 0,
        tokens_out: int = 0,
    ):
        """Track an OpenRouter API call."""
        self.openrouter.add_call(
            cost=cost,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
        )
        logger.debug(f"OpenRouter call tracked: ${cost:.4f} ({tokens_in}+{tokens_out} tokens)")

    def complete(self):
        """Mark the tracking session as complete."""
        self.completed_at = datetime.utcnow().isoformat()

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return {
            "client": self.client_name,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "api_calls": {
                "jina": {
                    "count": self.jina.count,
                    "est_cost": round(self.jina.est_cost, 4),
                },
                "spider": {
                    "count": self.spider.count,
                    "est_cost": round(self.spider.est_cost, 4),
                },
                "serper": {
                    "count": self.serper.count,
                    "est_cost": round(self.serper.est_cost, 4),
                },
                "openrouter": {
                    "count": self.openrouter.count,
                    "tokens_in": self.openrouter.tokens_in,
                    "tokens_out": self.openrouter.tokens_out,
                    "est_cost": round(self.openrouter.est_cost, 4),
                },
            },
            "total_api_calls": self.total_api_calls,
            "total_estimated_cost": round(self.total_estimated_cost, 4),
        }

    def save(self, output_path: Path):
        """Save cost log to JSON file."""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
        logger.info(f"Cost log saved to {output_path}")

    def summary(self) -> str:
        """Generate a human-readable summary."""
        return f"""
Cost Summary for {self.client_name}
{'=' * 40}
Jina:      {self.jina.count:3d} calls  ${self.jina.est_cost:.4f}
Spider:    {self.spider.count:3d} calls  ${self.spider.est_cost:.4f}
SerperDev: {self.serper.count:3d} calls  ${self.serper.est_cost:.4f}
OpenRouter:{self.openrouter.count:3d} calls  ${self.openrouter.est_cost:.4f}
           ({self.openrouter.tokens_in:,} in + {self.openrouter.tokens_out:,} out tokens)
{'=' * 40}
TOTAL:     {self.total_api_calls:3d} calls  ${self.total_estimated_cost:.4f}
"""
