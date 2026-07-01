"""LLM provider layer (provider-neutral).

Talks to any OpenAI-compatible chat endpoint — Ollama, LiteLLM, LocalAI, vLLM,
or a hosted gateway — configured via LLM_BASE_URL / LLM_MODEL / LLM_API_KEY.
When no endpoint is configured (or a call fails), it falls back to a fully
offline mode that stitches an answer from the retrieved context, so the app runs
end-to-end with zero setup.
"""
from __future__ import annotations

import json
import os
import textwrap
import urllib.request

# Defaults target a local Ollama server so the app is private and free by default.
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")

SYSTEM_PROMPT = textwrap.dedent(
    """
    You are a helpful customer-support agent. Answer the user's question using ONLY
    the provided context passages. Be concise and friendly. If the context does not
    contain the answer, say you don't have that information and offer to escalate to
    a human. Always cite the sources you used by their [n] number.
    """
).strip()


def llm_enabled() -> bool:
    return bool(os.getenv("LLM_API_KEY") or os.getenv("LLM_BASE_URL"))


def _chat(messages: list[dict], max_tokens: int = 700) -> str:
    url = LLM_BASE_URL.rstrip("/") + "/chat/completions"
    payload = json.dumps(
        {"model": LLM_MODEL, "messages": messages, "max_tokens": max_tokens, "temperature": 0.2}
    ).encode()
    headers = {"Content-Type": "application/json"}
    if LLM_API_KEY:
        headers["Authorization"] = f"Bearer {LLM_API_KEY}"
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"].strip()


def _format_context(chunks: list[dict]) -> str:
    return "\n\n".join(f"[{i + 1}] ({c['source']})\n{c['text']}" for i, c in enumerate(chunks))


def answer(question: str, chunks: list[dict]) -> dict:
    """Return {'answer': str, 'mode': 'llm'|'offline', 'sources': [...]}"""
    sources = [{"n": i + 1, "source": c["source"]} for i, c in enumerate(chunks)]
    context = _format_context(chunks)

    if llm_enabled():
        try:
            text = _chat(
                [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Context passages:\n{context}\n\nQuestion: {question}"},
                ]
            )
            return {"answer": text, "mode": "llm", "sources": sources}
        except Exception as exc:  # fall through to offline mode on any error
            offline = _offline_answer(question, chunks)
            offline["answer"] = f"(LLM call failed: {exc}. Showing offline answer.)\n\n" + offline["answer"]
            return offline

    return _offline_answer(question, chunks)


def _offline_answer(question: str, chunks: list[dict]) -> dict:
    """Extractive fallback: return the most relevant passages with citations."""
    sources = [{"n": i + 1, "source": c["source"]} for i, c in enumerate(chunks)]
    if not chunks:
        return {
            "answer": "I don't have information on that yet. Want me to escalate to a human?",
            "mode": "offline",
            "sources": [],
        }
    body = "\n\n".join(f"{c['text'].strip()} [{i + 1}]" for i, c in enumerate(chunks[:2]))
    answer_text = (
        "Here's what our knowledge base says:\n\n"
        f"{body}\n\n"
        "_(Offline demo mode — configure an LLM endpoint for a synthesized, conversational answer.)_"
    )
    return {"answer": answer_text, "mode": "offline", "sources": sources}
