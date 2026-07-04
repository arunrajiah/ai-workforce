---
title: Go live — the AI-native back office (Veska)
description: Deploy Veska — one AI platform for CRM, support, finance, HR & ops — on your domain with HTTPS.
sidebar_label: Veska — Go Live
slug: /apps/veska/deploy
keywords: [veska, ai erp, self-host, ai back office, one click deploy]
---

# Veska — go live in under an hour

One AI-native platform for your whole back office:

```
                     ┌──────────── Caddy (auto-HTTPS) ────────────┐
   your team ──────▶ │  https://app.yourdomain.com  (admin UI)    │
   customers  ──────▶ │  https://api.yourdomain.com  (API + chat)  │
   (Slack/WhatsApp/Email)          │                              │
                     └─────────────┼──────────────────────────────┘
                                   ▼
                     Veska: CRM · Support · Finance · HR · Ops
                       (AI action agent · workflow engine)
                                   │
                        Postgres/pgvector · Redis
```

- **Replaces:** a CRM + helpdesk + accounting + HRIS + ops tooling — all at once
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, Docker, and an LLM (local Ollama works)

> This guide layers HTTPS + your domain on top of Veska's own deploy. The
> authoritative app docs are Veska's [`SELF_HOSTING.md`](https://github.com/arunrajiah/veska/blob/main/SELF_HOSTING.md).

---

## Step 1 — Get a server

An Ubuntu 22.04+ VPS with **2 vCPU / 4 GB RAM** (more if you run a local LLM). Install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443**.

## Step 2 — Point your domain at it

Create two DNS **A records** at your server's IP:

- `app.yourdomain.com` — the admin UI
- `api.yourdomain.com` — the API (and channel webhooks)

```bash
dig +short app.yourdomain.com   # should print your server IP
```

## Step 3 — Deploy Veska

```bash
git clone https://github.com/arunrajiah/veska.git
cd veska
cp .env.example .env
```

Edit `veska/.env` and set at minimum (see Veska's [`.env.example`](https://github.com/arunrajiah/veska/blob/main/.env.example) for the full list):

- Your **LLM provider** — a hosted key, or a **local Ollama** endpoint for a fully private setup.
- `MAGIC_LINK_SECRET` — a 32+ char random string: `openssl rand -hex 32`
- `MAGIC_LINK_BASE_URL` — `https://app.yourdomain.com`

Bring it up and run migrations:

```bash
docker compose up -d
docker compose exec api node apps/api/dist/db/migrate.js
```

## Step 4 — Add HTTPS with the Caddy overlay

From **this** folder (`apps/veska` in the ai-workforce repo):

```bash
cp .env.example .env      # set DOMAIN=app.yourdomain.com and ACME_EMAIL
docker compose --env-file .env -f caddy-compose.yml up -d
```

Caddy attaches to Veska's Docker network and fetches TLS certs automatically for
`app.` and `api.` In ~1 minute, open **https://app.yourdomain.com**.

> **Heads-up (API URL):** Veska's admin UI reads its API URL from
> `NEXT_PUBLIC_API_URL`, which is set at build time (default `http://localhost:3001`).
> For a public HTTPS deployment, set it to `https://api.yourdomain.com` per Veska's
> self-hosting docs and rebuild the `admin` image, so the browser calls the API
> over HTTPS. If your Veska project folder isn't named `veska`, update the network
> name in [`caddy-compose.yml`](caddy-compose.yml) to `<folder>_default`.

## Step 5 — Onboard your company

Open the admin UI and complete onboarding — **describe your business in plain
English** and Veska configures CRM, support, finance, and HR for you. Explore the
seeded demo data first if you like (`pnpm seed` in dev, per Veska's README).

## Step 6 — Connect your channels

This is where Veska shines — your team works from chat, not dashboards. In Veska's
settings, connect:

- **Slack** — create a Slack app, enable the Events API, add the bot token/signing secret to `veska/.env` (see Veska's "Connecting Slack" section).
- **Email** — forward a support/ops address into Veska.
- **WhatsApp / Telegram** — follow the in-app channel wizards.

You're live. 🎉

---

## Operate it

| Task | Command (run in the `veska` repo) |
|---|---|
| Logs | `docker compose logs -f api admin` |
| Update | `git pull && docker compose pull && docker compose up -d && docker compose exec api node apps/api/dist/db/migrate.js` |
| Back up the database | `docker compose exec postgres pg_dump -U veska veska > veska-backup.sql` |
| Restart HTTPS overlay | `docker compose -f caddy-compose.yml up -d` (in `apps/veska`) |

## Troubleshooting

- **No certificate** — DNS for `app.`/`api.` isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose -f caddy-compose.yml logs caddy`.
- **Caddy can't reach `admin`/`api`** — the external network name must match Veska's Compose project (`<folder>_default`). Confirm with `docker network ls`.
- **UI loads but API calls fail** — set `NEXT_PUBLIC_API_URL=https://api.yourdomain.com` and rebuild the admin image (see the Step 4 heads-up).
- **App-level issues** — see Veska's [`SELF_HOSTING.md`](https://github.com/arunrajiah/veska/blob/main/SELF_HOSTING.md) and [Discussions](https://github.com/arunrajiah/veska/discussions).

---

Part of **[AI Workforce](../../README.md)** · Covers [Sales](../../departments/sales/) · [Support](../../departments/support/) · [Finance](../../departments/finance/) · [HR](../../departments/hr/) · [Operations](../../departments/operations/)
