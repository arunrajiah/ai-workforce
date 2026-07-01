"""Drafting layer: personalized outreach from company research (provider-neutral).

Talks to any OpenAI-compatible chat endpoint (Ollama, LiteLLM, LocalAI, vLLM, or
a hosted gateway) via LLM_BASE_URL / LLM_MODEL / LLM_API_KEY. When none is
configured (or a call fails), it produces a real templated draft from the
research signal so the app works with zero setup.
"""
from __future__ import annotations

import json
import os
import textwrap
import urllib.request

LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434/v1")
LLM_MODEL = os.getenv("LLM_MODEL", "llama3.1")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")

SYSTEM_PROMPT = textwrap.dedent(
    """
    You are a top-performing SDR. Write a short, specific, non-salesy cold email
    (max ~90 words) that references something concrete about the prospect's
    company, connects it to the value we offer, and ends with a low-friction
    call to action. Then list 3 crisp talking points. Avoid clichés like
    "I hope this email finds you well". Return the email and the talking points.
    """
).strip()


def llm_enabled() -> bool:
    return bool(os.getenv("LLM_API_KEY") or os.getenv("LLM_BASE_URL"))


def _chat(messages: list[dict], max_tokens: int = 600) -> str:
    url = LLM_BASE_URL.rstrip("/") + "/chat/completions"
    payload = json.dumps(
        {"model": LLM_MODEL, "messages": messages, "max_tokens": max_tokens, "temperature": 0.6}
    ).encode()
    headers = {"Content-Type": "application/json"}
    if LLM_API_KEY:
        headers["Authorization"] = f"Bearer {LLM_API_KEY}"
    req = urllib.request.Request(url, data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode())
    return data["choices"][0]["message"]["content"].strip()


def draft(company: str, research: dict, value_prop: str) -> dict:
    signal = research.get("description") or research.get("title") or ""

    if llm_enabled():
        try:
            user = textwrap.dedent(
                f"""
                Prospect company: {company}
                What they do (from their site): {signal or "unknown"}
                Our value proposition: {value_prop}
                """
            ).strip()
            text = _chat(
                [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": user}]
            )
            return {"draft": text, "mode": "llm", "signal": signal}
        except Exception as exc:
            out = _offline_draft(company, signal, value_prop)
            out["draft"] = f"(LLM call failed: {exc}. Showing offline draft.)\n\n" + out["draft"]
            return out

    return _offline_draft(company, signal, value_prop)


def _offline_draft(company: str, signal: str, value_prop: str) -> dict:
    hook = signal[:140].rstrip(". ") if signal else f"the work {company} is doing"
    email = textwrap.dedent(
        f"""\
        Subject: A quick idea for {company}

        Hi there,

        Saw that {company} focuses on {hook.lower() if hook else 'your space'} — impressive.
        Teams doing that usually hit a wall on {value_prop.lower()}. We help with exactly
        that, and it takes about a day to see whether it moves the needle for you.

        Worth a 15-minute look next week? Happy to send a short async demo instead.

        — Sent by your AI SDR"""
    )
    talking_points = [
        f"Reference their focus: {hook or company}.",
        f"Tie to our value: {value_prop}.",
        "Offer a low-friction next step (15 min or async demo).",
    ]
    body = email + "\n\nTalking points:\n" + "\n".join(f"- {t}" for t in talking_points)
    body += "\n\n_(Offline demo mode — configure an LLM endpoint for a fully written, tailored email.)_"
    return {"draft": body, "mode": "offline", "signal": signal}
