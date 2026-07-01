---
title: Go live — an autonomous coding agent in one command
description: Deploy OpenHands (autonomous coding agent that turns issues into pull requests) with HTTPS in under an hour.
sidebar_label: Engineering — Go Live
slug: /departments/engineering/deploy
keywords: [openhands self-host, autonomous coding agent, devops docker, one click deploy]
---

# 🛠️ Engineering / DevOps — go live in one command

This stack **is** an autonomous engineer:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   your team ──────────▶ │  https://dev.yourdomain.com                        │
   (issues / prompts)                          │                               │
                         └───────────────────┼───────────────────────────────┘
                                             ▼
                                    OpenHands (web UI)
                                     │            ▲
                        run a task   │            │  drafted diff / PR
                                     ▼            │
                          Sandbox runtime container (per session)
                                     │
                            host Docker socket
```

You get a self-hosted control center for an autonomous coding agent: give it a
repo and a task, and it plans, edits, runs, and opens a pull request — behind
real HTTPS on your domain.

- **Replaces:** junior SWE / contract-dev hours for scoped tickets
- **Time to live:** ~30–60 minutes
- **You need:** a server with a public IP, a domain, and Docker

---

## Step 1 — Get a server

Any Ubuntu 22.04+ VPS with **2 vCPU / 4 GB RAM** (minimum; 4 vCPU / 8 GB is
comfortable, since the agent launches its own sandbox containers) works — Hetzner,
DigitalOcean, Vultr, AWS Lightsail, etc. SSH in, then install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

## Step 2 — Point your domain at it

Create a DNS **A record** for `dev.yourdomain.com` → your server's IP.
Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short dev.yourdomain.com   # should print your server IP
```

## Step 3 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/engineering/deploy
cp .env.example .env
```

## Step 4 — Fill in `.env`

Edit the file and set at minimum:

- `DOMAIN` → `dev.yourdomain.com`
- `ACME_EMAIL` → your email (for Let's Encrypt)
- `SANDBOX_RUNTIME_CONTAINER_IMAGE` → leave as-is unless you're pinning a different version

The LLM is **provider-neutral**. You can leave `LLM_*` blank and pick a model in
the OpenHands UI on first run, or set them now to any OpenAI-compatible endpoint:

- `LLM_BASE_URL` → e.g. a local Ollama (`http://host.docker.internal:11434/v1`), a
  LiteLLM/vLLM proxy, or a hosted OpenAI-compatible gateway
- `LLM_MODEL` → the model id your endpoint serves
- `LLM_API_KEY` → the key for that endpoint (generate any secrets you need with `openssl rand -hex 24`)

## Step 5 — Launch

Bring everything up:

```bash
docker compose up -d
```

On first start, Docker pulls the OpenHands app image; the **sandbox runtime image**
(`SANDBOX_RUNTIME_CONTAINER_IMAGE`) is pulled the first time you run a task.
Caddy will fetch a TLS certificate automatically. In ~1 minute, open
**https://dev.yourdomain.com**.

> Watch it come up: `docker compose logs -f openhands caddy`

## Step 6 — Configure the LLM & run your first task

1. Open **https://dev.yourdomain.com** and go to **Settings**.
2. If you didn't set `LLM_*` in `.env`, choose the **Advanced** LLM settings and
   enter your **Base URL**, **Model**, and **API key** for any OpenAI-compatible
   endpoint. Save.
3. Start a conversation, connect a repo, and give it a task ("fix this failing test",
   "add pagination to the users endpoint"). Watch it work in the sandbox and review
   the diff it produces.

You're live. 🎉

---

## ⚠️ Security: the Docker socket

OpenHands runs the agent's code inside a **sandbox container** that it launches on
demand, which is why this stack mounts the host Docker socket:

```yaml
- /var/run/docker.sock:/var/run/docker.sock
```

**This is effectively root on the host.** Anyone who can reach the OpenHands UI can
make it start containers with host-level Docker access. Treat this box as
security-sensitive:

- Put it on a **dedicated host** you don't share with production workloads.
- **Restrict access** to the UI — keep it off the public internet, or front it with
  authentication / an allowlist / a VPN. (Caddy makes it easy to add
  [basic auth](https://caddyserver.com/docs/caddyfile/directives/basicauth) or
  forward-auth in the `Caddyfile`.)
- Give the agent's LLM key and any repo tokens **least privilege**.

---

## Optional add-on — n8n for CI/PR automation

Want to trigger OpenHands from new issues, or post its PRs to Slack/Linear? Add
[n8n](https://github.com/n8n-io/n8n) as an automation layer. It's **not** part of
the core compose (keep the deploy lean), but it drops in easily — run it alongside
and reverse-proxy it under a subpath or subdomain:

```bash
docker run -d --restart unless-stopped \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

Wire a webhook (new GitHub issue → call OpenHands / notify your team). See the
[Engineering directory](../README.md) for the n8n listing.

---

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f openhands caddy` |
| Update OpenHands | `docker compose pull && docker compose up -d` |
| Restart | `docker compose restart openhands` |
| Stop everything | `docker compose down` (add `-v` to also wipe state) |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`.
- **502 / blank page** — OpenHands is still booting. Check `docker compose logs openhands`.
- **Agent can't run code / "cannot connect to Docker"** — the socket mount is missing or the runtime image failed to pull. Confirm `/var/run/docker.sock` is mounted and pull it manually: `docker pull $SANDBOX_RUNTIME_CONTAINER_IMAGE`.
- **LLM errors** — check the Base URL is reachable *from inside the container* (use `host.docker.internal` for services on the host), and that the model id and key are correct.

> **Verification note:** the run details above (app image `docker.all-hands.dev/all-hands-ai/openhands:0.55`, `SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.55-nikolaik`, the `/var/run/docker.sock` mount, and web port `3000`) were verified against the official OpenHands docs and README for the 0.55 release. OpenHands ships frequently — check the [docs](https://docs.openhands.dev) and bump the version tags together if you want a newer release. (A newer preview line rebrands the images under `docker.openhands.dev` and uses `AGENT_SERVER_IMAGE_*` env vars instead; this stack pins the established 0.55 release documented above.)

## Swap a component

Prefer a different coding agent or a lighter footprint? Every piece is replaceable —
see the [Engineering / DevOps directory](../README.md) for alternatives (Aider,
Coder, Appsmith, Budibase, n8n, Frappe Helpdesk).
