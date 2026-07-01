# 📈 Sales & Revenue

> Replace: an SDR/BDR + a CRM admin + a meeting-booking tool + a lead-enrichment subscription.

Wire a CRM, a scraper, and an automation engine together with an LLM and you have
a system that researches leads, writes personalized outreach, books demos, and
keeps the pipeline clean — the core loop of a sales development team.

**Recommended starter stack:** Veska (runs the whole department) + Firecrawl (lead research) + our [AI SDR](../../apps/ai-sdr) flagship for outreach. See the [AI SDR deploy guide](../../docs/departments/sales.mdx) and the bundled [`apps/ai-sdr`](../../apps/ai-sdr) flagship.

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

### [Firecrawl](https://github.com/mendableai/firecrawl)

> Turns any website into clean markdown/JSON — the enrichment/research backbone for prospecting.

| | |
|---|---|
| **Stars** | ~142k |
| **Replaces** | an SDR's manual research + Apollo/Clearbit-style enrichment |
| **Self-host** | Medium — compose + workers/queue |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (+ Rust/Go) |
| **License** | AGPL-3.0 (SDKs MIT) |

**Why it's on the list:** feed a company URL, get structured facts back — the fuel for personalized outreach.

Also: our [AI SDR](../../apps/ai-sdr) flagship drafts personalized outreach.

---

📘 **Deploy guide:** [Ship an AI SDR](../../docs/departments/sales.mdx) · 🚀 **Flagship app:** [`apps/ai-sdr`](../../apps/ai-sdr)
🏭 **Industry cross-links:** [Real Estate](../../industries/README.md#real-estate) · [E-commerce](../../industries/README.md#e-commerce--retail)
