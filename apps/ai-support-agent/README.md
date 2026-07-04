# 🎧 AI Support Agent (flagship)

A self-hosted RAG support agent that answers questions **from your own docs, with
citations** — the core of Tier-1 ticket deflection. Drop your knowledge base in
`knowledge/`, run one command, embed the widget.

- **Replaces:** a Tier-1 support agent + a "chat with our docs" SaaS add-on
- **Ship in:** ~5 minutes
- **Offline demo mode:** runs with **zero API keys** (lexical retrieval + extractive answers)
- **Stack:** Python / FastAPI, no database required

![mode badge](https://img.shields.io/badge/offline_demo-no_API_key_needed-00B894)

---

## Run it

### Option A — Docker (recommended)

```bash
cp .env.example .env        # offline demo needs no configuration
docker compose up
# open http://localhost:8000
```

### Option B — Python

```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn app:app --reload
# open http://localhost:8000
```

## Use your own knowledge base

Replace the files in [`knowledge/`](knowledge/) with your own `.md` or `.txt`
docs (help center exports, product docs, policies). Restart to re-index. That's it.

## Turn on synthesized answers

Offline mode returns the most relevant passages. For synthesized, conversational
answers, point at any OpenAI-compatible endpoint in `.env` (Ollama, LiteLLM,
LocalAI, vLLM, or a hosted gateway):

```bash
LLM_BASE_URL=http://localhost:11434/v1   # e.g. local Ollama
LLM_MODEL=llama3.1
LLM_API_KEY=                             # set for hosted gateways
```

## How it works

```
question ─▶ rag.py (BM25 lexical search over your docs) ─▶ top passages
                                                              │
                                          llm.py ◀────────────┘
                                     ┌────────┴─────────┐
                              LLM endpoint set?     (not set)
                                     │                  │
                              synthesized answer   extractive answer
                                     └────────┬─────────┘
                                        answer + citations ─▶ web UI
```

- [`rag.py`](rag.py) — dependency-free BM25 retrieval. Swap in a vector store (see the [Quickstart](../../docs/quickstart.mdx)) when you outgrow it.
- [`llm.py`](llm.py) — provider-neutral layer; calls your OpenAI-compatible endpoint, offline fallback otherwise.
- [`app.py`](app.py) — FastAPI: `POST /api/ask`, `GET /api/health`, serves the widget.

## Endpoints

| Method | Path | Body | Returns |
|---|---|---|---|
| `POST` | `/api/ask` | `{"question": "..."}` | `{answer, mode, sources[]}` |
| `GET` | `/api/health` | — | `{status, chunks_indexed, mode}` |

## Where to take it next

- Graduate to [Onyx](../../departments/support/) for multi-connector RAG (Slack, Confluence, 50+ sources) at scale ([Support department](../../departments/support/)).
- Add a vector store (Qdrant/pgvector) for large knowledge bases.
- Add a "confidence" threshold that escalates low-confidence questions to a human.

---

Part of **[AI Workforce](../../README.md)** · [Support department →](../../departments/support/)
