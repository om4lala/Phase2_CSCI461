"""
URL parsing utilities for CLI.
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ParsedURL:
    """Parsed URL with category and name."""
    raw: str
    category: str  # MODEL | DATASET | CODE | UNKNOWN
    name: str


def parse_url(u: str) -> ParsedURL:
    """
    Parse a URL and extract category and name.
    
    Args:
        u: URL string to parse
        
    Returns:
        ParsedURL with raw URL, category, and extracted name
        
    Examples:
        >>> parse_url("https://huggingface.co/google/gemma-3-270m/tree/main")
        ParsedURL(raw="...", category="MODEL", name="google/gemma-3-270m")
    """
    s = u.strip()
    if "huggingface.co" in s:
        if "/datasets/" in s:
            name = s.split("/datasets/", 1)[1].split("/", 1)[0]
            return ParsedURL(s, "DATASET", name)
        else:
            # Extract owner/model from HuggingFace URL
            # e.g., "https://huggingface.co/google/gemma-3-270m/tree/main" -> "google/gemma-3-270m"
            tail = s.split("huggingface.co/", 1)[1]
            parts = [p for p in tail.split("/") if p and p not in ("tree", "main", "blob")]
            name = "/".join(parts[:2]) if len(parts) >= 2 else (parts[0] if parts else s)
            return ParsedURL(s, "MODEL", name)
    if "github.com" in s:
        tail = s.split("github.com/", 1)[1]
        parts = [p for p in tail.split("/") if p]
        name = "/".join(parts[:2]) if len(parts) >= 2 else (parts[0] if parts else s)
        return ParsedURL(s, "CODE", name)
    return ParsedURL(s, "UNKNOWN", s)

