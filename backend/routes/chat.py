"""
Chat API routes (LLM + agents wired here in later iterations).
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/chat/status")
def chat_status() -> dict[str, str]:
    """Placeholder until chat streaming is implemented."""
    return {"message": "Chat API scaffold ready."}
