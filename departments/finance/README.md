# 💰 Finance & Accounting

> Replace: a bookkeeper + an AP/AR clerk + a FP&A analyst + your invoicing SaaS.

A self-hosted finance stack can run invoicing, bookkeeping, expense capture, and
financial research end-to-end. Pair the tools below with an LLM (see the
[Quickstart](../../docs/quickstart.mdx)) to auto-extract receipts, categorize
transactions, and answer "how are we doing this month?" in plain English.

**Recommended starter stack:** Unstract (LLM extraction of receipts/invoices to JSON).

## AI-native options

### [Unstract](https://github.com/Zipstack/unstract)

> LLM-driven document extraction that turns invoices, statements, and filings into structured JSON for finance workflows.

| | |
|---|---|
| **Stars** | ~6.7k |
| **Replaces** | Manual AP data entry / template-based invoice parsers |
| **Self-host** | Medium — `./run-platform.sh`, Docker Compose, and an LLM provider |
| **Ship in** | ~half a day |
| **Stack** | Python (Django/FastAPI) + React |
| **License** | AGPL-3.0 |

**Why it's on the list:** AI extraction is the core product: prompt-defined schemas produce JSON that can feed AP, reconciliation, and reporting systems directly — no template regex to maintain.

### [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot)

> Multi-agent platform where LLM agents perform equity research, valuation modeling (DCF, comps, LBO), and generate financial analysis reports.

| | |
|---|---|
| **Stars** | ~7.5k |
| **Replaces** | an FP&A/equity-research analyst building valuation models |
| **Self-host** | Medium — Python, bring your own LLM |
| **Ship in** | ~half a day |
| **Stack** | Python |
| **License** | Apache-2.0 |

**Why it's on the list:** an analysis agent, not accounting software — it separates deterministic financial computation from LLM narration, so the numbers come from code and the LLM writes the report around them.

### [Veska](https://github.com/arunrajiah/veska)

> AI-native ERP with a real double-entry ledger that configures from a plain-English description of your business, then runs from Slack/WhatsApp/Email. Covers this whole department, not just finance.

| | |
|---|---|
| **Stars** | ~2 (new project) |
| **Replaces** | invoicing/bookkeeping software + the rest of the back office, in one deploy |
| **Self-host** | Medium — `docker compose up`, bring your own LLM |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (Next.js) |
| **License** | Apache-2.0 |

**Why it's on the list:** there isn't yet a strong single-purpose AI-native bookkeeping tool in this space, so an all-in-one option is worth including. **Disclosure:** built by this repo's maintainer — judge it on the same bar as everything else here. [Go-live guide](../../apps/veska/GO-LIVE.md).

---

🏭 **Industry cross-links:** [Fintech](../../industries/README.md#fintech)
