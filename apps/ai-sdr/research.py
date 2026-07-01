"""Lightweight, dependency-free company research.

Fetches a company's homepage and extracts a usable signal (title, meta
description, and a few salient lines) using only the Python standard library.
Falls back gracefully when there's no network or the site blocks bots.
"""
from __future__ import annotations

import re
import urllib.request

_TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
_META = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
_OG = re.compile(
    r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
_TAG = re.compile(r"<[^>]+>")


def _clean(text: str) -> str:
    return re.sub(r"\s+", " ", _TAG.sub(" ", text)).strip()


def research(website: str | None, notes: str | None = None, timeout: int = 8) -> dict:
    """Return {'title', 'description', 'source'} for a company."""
    result = {"title": "", "description": (notes or "").strip(), "source": "notes"}
    if not website:
        return result

    url = website if website.startswith("http") else f"https://{website}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (AI-Workforce SDR)"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            html = resp.read(200_000).decode("utf-8", errors="ignore")
        title = _TITLE.search(html)
        desc = _META.search(html) or _OG.search(html)
        result["title"] = _clean(title.group(1)) if title else ""
        fetched_desc = _clean(desc.group(1)) if desc else ""
        # Prefer fetched description, keep notes as extra context.
        if fetched_desc:
            result["description"] = fetched_desc
        result["source"] = url
    except Exception as exc:
        result["error"] = f"Could not fetch {url}: {exc}"
    return result
