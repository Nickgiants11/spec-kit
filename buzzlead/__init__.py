"""
Buzzlead GTM Automation System
==============================

A comprehensive system for B2B lead generation research and campaign planning.

Agent Pipeline:
- Agent 1: Deep Research - Comprehensive client and market research
- Agent 2: GTM Strategy Generator - Campaign brief creation (not yet implemented)
- Agent 3: List Builder - Lead list generation (not yet implemented)
- Agent 4: Data Enrichment - Contact enrichment (not yet implemented)
- Agent 5: Copy Generator - Email copy creation (not yet implemented)

Usage:
    from buzzlead.agents import DeepResearchAgent

    agent = DeepResearchAgent.from_env()
    result = agent.run(onboarding_data)

For CLI usage:
    python -m buzzlead.run_agent1 --client "ClientName" --onboarding path/to/onboarding.json
"""

__version__ = "1.0.0"
__author__ = "Buzzlead"

from .agents import DeepResearchAgent
from .utils import Config, CostTracker

__all__ = [
    "DeepResearchAgent",
    "Config",
    "CostTracker",
]
