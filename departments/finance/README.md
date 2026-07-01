# 💰 Finance & Accounting

> Replace: a bookkeeper + an AP/AR clerk + a FP&A analyst + your invoicing SaaS.

A self-hosted finance stack can run invoicing, bookkeeping, expense capture, and
financial research end-to-end. Pair the tools below with an LLM (see the
[Quickstart](../../docs/quickstart.mdx)) to auto-extract receipts, categorize
transactions, and answer "how are we doing this month?" in plain English.

**Recommended starter stack:** Veska (runs the whole department) + Paperless-ngx (receipt/invoice OCR) for AI document extraction.

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

### [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

> Document management with OCR — turn physical receipts and invoices into a searchable, taggable archive.

| | |
|---|---|
| **Stars** | ~43k |
| **Replaces** | Manual receipt filing / commercial DMS |
| **Self-host** | Easy — compose + install script |
| **Ship in** | ~1 hour |
| **Stack** | Python (Django) + Angular |
| **License** | GPL-3.0 |

**Why it's on the list:** the perfect front door for AI receipt/invoice extraction. OCR in, structured data out.

---

📘 **Deploy guide:** [Ship an AI finance back-office](../../docs/departments/finance.mdx)
🏭 **Industry cross-links:** [Fintech](../../industries/README.md#fintech)
