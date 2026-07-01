# 📊 Data & Analytics — one-click deploy

A talk-to-your-data analyst in one command: our flagship **[AI Analyst](../../../apps/ai-analyst)**
(ask plain-English questions over a CSV → the SQL it ran plus a results table) +
**Caddy** for automatic HTTPS.

```bash
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and (optionally) your LLM endpoint
docker compose up -d
```

👉 **Full walkthrough (server, DNS, HTTPS, connecting your data, scaling to a
warehouse with Vanna): [GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | a BI analyst + ad-hoc SQL requests |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (1 vCPU / 2 GB), a domain, Docker |
| **Includes** | AI Analyst, Caddy (HTTPS) |

Runs in **offline demo mode** with zero API keys; set `LLM_*` to turn any question
into SQL against any OpenAI-compatible endpoint. When you outgrow a single CSV,
graduate to [Vanna](https://github.com/vanna-ai/vanna) — see the
[Data & Analytics directory](../README.md).
