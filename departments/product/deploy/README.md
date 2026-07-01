# 🔬 Product & Research — one-click deploy

The core of a product-research department in one command: **GPT Researcher**
(autonomous cited research briefs) + **Caddy** for automatic HTTPS.

```bash
cp .env.example .env      # set DOMAIN, ACME_EMAIL, TAVILY_API_KEY, LLM_*
docker compose up -d
```

👉 **Full walkthrough (domain, DNS, API keys, first research run):
[GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | a junior market researcher + a "Deep Research" subscription |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (2 vCPU / 4 GB), a domain, Docker, a search-provider key, an OpenAI-compatible LLM |
| **Includes** | GPT Researcher, Caddy (HTTPS) |

The LLM is provider-neutral: point `LLM_BASE_URL`/`LLM_API_KEY` at any
OpenAI-compatible endpoint (self-hosted, Ollama, a gateway).

Want alternatives to any piece? See the [Product & Research directory](../README.md).
