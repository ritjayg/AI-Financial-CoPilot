"""
Data agent: market / ticker context via services (yfinance, etc.).
Implement fetch and formatting logic here.
"""


class DataAgent:
    """Coordinates retrieval of financial data for the copilot."""

    async def build_context(self, user_message: str) -> str:
        """Return a text block of market context for the LLM (stub)."""
        _ = user_message
        return ""
