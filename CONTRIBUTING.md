# Contributing to AI Workforce

Thanks for helping build the world's best directory of open-source AI apps that
run entire departments. Every good addition makes the repo more useful — and
more starred. Here's how to contribute well.

## Ways to contribute

Pick whatever fits — each has a one-click issue template ([open an issue](https://github.com/arunrajiah/ai-workforce/issues/new/choose)):

| I want to… | Use |
|---|---|
| 🚀 **Add an AI-native app** to a department or industry | [Suggest an app](.github/ISSUE_TEMPLATE/suggest-app.yml) → then a PR |
| 🐛 **Report a problem** — broken link, stale stars, dead/archived project, not AI-native | [Report a problem](.github/ISSUE_TEMPLATE/report-issue.yml) |
| 🔍 **Verify a page** — re-check that a page's entries are still accurate (great first PR) | [Verify a page](.github/ISSUE_TEMPLATE/verify-entries.yml) |
| 🏭 **Propose a new department or industry** (seeded with real tools) | [Suggest a vertical](.github/ISSUE_TEMPLATE/suggest-vertical.yml) |
| 🛠️ **Fix or add a one-click deploy** | [Improve a deploy](.github/ISSUE_TEMPLATE/improve-deploy.yml) |
| 💬 **Ask a question or float an idea** | [Discussions](https://github.com/arunrajiah/ai-workforce/discussions) |

**How contributions are reviewed** — the rubric, approval thresholds, verification cadence,
and how to become a trusted reviewer — is documented in **[REVIEWING.md](REVIEWING.md)**.
Read it before a big PR; it's exactly what reviewers check.

## What belongs here

An entry qualifies if it is **all** of the following:

1. **AI-native** — an LLM or an AI agent is at the tool's core; it does the work
   with AI. Legacy software with an "AI" add-on bolted on does **not** qualify
   (no generic CRMs, ERPs, helpdesks, or BI tools).
2. **Open source** — a real, public GitHub repository with an OSI-approved (or
   source-available) license. No closed SaaS, no "open core" that is useless
   without the paid tier.
3. **Self-hostable** — a team can run it on their own infrastructure.
4. **Department-grade** — it replaces or dramatically automates the work of a
   real role or department, not a toy demo.
5. **Shippable fast** — a competent person can get a working deployment in
   roughly a day or less (ideally an afternoon).

## How to add an app

1. Fork the repo and create a branch.
2. Add your entry to the correct file in [`departments/`](departments/), using
   the **exact card format** below.
3. If the app is industry-specific, also add a one-line pointer in
   [`industries/README.md`](industries/README.md).
4. Keep the department list ordered by usefulness (rough star/quality order).
5. Open a PR using the template. One app per PR keeps review fast.

### App card format

```markdown
### [Project Name](https://github.com/owner/repo)

> One sentence on what it does and the role it replaces.

| | |
|---|---|
| **Stars** | ~24k |
| **Replaces** | an SDR + a $99/mo outreach tool |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | Python / FastAPI |
| **License** | MIT |

**Why it's on the list:** one or two sentences of honest assessment.
```

## Rules that keep quality high

- **No dead or unverifiable links.** Every repo link must resolve. CI runs a
  link checker on every PR.
- **Real star counts.** Round to the nearest useful figure (`~24k`, `~1.2k`).
  Don't inflate.
- **Be honest in "Why it's on the list."** Note rough edges. Trust is the moat.
- **No affiliate links, no paid placement.** Ever.

## Flagship apps (`apps/`)

The [`apps/`](apps/) directory holds original, runnable reference apps built by
maintainers. To propose one, open an issue first so we can align on scope. Each
flagship app must run end-to-end with a documented `.env.example` and a
one-command start (`docker compose up` or an equivalent script), and should
include an **offline/mock mode** so it runs without API keys for evaluation.

## Tutorials (`docs/`)

Tutorials are Markdown/MDX with frontmatter (see [`docs/`](docs/)) so they render
on GitHub **and** publish to [hub.arunrajiah.com](https://hub.arunrajiah.com).
Follow the existing template and keep steps copy-pasteable.

## Code of conduct

Be kind and constructive. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
