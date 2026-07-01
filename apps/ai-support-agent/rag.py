"""Tiny dependency-free retrieval over a folder of Markdown/text docs.

Uses BM25-style lexical scoring so it works fully offline. Good enough to power a
real ticket-deflection demo; swap in a vector store (see docs/quickstart) for scale.
"""
from __future__ import annotations

import math
import re
from pathlib import Path

_WORD = re.compile(r"[a-z0-9]+")


def _tokenize(text: str) -> list[str]:
    return _WORD.findall(text.lower())


_HEADING = re.compile(r"^#{1,6}\s+", re.MULTILINE)


def _split_sections(text: str) -> list[str]:
    """Split Markdown on headings so each section is retrieved independently."""
    parts, cuts = [], [m.start() for m in _HEADING.finditer(text)]
    if not cuts:
        return [text]
    if cuts[0] > 0:
        parts.append(text[: cuts[0]])
    for i, start in enumerate(cuts):
        end = cuts[i + 1] if i + 1 < len(cuts) else len(text)
        parts.append(text[start:end])
    return parts


def _chunk(text: str, source: str, size: int = 160) -> list[dict]:
    """Chunk by Markdown section, further splitting any section over `size` words."""
    chunks: list[dict] = []
    for section in _split_sections(text):
        words = section.split()
        if not words:
            continue
        if len(words) <= size:
            chunks.append({"text": section.strip(), "source": source})
            continue
        for i in range(0, len(words), size):
            chunks.append({"text": " ".join(words[i : i + size]), "source": source})
    return chunks


class KnowledgeBase:
    def __init__(self, folder: str | Path):
        self.chunks: list[dict] = []
        self._tokens: list[list[str]] = []
        self._df: dict[str, int] = {}
        self._avg_len = 0.0
        self.load(folder)

    def load(self, folder: str | Path) -> None:
        folder = Path(folder)
        for path in sorted(folder.rglob("*")):
            if path.suffix.lower() not in {".md", ".markdown", ".txt"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            self.chunks.extend(_chunk(text, source=path.name))

        self._tokens = [_tokenize(c["text"]) for c in self.chunks]
        self._avg_len = (sum(len(t) for t in self._tokens) / len(self._tokens)) if self._tokens else 0.0
        for toks in self._tokens:
            for term in set(toks):
                self._df[term] = self._df.get(term, 0) + 1

    def search(self, query: str, k: int = 4) -> list[dict]:
        if not self.chunks:
            return []
        q_terms = _tokenize(query)
        n = len(self.chunks)
        k1, b = 1.5, 0.75
        scored = []
        for i, toks in enumerate(self._tokens):
            length = len(toks) or 1
            score = 0.0
            for term in q_terms:
                tf = toks.count(term)
                if not tf:
                    continue
                idf = math.log(1 + (n - self._df.get(term, 0) + 0.5) / (self._df.get(term, 0) + 0.5))
                denom = tf + k1 * (1 - b + b * length / (self._avg_len or 1))
                score += idf * (tf * (k1 + 1)) / denom
            if score > 0:
                scored.append((score, i))
        scored.sort(reverse=True)
        return [self.chunks[i] for _, i in scored[:k]]
