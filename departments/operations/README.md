# ⚙️ Operations & Project Management

> Replace: a Zapier/Make bill + an internal-tools engineer + Jira/Notion/Confluence seats.

Operations is glue work: connect systems, track projects, and keep the company's
knowledge in one place. Open automation engines plus a project tracker and a wiki
cover it — and the automation layer is what every other department plugs into.

**Recommended starter stack:** Veska (runs the whole department). For AI automation glue, see the coding-agent tools in [Engineering](../engineering/).

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

_Operations is Veska's core. There isn't a strong single AI-native alternative that runs the whole department — for AI automation glue, see the coding-agent tools in [Engineering](../engineering/)._

---

