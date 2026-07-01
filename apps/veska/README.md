# 🌟 Veska — our AI-native ERP (flagship)

> **Veska is our own open-source, AI-native ERP** — built by the maintainer of
> AI Workforce and featured here as its flagship. **One AI platform that runs your
> whole back office.** Describe your company in plain language and Veska configures
> CRM, support desk, finance, and HR — then your team works entirely through Slack,
> WhatsApp, and Email. No logins, no training.

**Veska is the one-click answer for five departments at once** —
[Sales](../../departments/sales/), [Support](../../departments/support/),
[Finance](../../departments/finance/), [HR](../../departments/hr/), and
[Operations](../../departments/operations/). Instead of wiring up separate tools,
you run one AI-native platform that covers all of them.

🔗 **Project:** [github.com/arunrajiah/veska](https://github.com/arunrajiah/veska) · Apache-2.0 · self-hosted · bring-your-own-LLM (local Ollama supported)

---

## Why it's the flagship

- **Conversational setup.** Type one sentence about your business; the AI stands up the back office in minutes.
- **Work happens in chat.** Slack, WhatsApp, Email, Telegram — employees, customers, and vendors never log into a dashboard.
- **Not a chat wrapper.** Real double-entry accounting (immutable ledger, invoices, expenses, budgets), an AI action agent with 57 audited ERP tools, multi-tenant RBAC + 2FA, a workflow engine, and a plugin SDK (Stripe, QuickBooks, Google Calendar ship in-repo).
- **Yours to run.** Apache-2.0, self-hosted, your data in your Postgres.

| Old way | Veska way |
|---|---|
| Months of setup, consultants, $50K–$500K | Describe your business → live in minutes, free |
| Employees log into complex dashboards | Everything in Slack / WhatsApp / Email |
| Rigid workflows, costly customization | AI understands context and adapts |

---

## Deploy it (one command)

```bash
git clone https://github.com/arunrajiah/veska.git
cd veska
cp .env.example .env          # set your LLM provider (local Ollama supported) + MAGIC_LINK_SECRET
docker compose up -d
docker compose exec api node apps/api/dist/db/migrate.js
# admin UI on http://localhost:3000
```

👉 **Go live on your domain with HTTPS (server, DNS, Caddy overlay, channels):
[GO-LIVE.md](GO-LIVE.md)** — uses Veska's official [`SELF_HOSTING.md`](https://github.com/arunrajiah/veska/blob/main/SELF_HOSTING.md) plus the Caddy overlay in this folder.

---

## What's in this folder

This is a thin **deploy wrapper** — it does not fork Veska. It adds an HTTPS layer
on top of Veska's own Docker Compose:

- [`Caddyfile`](Caddyfile) — automatic HTTPS; routes your domain → Veska's admin UI, `api.` subdomain → Veska's API.
- [`caddy-compose.yml`](caddy-compose.yml) — a Caddy container that attaches to Veska's Docker network.
- [`.env.example`](.env.example) — the domain/email for the overlay.
- [`GO-LIVE.md`](GO-LIVE.md) — the full walkthrough.

Prefer to assemble a department from individual AI tools instead? Each department
page keeps an AI-native **"🧩 Swap a component"** list.
