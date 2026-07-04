# 📈 Sales & Revenue

> Replace: an SDR/BDR + a CRM admin + a meeting-booking tool + a lead-enrichment subscription.

Wire a CRM, a scraper, and an automation engine together with an LLM and you have
a system that researches leads, writes personalized outreach, books demos, and
keeps the pipeline clean — the core loop of a sales development team.

**Recommended starter stack:** Veska (runs the whole department) + SalesGPT (AI sales agent) + our [AI SDR](../../apps/ai-sdr) flagship for outreach.

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

### [SalesGPT](https://github.com/filip-michalsky/SalesGPT)

> Context-aware AI sales agent for voice, email, and chat that advances prospects through configurable sales stages.

| | |
|---|---|
| **Stars** | ~2.7k |
| **Replaces** | Scripted SDR sequences / first-touch sales reps |
| **Self-host** | Medium — Docker Compose or Python, bring your own LLM keys |
| **Ship in** | ~1 hour |
| **Stack** | Python + LangChain / LiteLLM |
| **License** | MIT |

**Why it's on the list:** the sales-stage agent loop, product-knowledge tools, email follow-ups, and meeting/payment handoffs are the core product. It is more of an agent framework than a polished CRM, so pair it with a pipeline system rather than expecting a full sales suite.

---

Also: our [AI SDR](../../apps/ai-sdr) flagship drafts personalized outreach.

🚀 **Flagship app:** [`apps/ai-sdr`](../../apps/ai-sdr)
🏭 **Industry cross-links:** [Real Estate](../../industries/README.md#real-estate) · [E-commerce](../../industries/README.md#e-commerce--retail)
