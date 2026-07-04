---
title: Go live — an AI content & agent platform in one command
description: Deploy Dify (open-source LLM app/agent platform) for marketing content, SEO, and campaign agents, with HTTPS on your domain in under an hour.
sidebar_label: Marketing — Go Live
slug: /departments/marketing/deploy
keywords: [dify self-host, llm app platform, ai content agent, marketing automation docker, one click deploy]
---

# 📣 Marketing & Growth — go live in one command

This stack gives your marketing team an **AI app/agent platform**: build ad-copy,
blog, and SEO agents with RAG, prompts, and knowledge — then put them behind real
HTTPS on your domain.

```
                     ┌──────────── Caddy (auto-HTTPS) ────────────┐
   your team ──────▶ │  https://marketing.yourdomain.com          │
   (content · SEO · agents)              │                        │
                     └─────────────┬──────────────────────────────┘
                                   ▼
                          Dify (nginx entrypoint)
                                   │
                     web · api · worker · plugin daemon
                                   │
                        Postgres · Redis · vector DB
```

- **Replaces:** a content marketer + Jasper/Copy.ai (and the glue to run agents)
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, Docker, and an LLM (a local
  Ollama endpoint works for a fully private setup)

> This guide layers HTTPS + your domain on top of Dify's own deploy. The
> authoritative app docs are Dify's
> [official docker deployment](https://github.com/langgenius/dify/tree/main/docker).

---

## Step 1 — Get a server

An Ubuntu 22.04+ VPS with **2 vCPU / 4 GB RAM** (more if you run a local LLM).
Dify's full stack is heavier than a single container, so **8 GB RAM** is
comfortable. Install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

## Step 2 — Point your domain at it

Create a DNS **A record** for `marketing.yourdomain.com` → your server's IP.
Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short marketing.yourdomain.com   # should print your server IP
```

## Step 3 — Deploy Dify

Dify ships its own multi-service Docker Compose. Start it from the `docker/`
folder (this is Dify's documented quick-start):

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
```

Before launching, edit `dify/docker/.env` and change the exposed web port so Dify
does **not** grab host port 80 (Caddy needs it):

```bash
# in dify/docker/.env
EXPOSE_NGINX_PORT=8080
```

Then bring Dify up:

```bash
docker compose up -d
```

Dify's `nginx` service fronts the web UI and API. It's now reachable on the host
at `http://<server-ip>:8080` — we'll put HTTPS in front of it next.

## Step 4 — Add HTTPS with the Caddy overlay

From **this** folder (`departments/marketing/deploy` in the ai-workforce repo):

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/marketing/deploy
cp .env.example .env      # set DOMAIN=marketing.yourdomain.com and ACME_EMAIL
docker compose --env-file .env -f caddy-compose.yml up -d
```

Caddy attaches to Dify's Docker network and reverse-proxies your domain to Dify's
`nginx` service, fetching a TLS certificate automatically. In ~1 minute, open
**https://marketing.yourdomain.com/install** to complete Dify's first-run setup.

> **Network-name caveat (read this):** the overlay joins an **external** Docker
> network named `docker_default`. That name comes from Dify's Compose *project
> directory* being `docker/` — Compose names the default network
> `<dir>_default`. If you cloned or started Dify from a differently named folder,
> the network won't be `docker_default`; find the real name with
> `docker network ls` and update it in
> [`caddy-compose.yml`](caddy-compose.yml). If joining the network is awkward in
> your setup, an alternative is to drop the `networks:` block and instead
> `reverse_proxy host.docker.internal:8080` in the [`Caddyfile`](Caddyfile),
> pointing at the host port Dify published in Step 3.

## Step 5 — Set your LLM provider

In Dify → **Settings → Model Provider**, add your LLM. Dify is provider-neutral:
point it at any OpenAI-compatible endpoint — a **local Ollama** for a fully
private setup, a self-hosted gateway (LiteLLM, vLLM, LocalAI), or a hosted key.

## Step 6 — Build your first content agent

In Dify, create an app (chatflow, workflow, or agent) for your use case:

- **Ad copy / blog drafts** — a prompt app with your brand voice as the system prompt.
- **SEO research** — a workflow that summarizes competitor pages and drafts optimized copy.
- **Campaign ops** — expose the app's API and trigger it from
  [Activepieces](https://github.com/activepieces/activepieces) or your own scripts.

You're live. 🎉

---

## Operate it

| Task | Command |
|---|---|
| Dify logs | `docker compose logs -f` (run in `dify/docker`) |
| Update Dify | `git pull && docker compose pull && docker compose up -d` (in `dify/docker`) |
| Back up the database | `docker compose exec db pg_dump -U postgres dify > dify-backup.sql` (in `dify/docker`) |
| Restart HTTPS overlay | `docker compose -f caddy-compose.yml up -d` (in this folder) |
| Stop the overlay | `docker compose -f caddy-compose.yml down` (in this folder) |

## Troubleshooting

- **No certificate** — DNS for `marketing.` isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose -f caddy-compose.yml logs caddy`.
- **Caddy can't reach `nginx`** — the external network name must match Dify's Compose project (`docker_default` when started from `dify/docker`). Confirm with `docker network ls` and update [`caddy-compose.yml`](caddy-compose.yml).
- **Port 80 already in use** — Dify is still binding it. Set `EXPOSE_NGINX_PORT=8080` in `dify/docker/.env` and `docker compose up -d` again (in `dify/docker`).
- **App-level issues** — see Dify's [docker deployment docs](https://github.com/langgenius/dify/tree/main/docker).

## Swap a component

Prefer a different platform or a lighter footprint? Every piece is replaceable —
see the [Marketing & Growth directory](../README.md) for alternatives (Activepieces).

---

> ⚠️ **Verification note:** Dify's quick-start (`git clone`, `cd dify/docker`,
> `cp .env.example .env`, `docker compose up -d`, then `/install`), its `nginx`
> reverse-proxy entrypoint, the `EXPOSE_NGINX_PORT` host-port variable (default
> 80), and the `docker_default` network name (project dir `docker/`) are taken
> from Dify's official
> [docker-compose.yaml](https://github.com/langgenius/dify/blob/main/docker/docker-compose.yaml)
> and [README](https://github.com/langgenius/dify). Dify is licensed under the
> Dify Open Source License (Apache-2.0-based with additional conditions).
