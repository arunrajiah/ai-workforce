# 📣 Marketing & Growth — one-click deploy

An AI content & agent platform behind HTTPS: **[Dify](https://github.com/langgenius/dify)**
(open-source LLM app/agent platform — build ad-copy, blog, and SEO agents with RAG)
fronted by **Caddy** for automatic HTTPS.

This is a thin **deploy wrapper** — it does not fork or re-implement Dify's
multi-service stack. Dify runs from its own Compose; this folder adds an HTTPS
overlay on top.

```bash
# 1) Start Dify (its official quick-start)
git clone https://github.com/langgenius/dify.git
cd dify/docker && cp .env.example .env
# set EXPOSE_NGINX_PORT=8080 in .env so Dify frees host port 80 for Caddy
docker compose up -d

# 2) Add HTTPS on your domain (from this folder)
cp .env.example .env      # set DOMAIN and ACME_EMAIL
docker compose --env-file .env -f caddy-compose.yml up -d
```

👉 **Full walkthrough (server, DNS, HTTPS overlay, LLM provider, first agent):
[GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | a content marketer + Jasper/Copy.ai |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (2 vCPU / 4 GB; 8 GB comfortable), a domain, Docker, an LLM |
| **Includes** | Caddy (HTTPS) overlay for Dify's own stack |

## What's in this folder

- [`Caddyfile`](Caddyfile) — automatic HTTPS; reverse-proxies your domain → Dify's `nginx` entrypoint.
- [`caddy-compose.yml`](caddy-compose.yml) — a Caddy container that joins Dify's Docker network.
- [`.env.example`](.env.example) — the domain/email for the overlay.
- [`GO-LIVE.md`](GO-LIVE.md) — the full walkthrough.

Want alternatives to any piece? See the [Marketing directory](../README.md).
