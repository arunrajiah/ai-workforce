---
title: Go live — a talk-to-your-data analyst in one command
description: Deploy the AI Analyst (plain-English questions over your data → SQL + results table) with HTTPS on your domain in under an hour.
sidebar_label: Data — Go Live
slug: /departments/data/deploy
keywords: [ai analyst, text-to-sql, talk to your data, bi docker, vanna, one click deploy]
---

# 📊 Data & Analytics — go live in one command

This stack **is** a talk-to-your-data analyst:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   your team ──────────▶ │  https://analytics.yourdomain.com                  │
   (plain-English questions)                  │                               │
                         └───────────────────┼───────────────────────────────┘
                                             ▼
                              AI Analyst (FastAPI, port 8000)
                                             │
                        question → SQL (single read-only SELECT) → results table
```

Ask a question in plain English and get an answer, the **SQL it ran**, and a
**results table** — the analyst-in-the-loop for routine "what's the number?"
requests, behind real HTTPS on your domain.

- **Replaces:** a BI analyst + ad-hoc "can you pull this number?" requests
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, Docker, and (optionally) an LLM

---

## Step 1 — Get a server

Any Ubuntu 22.04+ VPS with **1 vCPU / 2 GB RAM** works — the analyst is a small
FastAPI service. SSH in, then install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

## Step 2 — Point your domain at it

Create a DNS **A record** for `analytics.yourdomain.com` → your server's IP.
Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short analytics.yourdomain.com   # should print your server IP
```

## Step 3 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/data/deploy
cp .env.example .env
```

## Step 4 — Fill in `.env`

In `.env`, set at minimum:

- `DOMAIN` → `analytics.yourdomain.com`
- `ACME_EMAIL` → your email (for Let's Encrypt)

Leave the `LLM_*` values blank to launch in **offline demo mode** (built-in
example questions run end-to-end with zero API keys). To turn *any* question into
SQL, point at any OpenAI-compatible endpoint — a **local Ollama** for a fully
private setup, or a self-hosted gateway (LiteLLM, vLLM, LocalAI):

```bash
LLM_BASE_URL=http://localhost:11434/v1   # e.g. local Ollama
LLM_MODEL=llama3.1
LLM_API_KEY=                             # set for hosted gateways
```

## Step 5 — Launch

Bring everything up (this builds the AI Analyst image from
[`apps/ai-analyst`](../../../apps/ai-analyst)):

```bash
docker compose up -d
```

Caddy will fetch a TLS certificate automatically. In ~1 minute, open
**https://analytics.yourdomain.com** and start asking questions.

> Watch it come up: `docker compose logs -f ai-analyst caddy`

## Step 6 — Use your own data

Out of the box the analyst answers questions over a bundled sample CSV. To use
your own, drop a CSV into a `data/` folder next to `docker-compose.yml` and
rebuild — the compose file mounts `./data` into the container:

```bash
mkdir -p data
cp /path/to/your.csv data/sales.csv
docker compose up -d --build ai-analyst
```

Column types are inferred automatically. Queries are **read-only** — only a
single `SELECT` is ever executed.

You're live. 🎉

---

## Scale up: from one CSV to your whole warehouse

The AI Analyst is deliberately lean — one CSV, in-memory SQLite, read-only. When
you're ready to point text-to-SQL at your **actual data warehouse** (Postgres,
MySQL, BigQuery, Snowflake, and more), graduate to
[**Vanna**](https://github.com/vanna-ai/vanna): train it on your schema and it
answers ad-hoc questions in SQL across your real tables.
[Wren AI](https://github.com/Canner/WrenAI) is the maintained alternative with a
semantic layer. See the [Data & Analytics directory](../README.md).

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f ai-analyst caddy` |
| Rebuild the analyst (new CSV or code) | `docker compose up -d --build ai-analyst` |
| Restart the analyst | `docker compose up -d ai-analyst` |
| Stop everything | `docker compose down` |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`.
- **502 / blank page** — the analyst is still building or booting. Check `docker compose logs ai-analyst`.
- **Analyst answers only example questions** — that's offline demo mode. Set `LLM_BASE_URL`/`LLM_MODEL`/`LLM_API_KEY` in `.env` and `docker compose up -d ai-analyst`.

## Swap a component

Prefer a different text-to-SQL engine? Every piece is replaceable — see the
[Data & Analytics directory](../README.md) for alternatives (Vanna, Wren AI,
or DB-GPT for a fuller agentic data assistant) and the
[flagship app](../../../apps/ai-analyst) you can run standalone.
