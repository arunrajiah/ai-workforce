# 📈 AI SDR (flagship)

Give it a company and a website; it **reads the site, extracts a real signal, and
drafts a personalized cold email + talking points**. The core loop of a sales
development rep — as a single small service.

- **Replaces:** the research-and-draft work of an SDR
- **Ship in:** ~5 minutes
- **Offline demo mode:** runs with **zero API keys** (real site-scrape + templated draft)
- **Stack:** Python / FastAPI (web UI + CLI), no database

![mode badge](https://img.shields.io/badge/offline_demo-no_API_key_needed-00B894)

---

## Run it

### Web UI (Docker)

```bash
cp .env.example .env        # offline demo needs no configuration
docker compose up
# open http://localhost:8000
```

### CLI

```bash
pip install -r requirements.txt
python app.py --company "Linear" --website linear.app --value "cutting support response time"
```

## Turn on fully written emails

Offline mode produces a real, personalized template from the site's actual meta
description. For a fully written, tailored email, point at any OpenAI-compatible
endpoint in `.env` (Ollama, LiteLLM, LocalAI, vLLM, or a hosted gateway):

```bash
LLM_BASE_URL=http://localhost:11434/v1   # e.g. local Ollama
LLM_MODEL=llama3.1
LLM_API_KEY=                             # set for hosted gateways
```

## How it works

- [`research.py`](research.py) — fetches the homepage and extracts `<title>` / meta description using only the standard library (no scraper dependency).
- [`llm.py`](llm.py) — turns the signal into an email; calls your OpenAI-compatible endpoint when configured, templated draft otherwise.
- [`app.py`](app.py) — FastAPI (`POST /api/draft`) + a web UI, and a CLI entry point.

## Endpoints

| Method | Path | Body | Returns |
|---|---|---|---|
| `POST` | `/api/draft` | `{company, website?, notes?, value_prop}` | `{draft, mode, research, signal}` |
| `GET` | `/api/health` | — | `{status, mode}` |

## Where to take it next

- Pull leads from [Veska](../veska/)'s CRM and loop this app over them.
- Pair it with [SalesGPT](../../departments/sales/) for the full conversation loop once a prospect replies.

---

Part of **[AI Workforce](../../README.md)** · [Sales department →](../../departments/sales/)
