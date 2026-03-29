"""Lightweight ticker extraction from natural language (heuristic, not financial advice)."""

import re
from typing import Set

# Words that look like tickers but are common English — exclude from auto-detection.
_STOPWORDS: Set[str] = {
    "A", "I", "IT", "IS", "AM", "AN", "AS", "AT", "BE", "BY", "DO", "GO", "HE",
    "IF", "IN", "ME", "MY", "NO", "OF", "ON", "OR", "SO", "TO", "UP", "US", "WE",
    "THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN", "HER", "WAS",
    "ONE", "OUR", "OUT", "DAY", "GET", "HAS", "HIM", "HIS", "HOW", "ITS", "MAY",
    "NEW", "NOW", "OLD", "SEE", "TWO", "WHO", "WAY", "BUY", "SAY", "SHE", "TOO",
    "ANY", "BAD", "BIG", "END", "FEW", "GOT", "HAD", "OWN", "PUT", "RUN", "SET",
    "TRY", "YES", "YET", "IPO", "ETF", "EPS", "YTD", "Q1", "Q2", "Q3", "Q4",
}


def extract_candidate_tickers(text: str, max_symbols: int = 5) -> list[str]:
    """
    Find uppercase tokens that resemble US-style tickers (1–5 letters).
    Returns unique symbols in order of appearance, capped at max_symbols.
    """
    if not text:
        return []
    # Match standalone uppercase letter groups (word boundaries).
    raw = re.findall(r"\b([A-Z]{1,5})\b", text.upper())
    seen: set[str] = set()
    out: list[str] = []
    for sym in raw:
        if sym in _STOPWORDS or sym in seen:
            continue
        seen.add(sym)
        out.append(sym)
        if len(out) >= max_symbols:
            break
    return out
