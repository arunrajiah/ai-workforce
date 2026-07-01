# 📊 AI Analyst (flagship)

Drop in a CSV and **ask it questions in plain English** — get an answer, the SQL
it ran, and a results table. A talk-to-your-data BI analyst as one small service.

- **Replaces:** ad-hoc "can you pull this number?" requests to a data analyst
- **Ship in:** ~5 minutes
- **Offline demo mode:** built-in example questions run end-to-end with **zero API keys**
- **Stack:** Python / FastAPI + SQLite (read-only), no external DB

![mode badge](https://img.shields.io/badge/offline_demo-no_API_key_needed-0984E3)

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
python app.py "revenue by region"
python app.py "who is the top rep"
```

## Use your own data

Replace [`data/sales.csv`](data/sales.csv) with any CSV (or set `CSV_PATH`). The
column types are inferred automatically. With an API key, you can ask anything;
offline, the built-in example questions still work against your columns if named
similarly.

## Turn on full natural-language querying

Point at any OpenAI-compatible endpoint in `.env` (Ollama, LiteLLM, LocalAI,
vLLM, or a hosted gateway):

```bash
LLM_BASE_URL=http://localhost:11434/v1   # e.g. local Ollama
LLM_MODEL=llama3.1
LLM_API_KEY=                             # set for hosted gateways
```

Now any question becomes SQL. Queries are **read-only** — only a single `SELECT`
is ever executed (see [`db.py`](db.py)).

## How it works

- [`db.py`](db.py) — loads the CSV into in-memory SQLite; `run_sql()` allows only single read-only `SELECT`s.
- [`llm.py`](llm.py) — turns a question into SQL via your OpenAI-compatible endpoint, with offline example-question fallback and a no-API answer narrator.
- [`app.py`](app.py) — FastAPI (`POST /api/ask`) + web UI + CLI.

## Safety

Only a single `SELECT` statement runs; multiple statements, writes, and DDL are
rejected. Still, point this at a read-only replica or a copy for anything sensitive.

## Where to take it next

- Swap SQLite for your warehouse connection and graduate to [Metabase](../../departments/data/) or [Wren AI](../../departments/data/) for a full BI layer.
- Schedule a daily "state of the business" summary via [n8n](../../departments/operations/).

---

Part of **[AI Workforce](../../README.md)** · [Data department →](../../departments/data/)
