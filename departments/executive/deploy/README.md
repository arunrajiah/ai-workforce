# 🧠 Executive / Assistant — one-click deploy

The whole executive-assistant department in one command: **Khoj** (a personal AI
"second brain" — chat + semantic search over your own docs) + **Caddy** for
automatic HTTPS, and it runs on a local/private LLM.

```bash
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and the generated secrets
docker compose up -d
```

👉 **Full walkthrough (domain, DNS, first login, pointing Khoj at a local LLM,
indexing your docs): [GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | an executive assistant + a "chat with my notes" tool + scattered search |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (2 vCPU / 4 GB), a domain, Docker |
| **Includes** | Khoj (server), Caddy (HTTPS), Postgres/pgvector, SearXNG, Terrarium |

Want alternatives to any piece? See the [Executive / Assistant directory](../README.md).
