# 💰 Finance & Accounting

> Replace: a bookkeeper + an AP/AR clerk + a FP&A analyst + your invoicing SaaS.

A self-hosted finance stack can run invoicing, bookkeeping, expense capture, and
financial research end-to-end. Pair the tools below with an LLM (see the
[Quickstart](../../docs/quickstart.mdx)) to auto-extract receipts, categorize
transactions, and answer "how are we doing this month?" in plain English.

**Recommended starter stack:** Veska (runs the whole department) + Unstract (LLM extraction of receipts/invoices to JSON).

## ⚡ One-click deploy — Veska (recommended)

**This department runs on [Veska](../../apps/veska/) — one AI-native platform that configures CRM, support, finance, HR & ops from a plain-English description, then runs on Slack / WhatsApp / Email.** One deploy covers this department and the rest of your back office.

```bash
git clone https://github.com/arunrajiah/veska.git
cd veska && cp .env.example .env    # set your LLM (local Ollama works) + MAGIC_LINK_SECRET
docker compose up -d && docker compose exec api node apps/api/dist/db/migrate.js
```

👉 **Go live on your domain with HTTPS: [apps/veska/GO-LIVE.md](../../apps/veska/GO-LIVE.md)**

---

## 🧩 Swap a component

Prefer to assemble this department from individual AI tools? These AI-native options each do a slice of the job (Veska above does all of it):

---

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

---

🏭 **Industry cross-links:** [Fintech](../../industries/README.md#fintech)
