---
title: Go live — Product & Research in one command
description: Deploy a product-research agent (GPT Researcher) with HTTPS in under an hour.
sidebar_label: Product & Research — Go Live
slug: /departments/product/deploy
keywords: [gpt researcher self-host, research agent docker, one click deploy]
---

# 🔬 Product & Research — go live in one command

This stack **is** a product-research department:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   your team ──────────▶ │  https://research.yourdomain.com   (GPT Researcher)│
                         └───────────────────────┬────────────────────────────┘
                                                 ▼
                                         GPT Researcher
                                         (cited briefs)
                                                 │
                                         web search + LLM
```

You get an autonomous research agent that turns a question into a sourced brief —
behind real HTTPS on your domain.

- **Replaces:** a junior market/desk researcher + a "Deep Research" subscription
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, Docker, a search-provider key, and an OpenAI-compatible LLM endpoint

---

## Step 1 — Get a server

Any Ubuntu 22.04+ VPS with **2 vCPU / 4 GB RAM** (minimum) works — Hetzner, DigitalOcean,
Vultr, AWS Lightsail, etc. SSH in, then install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

## Step 2 — Point your domain at it

Create a DNS **A record** pointing at your server's IP:

- `research.yourdomain.com` → GPT Researcher

Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short research.yourdomain.com   # should print your server IP
```

## Step 3 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/product/deploy
cp .env.example .env
```

## Step 4 — Fill in `.env`

In `.env`, set at minimum:

- `DOMAIN` → `research.yourdomain.com` and `ACME_EMAIL` → your email (for Let's Encrypt)
- `TAVILY_API_KEY` → a search-provider key from [tavily.com](https://tavily.com) (GPT Researcher's default retriever)
- `LLM_BASE_URL` and `LLM_API_KEY` → your OpenAI-compatible endpoint and key (see below)

### Pointing at your LLM (provider-neutral)

GPT Researcher speaks the OpenAI API, so **any OpenAI-compatible server works** — a
self-hosted model server, Ollama, or an OpenAI-compatible gateway. Set:

- `LLM_BASE_URL` → the endpoint's base URL (usually ends in `/v1`)
- `LLM_API_KEY` → the key that endpoint expects (some local servers accept any value)
- `FAST_LLM` / `SMART_LLM` / `STRATEGIC_LLM` / `EMBEDDING` → models in `provider:model`
  form. Keep the `openai:` prefix for any OpenAI-compatible server (e.g.
  `openai:gpt-4o-mini`), or use `ollama:<model>` when running against Ollama.

## Step 5 — Launch

```bash
docker compose up -d
```

Caddy will fetch a TLS certificate automatically. In ~1 minute, open
**https://research.yourdomain.com** and ask your first research question.

> Watch it come up: `docker compose logs -f gpt-researcher caddy`

## Step 6 — Run a research brief

In GPT Researcher, enter a question (e.g. *"competitive landscape for open-source
survey tools in 2026"*), pick the report type, and it will search the web, read
sources, and return a **cited report** you can export.

You're live. 🎉

---

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f gpt-researcher caddy` |
| Update everything | `docker compose pull && docker compose up -d` |
| Restart the researcher | `docker compose up -d gpt-researcher` |
| Stop everything | `docker compose down` |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`. The `research.` record must resolve.
- **Research runs fail / no answer** — check `TAVILY_API_KEY` is set and that `LLM_BASE_URL`/`LLM_API_KEY` point at a reachable OpenAI-compatible endpoint. Inspect `docker compose logs gpt-researcher`.

## Swap a component

Prefer a different research agent or an internal-knowledge base? Every piece is
replaceable — see the [Product & Research directory](../README.md) for
alternatives (Open Deep Research, deep-research, Onyx).
