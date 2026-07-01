"""AI Analyst — ask your data questions in English, get SQL + an answer + a table.

Runs fully offline with built-in example questions. Configure an OpenAI-compatible
LLM endpoint for full natural-language querying over any CSV you drop in `data/`.

    pip install -r requirements.txt
    uvicorn app:app --reload            # web UI at http://localhost:8000
    # or CLI:
    python app.py "revenue by region"
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from db import DataStore
from llm import llm_enabled, narrate, to_sql

CSV_PATH = os.getenv("CSV_PATH", str(Path(__file__).parent / "data" / "sales.csv"))

app = FastAPI(title="AI Analyst", version="1.0.0")
store = DataStore(CSV_PATH)


class Question(BaseModel):
    question: str


def _answer(question: str) -> dict:
    plan = to_sql(question, store.schema())
    if not plan["sql"]:
        return {"mode": plan["mode"], "note": plan["note"], "answer": None, "summary": store.summary(), "sql": None}
    try:
        result = store.run_sql(plan["sql"])
    except Exception as exc:
        return {"mode": plan["mode"], "note": f"Query error: {exc}", "answer": None, "sql": plan["sql"]}
    return {
        "mode": plan["mode"],
        "sql": result["sql"],
        "columns": result["columns"],
        "rows": result["rows"],
        "answer": narrate(question, result),
        "note": plan.get("note", ""),
    }


@app.get("/", response_class=HTMLResponse)
def index():
    return (Path(__file__).parent / "static" / "index.html").read_text()


@app.get("/api/health")
def health():
    return {"status": "ok", "mode": "llm" if llm_enabled() else "offline", "schema": store.schema()}


@app.post("/api/ask")
def ask(body: Question):
    return _answer(body.question)


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "revenue by region"
    res = _answer(q)
    print(f"\n[mode: {res['mode']}]  SQL: {res.get('sql')}\n")
    if res.get("answer"):
        print("Answer:", res["answer"])
        for row in res.get("rows", [])[:20]:
            print("  ", row)
    else:
        print(res.get("note"))
        print("Summary:", res.get("summary"))
