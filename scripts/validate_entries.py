#!/usr/bin/env python3
"""Entry-format + hub-frontmatter linter for AI Workforce.

1. Every tool card (`### [Name](url)`) in departments/ and industries/ must carry
   a `Stars` row and a `License` row, and its heading must link to a real URL.
2. Every file that's supposed to publish to hub.arunrajiah.com/docs — docs/*.mdx,
   departments/*/deploy/GO-LIVE.md, apps/*/GO-LIVE.md, industries/*/README.md —
   must open with valid YAML frontmatter carrying title/description/sidebar_label/
   slug/keywords. See CONTRIBUTING.md#hub-publishing.

Run: python scripts/validate_entries.py
"""
from __future__ import annotations

import glob
import re
import sys

CARD = re.compile(r"^###\s+\[([^\]]+)\]\(([^)]+)\)\s*$")

# Files that are indexes / prose, not card lists — skipped for the card check.
SKIP = {"industries/README.md"}

FRONTMATTER_REQUIRED_KEYS = ("title", "description", "sidebar_label", "slug", "keywords")


def check_frontmatter(paths: list[str]) -> list[str]:
    problems: list[str] = []
    for path in paths:
        text = open(path, encoding="utf-8").read()
        if not text.startswith("---\n"):
            problems.append(f"{path}:1  missing hub frontmatter (must start with '---')")
            continue
        end = text.find("\n---\n", 4)
        if end == -1:
            problems.append(f"{path}:1  frontmatter opened but never closed with '---'")
            continue
        block = text[4:end]
        for key in FRONTMATTER_REQUIRED_KEYS:
            if not re.search(rf"^{key}:", block, re.MULTILINE):
                problems.append(f"{path}:1  frontmatter missing '{key}:'")
        if re.search(r"^description:.*[^\[]:\s", block, re.MULTILINE):
            problems.append(f"{path}:1  'description:' contains an unescaped colon — likely breaks YAML")
    return problems


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

    hub_files = sorted(set(
        glob.glob("docs/*.mdx")
        + glob.glob("departments/*/deploy/GO-LIVE.md")
        + glob.glob("apps/*/GO-LIVE.md")
        + glob.glob("industries/README.md")
        + glob.glob("industries/*/README.md")
    ))
    fm_problems = check_frontmatter(hub_files)
    problems.extend(fm_problems)

    if problems:
        print("Entry-format / hub-frontmatter problems found:\n")
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) across {checked} cards and {len(hub_files)} hub-publishable files.")
        return 1
    print(f"OK — {checked} cards and {len(hub_files)} hub-publishable files validated, all well-formed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
