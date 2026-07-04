# The Review System

This repo's whole value is **trust** — every entry is real, AI-native, and honestly
assessed. This document is how we keep it that way as contributions scale. If you're
submitting a PR, skim [The bar](#the-bar); if you want to help review, read
[Reviewers](#reviewers).

## How a contribution flows

```
  Idea ──▶ Issue (optional, to align)
                │
                ▼
   Pull request ──▶ ① Automated checks (CI)
                          │  link-check + entry-format lint must pass
                          ▼
                    ② Review against the rubric
                          │  1 approval to add/edit a tool
                          │  2 approvals for a new department/industry or flagship
                          ▼
                       ③ Merge  ──▶ entry marked Verified (date + reviewer)
```

Small, focused PRs move fastest — **one app per PR**.

## The bar

An entry is accepted only if a reviewer can check **every** box. This is the rubric
reviewers score against, so self-check before you submit:

| # | Criterion | How it's checked |
|---|---|---|
| 1 | **AI-native** — an LLM / AI agent / ML model is the core of the tool | Reviewer opens the repo; a legacy app with an "AI" add-on fails |
| 2 | **Open source** — real, OSI-approved or clearly source-available license | License file on the repo; source-available is flagged in the card |
| 3 | **Self-hostable** — a team can run it on their own infra | Docker/compose or documented self-host path |
| 4 | **Shippable fast** — working deploy in ~a day or less | Reviewer sanity-checks the setup steps |
| 5 | **Verified & honest** — link resolves, stars ~right, assessment names rough edges | CI link-check + reviewer spot-check |
| 6 | **Correct placement & format** — right department/industry, exact card format | `CONTRIBUTING.md` card format; the CI linter |

Anything that can't clear the bar is closed with a short reason — not a judgment on the
project, just a fit call for this list.

## Automated checks (Tier 1)

Every PR runs CI before a human looks:

- **Link check** (`lychee`) — every repo link and internal link must resolve.
- **Entry lint** (`scripts/validate_entries.py`) — every `### [Name]` (a tool card) card must carry a `Stars` and a `License` row, so cards stay consistent and parseable.

Green CI doesn't mean "accepted" — it means "ready for human review."

## Human review (Tier 2)

- **Add or edit a tool:** **1** maintainer or trusted-reviewer approval.
- **New department / industry, or a flagship app:** **2** approvals (these reshape the map).
- Reviewers use the [rubric](#the-bar). If something's borderline, they ask in the PR rather than silently rejecting.
- **Target response time:** a first reply within ~5 days. Ping the PR if it goes quiet.

## 🔍 Verification — keeping the list honest

Entries drift: projects get archived, stars change, licenses flip. So verification is
continuous, not one-time.

- **On merge**, an entry is considered *Verified* as of that date.
- **Quarterly**, each department/industry page should be re-checked. Anyone can claim a
  page with the **[🔍 Verify a page](.github/ISSUE_TEMPLATE/verify-entries.yml)** issue
  template — it's the best first contribution.
- Re-verification confirms: repo still exists and is maintained, still AI-native, stars &
  license roughly current. Findings become a small PR.
- Entries whose project is archived/abandoned or no longer AI-native are **removed** (with
  a note in the PR) — a shorter, true list beats a long, stale one.

## Reviewers

Two roles keep review fast without lowering the bar:

- **Maintainers** — merge rights; own the roadmap and the final call.
- **Trusted reviewers** — community members who can approve PRs (their approval counts
  toward the thresholds above). We invite you after **3+ merged, high-quality
  contributions** (good judgment, honest assessments, clean format). Want in sooner? Do a
  few [verification passes](#-verification-keeping-the-list-honest) — they show exactly the
  judgment we look for.

Reviewers commit to: use the rubric, be kind and specific, disclose conflicts (e.g. don't
solo-approve your own project — that includes maintainers).

## What gets rejected (so you don't waste effort)

- Closed SaaS, or "open core" that's useless without the paid tier.
- Non-AI infrastructure (generic CRMs, ERPs, helpdesks, BI) — those workflows need an AI-native tool, not a legacy app.
- Toy demos, course projects, and single-digit-star hobby repos presented as production tools.
- Affiliate links, paid placement, or self-promo dressed as a neutral entry (disclose authorship — it's fine to submit your own project, just say so).
- Inflated stars or descriptions that hide real limitations.

---

Questions about a review? Open a [Discussion](https://github.com/arunrajiah/ai-workforce/discussions)
or ask right in the PR. See also [CONTRIBUTING.md](CONTRIBUTING.md).
