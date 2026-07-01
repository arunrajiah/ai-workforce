---
title: Go live — Executive / Assistant in one command
description: Deploy a personal AI second brain (Khoj — chat + semantic search over your docs) with HTTPS in under an hour.
sidebar_label: Executive — Go Live
slug: /departments/executive/deploy
keywords: [khoj self-host, personal ai assistant, second brain docker, semantic search, one click deploy]
---

# 🧠 Executive / Assistant — go live in one command

This stack **is** an executive assistant:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   you ────────────────▶ │  https://assistant.yourdomain.com                  │
   (chat / search)                            │                               │
                         └───────────────────┼───────────────────────────────┘
                                             ▼
                                     Khoj (second brain)
                                     │            ▲
                        your docs    │            │  answers + citations
                                     ▼            │
                             semantic search over your knowledge
                                     │
                    Postgres/pgvector · SearXNG · Terrarium
```

You get a personal AI assistant that **chats with and semantically searches your
own documents** — notes, PDFs, org files, Markdown — behind real HTTPS on your
domain, and it can run entirely on a local/private LLM.

- **Replaces:** an executive assistant + a "chat with my notes" tool + scattered search
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

Create a DNS **A record** for `assistant.yourdomain.com` → your server's IP.
Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short assistant.yourdomain.com   # should print your server IP
```

## Step 3 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/executive/deploy
cp .env.example .env
```

## Step 4 — Fill in `.env`

Generate the secrets and edit the file:

```bash
echo "KHOJ_DJANGO_SECRET_KEY=$(openssl rand -hex 32)"
echo "POSTGRES_PASSWORD=$(openssl rand -hex 24)"
echo "KHOJ_ADMIN_PASSWORD=$(openssl rand -hex 24)"
```

In `.env`, set at minimum:

- `DOMAIN` → `assistant.yourdomain.com`
- `ACME_EMAIL` → your email (for Let's Encrypt)
- `KHOJ_DJANGO_SECRET_KEY`, `POSTGRES_PASSWORD`, `KHOJ_ADMIN_PASSWORD` → the generated values
- `KHOJ_ADMIN_EMAIL` → the email you'll use to log into Khoj's admin panel

## Step 5 — Launch

Bring everything up:

```bash
docker compose up -d
```

Caddy will fetch a TLS certificate automatically. In ~1 minute, open
**https://assistant.yourdomain.com** and sign in.

> Watch it come up: `docker compose logs -f server caddy`

## Step 6 — Point Khoj at a local/private LLM

Khoj configures its chat model in the **admin panel** — this is where you keep it
provider-neutral and offline.

1. Open **https://assistant.yourdomain.com/server/admin** and log in with
   `KHOJ_ADMIN_EMAIL` / `KHOJ_ADMIN_PASSWORD` from your `.env`.
2. Add an **AI Model API**. Set its **api url** to any OpenAI-compatible endpoint.
   For a local/private model, run Ollama on the host and use
   `http://host.docker.internal:11434/v1/`.
3. Add a **Chat Model** entry, choose type **OpenAI**, and set the model name
   (e.g. `llama3.1`) to match what your endpoint serves.

Prefer to wire it up front instead of in the UI? Set `LLM_BASE_URL` and
`LLM_API_KEY` in `.env` (they map to Khoj's `OPENAI_BASE_URL` / `OPENAI_API_KEY`)
and `docker compose up -d`. For local Ollama, any non-empty `LLM_API_KEY` works.

> **Keep it private:** pointing the base URL at a local Ollama means your documents
> and prompts never leave the server. No external API key required.

## Step 7 — Add your documents

Give your assistant a knowledge base to search and chat over:

- **Web/desktop:** in Khoj, open **Settings** and connect your files — upload
  Markdown, PDF, `.org`, and plain-text docs, or sync a folder.
- Khoj indexes them into semantic search automatically; ask a question and it
  answers **with citations** back to the source.

## Step 8 — Use it every day

Chat with your knowledge, run semantic searches, and let Khoj draft and recall
across everything you've indexed:

- **Search** — find anything across your notes and docs by meaning, not keywords.
- **Chat** — ask questions and get answers grounded in your own material.
- **Clients** — install the Khoj Obsidian/Emacs/desktop clients and point them at
  `https://assistant.yourdomain.com`.

You're live. 🎉

---

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f server caddy` |
| Update Khoj | `docker compose pull && docker compose up -d` |
| Restart the server | `docker compose up -d server` |
| Back up the database | `docker compose exec database pg_dump -U postgres khoj > backup.sql` |
| Stop everything | `docker compose down` (add `-v` to also wipe data) |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`.
- **502 / blank page** — the server is still booting (first run downloads embedding models). Give it a minute and check `docker compose logs server`.
- **No answers / model errors** — confirm you added an AI Model API and Chat Model in the admin panel (Step 6), and that your LLM endpoint is reachable from the container. For a host Ollama, use `http://host.docker.internal:11434/v1/`.
- **Docs not searchable** — re-open Khoj Settings and re-sync the files; watch `docker compose logs -f server` while indexing.

## Swap a component

Prefer a different assistant or a lighter footprint? Every piece is replaceable —
see the [Executive / Assistant directory](../README.md) for alternatives you can
run instead.

---

> **Verification note:** service names, images, the `42110` web port, and the
> `POSTGRES_*` / `KHOJ_*` / `KHOJ_TERRARIUM_URL` / `KHOJ_SEARXNG_URL` env vars are
> taken from Khoj's official `docker-compose.yml`. Khoj configures the chat model
> primarily through its admin UI (`/server/admin`); the `OPENAI_BASE_URL` /
> `OPENAI_API_KEY` env vars are Khoj's documented way to preset an OpenAI-compatible
> (or local Ollama) endpoint. `LLM_MODEL` is provided for your convenience but is
> set on the Chat Model entry in the admin UI. This compose omits Khoj's optional
> `--anonymous-mode` flag so the admin login is enforced; add it back if you want
> an open, single-user instance.
