"""Natural-language-to-SQL layer (provider-neutral).

Generates SQL from a question via any OpenAI-compatible chat endpoint (Ollama,
LiteLLM, LocalAI, vLLM, or a hosted gateway), configured with LLM_BASE_URL /
LLM_MODEL / LLM_API_KEY. Offline, a small set of built-in example questions still
work end-to-end, and any other question returns a data summary — so the app is
useful with zero setup.
"""
from __future__ import annotations

import json
import os
import re
import textwrap
import urllib.request

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")

# Built-in questions that work offline, mapped to SQL over the sample dataset.
EXAMPLES = {
    "total revenue": "SELECT ROUND(SUM(revenue),2) AS total_revenue FROM data",
    "revenue by region": "SELECT region, ROUND(SUM(revenue),2) AS revenue FROM data GROUP BY region ORDER BY revenue DESC",
    "top rep": "SELECT rep, ROUND(SUM(revenue),2) AS revenue FROM data GROUP BY rep ORDER BY revenue DESC LIMIT 1",
    "best selling product": "SELECT product, SUM(units) AS units FROM data GROUP BY product ORDER BY units DESC LIMIT 1",
    "revenue by product": "SELECT product, ROUND(SUM(revenue),2) AS revenue FROM data GROUP BY product ORDER BY revenue DESC",
}


def llm_enabled() -> bool:
    return bool(os.getenv("LLM_API_KEY") or os.getenv("LLM_BASE_URL"))


def _chat(messages: list[dict], max_tokens: int = 300) -> str:
    url = LLM_BASE_URL.rstrip("/") + "/chat/completions"
    payload = json.dumps(
        {"model": LLM_MODEL, "messages": messages, "max_tokens": max_tokens, "temperature": 0.0}
    ).encode()
    headers = {"Content-Type": "application/json"}
    if LLM_API_KEY:
        headers["Authorization"] = f"Bearer {LLM_API_KEY}"
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"].strip()


def _match_example(question: str) -> str | None:
    q = question.lower()
    for key, sql in EXAMPLES.items():
        if all(word in q for word in key.split()):
            return sql
    return None


def to_sql(question: str, schema: str) -> dict:
    """Return {'sql': str|None, 'mode': str, 'note': str}."""
    if llm_enabled():
        try:
            prompt = textwrap.dedent(
                f"""
                {schema}

                Write ONE read-only SQLite SELECT query that answers this question.
                Return only the SQL, no markdown, no explanation.

                Question: {question}
                """
            ).strip()
            sql = _chat([{"role": "user", "content": prompt}])
            sql = re.sub(r"^```\w*\n?|\n?```$", "", sql).strip()
            return {"sql": sql, "mode": "llm", "note": ""}
        except Exception as exc:
            return {"sql": _match_example(question), "mode": "offline", "note": f"LLM call failed ({exc}); tried offline examples."}

    sql = _match_example(question)
    note = "" if sql else (
        "Offline demo mode: I can answer built-in example questions exactly, and "
        "summarize the data for anything else. Configure an LLM endpoint for full "
        "natural-language querying."
    )
    return {"sql": sql, "mode": "offline", "note": note}


def narrate(question: str, result: dict) -> str:
    """Turn a small result set into a one-line English answer (no LLM needed)."""
    rows, cols = result["rows"], result["columns"]
    if not rows:
        return "No matching rows."
    if len(rows) == 1 and len(cols) == 1:
        return f"{cols[0].replace('_', ' ').title()}: {rows[0][0]}"
    if len(rows) == 1:
        pairs = ", ".join(f"{c} = {v}" for c, v in zip(cols, rows[0]))
        return pairs
    top = rows[0]
    return f"Top result: {', '.join(f'{c}={v}' for c, v in zip(cols, top))} ({len(rows)} rows)."
