---
title: Go live — Customer Support in one command
description: Deploy a complete, AI-powered support department (Chatwoot + auto-answering bot) with HTTPS in under an hour.
sidebar_label: Support — Go Live
slug: /departments/support/deploy
keywords: [chatwoot self-host, ai support agent, helpdesk docker, one click deploy]
---

# 🎧 Customer Support — go live in one command

This stack **is** a support department:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   customers ──────────▶ │  https://support.yourdomain.com                    │
   (chat / email / social)                    │                               │
                         └───────────────────┼───────────────────────────────┘
                                             ▼
                                    Chatwoot (helpdesk)
                                     │            ▲
                        new message  │            │  drafted answer
                                     ▼            │
                             AI Support Agent (RAG over your docs)
                                     │
                          Postgres/pgvector · Redis
```

You get an omnichannel helpdesk **and** an AI agent that auto-answers incoming
tickets from your own documentation — behind real HTTPS on your domain.

- **Replaces:** a Tier-1 support team + Intercom/Zendesk + a "chat with our docs" add-on
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, and Docker

---

## Step 1 — Get a server

Any Ubuntu 22.04+ VPS with **2 vCPU / 4 GB RAM** (minimum) works — Hetzner, DigitalOcean,
Vultr, AWS Lightsail, etc. SSH in, then install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

## Step 2 — Point your domain at it

Create a DNS **A record** for `support.yourdomain.com` → your server's IP.
Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short support.yourdomain.com   # should print your server IP
```

## Step 3 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/support/deploy
cp .env.example .env
```

## Step 4 — Fill in `.env`

Generate the secrets and edit the file:

```bash
echo "SECRET_KEY_BASE=$(openssl rand -hex 64)"
echo "POSTGRES_PASSWORD=$(openssl rand -hex 24)"
echo "REDIS_PASSWORD=$(openssl rand -hex 24)"
```

In `.env`, set at minimum:

- `DOMAIN` and `FRONTEND_URL` → `support.yourdomain.com` / `https://support.yourdomain.com`
- `ACME_EMAIL` → your email (for Let's Encrypt)
- `SECRET_KEY_BASE`, `POSTGRES_PASSWORD`, `REDIS_PASSWORD` → the generated values
- SMTP settings → so Chatwoot can send agent invites & notifications (any provider)

## Step 5 — Launch

Prepare the database once, then bring everything up:

```bash
docker compose run --rm rails bundle exec rails db:chatwoot_prepare
docker compose up -d
```

Caddy will fetch a TLS certificate automatically. In ~1 minute, open
**https://support.yourdomain.com** and create your admin account.

> Watch it come up: `docker compose logs -f rails caddy`

## Step 6 — Connect the AI agent (auto-answer tickets)

The bot is already running; now let Chatwoot hand it conversations.

1. In Chatwoot, go to **Super Admin** or your profile → **Access Token** and copy it.
   Put it in `.env` as `CHATWOOT_API_TOKEN`. Confirm `CHATWOOT_ACCOUNT_ID` (usually `1`).
2. Create an **Agent Bot** pointing at the bot's webhook. Easiest via the Platform API:

   ```bash
   curl -X POST https://support.yourdomain.com/platform/api/v1/agent_bots \
     -H "api_access_token: <YOUR_PLATFORM_TOKEN>" \
     -H "Content-Type: application/json" \
     -d '{"name":"AI Support Agent","outgoing_url":"http://ai-support-agent:8000/webhooks/chatwoot"}'
   ```

   > `http://ai-support-agent:8000` is the bot's address **inside** the Docker network —
   > Chatwoot reaches it directly; it never needs to be public.
3. Restart the bot so it picks up the token:

   ```bash
   docker compose up -d ai-support-agent
   ```
4. In Chatwoot → **Inbox settings → Bot**, assign **AI Support Agent** to your inbox.

Now every incoming message is answered from your knowledge base. The bot only
replies to **incoming** messages, so it never talks to itself.

## Step 7 — Load your knowledge base

Replace the sample docs with your own help center / product docs:

```bash
# from the deploy/ folder
cp -r /path/to/your/docs/* knowledge/     # .md or .txt files
docker compose up -d --build ai-support-agent
```

Ask a question in the website widget and watch it answer with citations.

## Step 8 — Add channels

In Chatwoot → **Inboxes → Add Inbox**, connect the channels you need:

- **Website widget** — paste the snippet on your site (deflects the most tickets).
- **Email** — forward `support@yourdomain.com` into Chatwoot.
- **WhatsApp / Instagram / Messenger / Telegram** — follow the in-app wizards.

You're live. 🎉

---

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f rails sidekiq ai-support-agent` |
| Update Chatwoot | `docker compose pull && docker compose up -d` |
| Restart the bot | `docker compose up -d ai-support-agent` |
| Back up the database | `docker compose exec postgres pg_dump -U postgres chatwoot > backup.sql` |
| Stop everything | `docker compose down` (add `-v` to also wipe data) |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`.
- **502 / blank page** — Rails is still booting or the DB wasn't prepared. Re-run Step 5's prepare command and check `docker compose logs rails`.
- **Bot doesn't reply** — confirm the Agent Bot is assigned to the inbox, `CHATWOOT_API_TOKEN` is set, and you restarted `ai-support-agent`. Test directly: `docker compose exec ai-support-agent python -c "import chatwoot; print(chatwoot.enabled())"`.
- **Emails not sending** — fill in the `SMTP_*` values in `.env` and `docker compose up -d`.

## Swap a component

Prefer a different helpdesk or a lighter footprint? Every piece is replaceable —
see the [Customer Support directory](../README.md) for alternatives (Zammad,
FreeScout, Typebot, Botpress) and the [flagship app](../../../apps/ai-support-agent)
you can run standalone.
