# Veska — AI-native ERP

An open-source, AI-native platform that configures a CRM, support desk, finance
ledger, and HR from a plain-English description of your business, then runs
through Slack, WhatsApp, and Email instead of a dashboard.

- **Replaces:** a CRM + helpdesk + bookkeeping software + HRIS, in one deploy — listed in [Sales](../../departments/sales/), [Support](../../departments/support/), [Finance](../../departments/finance/), [HR](../../departments/hr/), and [Operations](../../departments/operations/)
- **What's under the hood:** real double-entry accounting (immutable ledger, invoices, expenses, budgets), an AI action agent with 57 audited ERP tools, multi-tenant RBAC + 2FA, a workflow engine, a plugin SDK (Stripe, QuickBooks, Google Calendar)
- **License:** Apache-2.0, self-hosted, bring-your-own-LLM (local Ollama supported)
- **Disclosure:** built by this repo's maintainer. It's listed because there isn't yet a strong single-purpose AI-native alternative for these departments — judge it on the same bar as everything else here.

🔗 **Project:** [github.com/arunrajiah/veska](https://github.com/arunrajiah/veska)

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
page ([Sales](../../departments/sales/), [Support](../../departments/support/),
[Finance](../../departments/finance/), [HR](../../departments/hr/)) lists its own
AI-native options too.
