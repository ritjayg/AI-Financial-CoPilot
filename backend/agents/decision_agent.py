"""
Decision agent: reasoning and response synthesis via the LLM.
"""


class DecisionAgent:
    """Uses the LLM to produce user-facing answers given data context."""

    async def respond(self, user_message: str, market_context: str) -> str:
        """Generate a reply (stub)."""
        _ = (user_message, market_context)
        return "Decision agent not wired yet."
