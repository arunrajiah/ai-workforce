---
title: Go live — Legal & Compliance in one command
description: Deploy a private legal document stack (AnythingLLM contract Q&A) with HTTPS in under an hour.
sidebar_label: Legal — Go Live
slug: /departments/legal/deploy
keywords: [anythingllm self-host, contract review ai, private rag docker, one click deploy]
---

# ⚖️ Legal & Compliance — go live in one command

This stack **is** a lean legal department:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   your team ──────────▶ │  https://legal.yourdomain.com   (doc Q&A)          │
                         └──────────────────────┬─────────────────────────────┘
                                                ▼
                                          AnythingLLM
                                    (RAG over your contracts)
                                                │
                                    local Ollama (default) or any
                                    OpenAI-compatible endpoint
```

You get a private "chat with our contracts" assistant — behind real HTTPS on your
own domain, with confidential material never leaving your server.

- **Replaces:** outside-counsel document-review hours
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, and Docker

> ⚠️ **Not legal advice.** These tools assist review; a qualified lawyer must
> sign off on anything that matters.

---

## Step 1 — Get a server

Any Ubuntu 22.04+ VPS with **2 vCPU / 4 GB RAM** (minimum) works — Hetzner, DigitalOcean,
Vultr, AWS Lightsail, etc. SSH in, then install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

> Running LLM inference locally with Ollama (the default) is CPU/RAM hungry —
> bump to **8 GB+** (or a GPU box) if you want snappy answers on large models.

## Step 2 — Point your domain at it

Create a DNS **A record** → your server's IP:

- `legal.yourdomain.com` → the doc-Q&A app (AnythingLLM)

Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short legal.yourdomain.com   # should print your server IP
```

## Step 3 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/legal/deploy
cp .env.example .env
```

## Step 4 — Fill in `.env`

Generate the secret and edit the file:

```bash
echo "JWT_SECRET=$(openssl rand -hex 32)"
```

In `.env`, set at minimum:

- `DOMAIN` → `legal.yourdomain.com` (AnythingLLM)
- `ACME_EMAIL` → your email (for Let's Encrypt)
- `JWT_SECRET` → the generated value

**LLM choice (privacy-first).** The default is a **local Ollama**, so no document
text ever leaves your network:

```bash
# on the host (not in a container):
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1        # or any model you prefer
```

Prefer a hosted, OpenAI-compatible endpoint instead? In `.env` set
`LLM_PROVIDER=generic-openai` and fill in `LLM_BASE_URL`, `LLM_MODEL`, and
`LLM_API_KEY`. The stack is provider-neutral by design.

## Step 5 — Launch

Bring everything up:

```bash
docker compose up -d
```

Caddy will fetch a TLS certificate for your domain automatically. In ~1 minute:

- open **https://legal.yourdomain.com** and create your AnythingLLM admin account

> Watch it come up: `docker compose logs -f anythingllm caddy`

## Step 6 — Load your documents (AnythingLLM)

In AnythingLLM, create a **workspace** (e.g. "Contracts"), then upload your
contracts and policies (PDF, DOCX, TXT, MD). Ask a question and watch it answer
with citations, all from your private corpus.

> The default embeddings engine is fully local, so ingestion happens on your
> server too. Confirm the **LLM Preference** in Settings matches your `.env`
> (Ollama by default).

You're live. 🎉

---

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f anythingllm caddy` |
| Update everything | `docker compose pull && docker compose up -d` |
| Restart the Q&A app | `docker compose up -d anythingllm` |
| Back up AnythingLLM | `docker run --rm -v deploy_anythingllm_storage:/s -v "$PWD":/b alpine tar czf /b/anythingllm.tgz -C /s .` |
| Stop everything | `docker compose down` (add `-v` to also wipe data) |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`. The `legal.` record must resolve.
- **502 / blank page** — the app is still booting. Check `docker compose logs anythingllm`.
- **AnythingLLM can't reach Ollama** — the default `OLLAMA_BASE_PATH` is `http://host.docker.internal:11434`, which resolves to the host via the `extra_hosts` mapping. Confirm `ollama serve` is running on the host and the model is pulled.
- **Answers are slow or empty** — CPU-only inference on a large model is slow; try a smaller model, add RAM/GPU, or switch to an OpenAI-compatible endpoint (`LLM_PROVIDER=generic-openai`).

## Notes & caveats

- **Image/port/volume verification.** `mintplexlabs/anythingllm` serves on port **3001** and persists to volume **`/app/server/storage`** (`STORAGE_DIR=/app/server/storage`). Verified against the AnythingLLM Docker guide.
- **Not legal advice.** Repeated for emphasis: these tools assist review; a qualified lawyer must sign off on anything that matters.

## Swap a component

Prefer a heavier RAG engine or an on-prem-only stack? Every piece is replaceable —
see the [Legal & Compliance directory](../README.md) for alternatives (Onyx, PrivateGPT).
