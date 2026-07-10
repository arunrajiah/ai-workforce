# AI Workforce (agents)
Curated catalog of open-source, AI-native apps mapped to the company departments they replace — a docs/awesome-list repo, not an application codebase.

## Stack
Markdown content repo. No build framework; helper scripts in `scripts/`.

## Layout
- `departments/` — one dir per department (sales, marketing, hr, finance, legal, engineering, data, design, operations, product, executive, support) with curated tool lists.
- `industries/` — 18 vertical-specific tool lists.
- `apps/` — flagship app writeups (ai-analyst, ai-sdr, ai-support-agent, veska).
- `scripts/` — maintenance/validation scripts.
- `docs/`, `assets/` — supporting docs and images.

## Commands
None (content repo). Check `scripts/` before assuming any validation tooling.

## Conventions
- Markdown lists with consistent entry format; badges and emoji headers in READMEs.
- No em dashes in user-facing copy.

## Token efficiency
- Grep/Glob to the target file; read only the relevant section, never whole large files.
- Don't re-read files after editing. Verify once per batch of edits, not per edit.
- Keep progress narration and final summaries to 2-3 sentences.
