# 🎧 Customer Support — one-click deploy

The whole support department in one command: **Chatwoot** (omnichannel helpdesk)
+ an **AI agent that auto-answers tickets** from your docs + **Caddy** for
automatic HTTPS.

```bash
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and the generated secrets
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
docker compose up -d
```

👉 **Full walkthrough (domain, DNS, first login, connecting the bot, adding channels):
[GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | a Tier-1 support team + Intercom/Zendesk + a doc-chat add-on |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (2 vCPU / 4 GB), a domain, Docker |
| **Includes** | Chatwoot, AI Support Agent, Caddy (HTTPS), Postgres/pgvector, Redis |

Want alternatives to any piece? See the [Support directory](../README.md).
