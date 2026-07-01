#!/usr/bin/env python3
"""Entry-format linter for AI Workforce.

Every tool card (`### [Name](url)`) in departments/ and industries/ must carry a
`Stars` row and a `License` row, and its heading must link to a real URL. Keeps
cards consistent and parseable. Run: python scripts/validate_entries.py
"""
from __future__ import annotations

import glob
import re
import sys

CARD = re.compile(r"^###\s+\[([^\]]+)\]\(([^)]+)\)\s*$")

# Files that are indexes / prose, not card lists — skipped.
SKIP = {"industries/README.md"}


def card_blocks(lines: list[str]):
    """Yield (name, url, heading_lineno, block_lines) for each ### [..](..) card."""
    starts = [i for i, ln in enumerate(lines) if CARD.match(ln)]
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        m = CARD.match(lines[start])
        yield m.group(1), m.group(2), start + 1, lines[start:end]


def main() -> int:
    files = sorted(glob.glob("departments/**/README.md", recursive=True) +
                   glob.glob("industries/**/README.md", recursive=True))
    problems: list[str] = []
    checked = 0
    for path in files:
        if path.replace("\\", "/") in SKIP:
            continue
        lines = open(path, encoding="utf-8").read().splitlines()
        for name, url, lineno, block in card_blocks(lines):
            checked += 1
            body = "\n".join(block)
            if not url.startswith("http"):
                problems.append(f"{path}:{lineno}  card '{name}' heading link is not a URL: {url}")
            if "**Stars**" not in body:
                problems.append(f"{path}:{lineno}  card '{name}' is missing a **Stars** row")
            if "**License**" not in body:
                problems.append(f"{path}:{lineno}  card '{name}' is missing a **License** row")

    if problems:
        print("Entry-format problems found:\n")
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) across {checked} cards.")
        return 1
    print(f"OK — {checked} cards validated, all well-formed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
