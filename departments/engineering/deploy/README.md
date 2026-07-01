# 🛠️ Engineering / DevOps — one-click deploy

An autonomous coding agent in one command: **OpenHands** (turns issues into pull
requests) + **Caddy** for automatic HTTPS.

```bash
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and (optionally) your LLM endpoint
docker compose up -d
```

👉 **Full walkthrough (domain, DNS, first login, connecting an LLM, running your
first task): [GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | junior SWE / contract-dev hours for scoped tickets |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (2 vCPU / 4 GB), a domain, Docker |
| **Includes** | OpenHands, Caddy (HTTPS) |

> ⚠️ OpenHands runs the agent's code in sandbox containers and mounts the host
> Docker socket — effectively root on the host. Keep this box dedicated and
> access-restricted. See the security note in [GO-LIVE.md](GO-LIVE.md).

Want alternatives to any piece? See the [Engineering directory](../README.md).
