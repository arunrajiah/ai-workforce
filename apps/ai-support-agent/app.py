"""AI Support Agent — a RAG helpdesk that answers from your docs with citations.

Runs fully offline (no API key) using lexical retrieval + an extractive answer.
Configure an OpenAI-compatible LLM endpoint for synthesized, conversational answers.

    pip install -r requirements.txt
    uvicorn app:app --reload
    # open http://localhost:8000
"""
from __future__ import annotations

import os
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel

import chatwoot
from llm import answer as llm_answer
from llm import llm_enabled
from rag import KnowledgeBase

KNOWLEDGE_DIR = os.getenv("KNOWLEDGE_DIR", str(Path(__file__).parent / "knowledge"))

app = FastAPI(title="AI Support Agent", version="1.0.0")
kb = KnowledgeBase(KNOWLEDGE_DIR)


class Ask(BaseModel):
    question: str


@app.get("/")
def index():
    return FileResponse(Path(__file__).parent / "static" / "index.html")


@app.get("/api/health")
def health():
    return {"status": "ok", "chunks_indexed": len(kb.chunks), "mode": "llm" if llm_enabled() else "offline"}


@app.post("/api/ask")
def ask(body: Ask):
    chunks = kb.search(body.question, k=4)
    result = llm_answer(body.question, chunks)
    return result


@app.post("/webhooks/chatwoot")
async def chatwoot_webhook(req: Request):
    """Chatwoot Agent Bot endpoint: auto-answer incoming customer messages.

    Point a Chatwoot AgentBot's outgoing URL at this route. Only 'incoming'
    messages are answered, so the bot never replies to itself (no loops).
    """
    payload = await req.json()
    if payload.get("event") != "message_created" or payload.get("message_type") != "incoming":
        return {"status": "ignored"}

    question = (payload.get("content") or "").strip()
    conversation_id = (payload.get("conversation") or {}).get("id")
    account_id = os.getenv("CHATWOOT_ACCOUNT_ID") or (payload.get("account") or {}).get("id")
    if not (question and conversation_id and account_id):
        return {"status": "skipped", "reason": "missing content/conversation/account"}

    chunks = kb.search(question, k=4)
    result = llm_answer(question, chunks)

    if not chatwoot.enabled():
        return {"status": "dry-run", "answer": result["answer"], "mode": result["mode"]}
    try:
        chatwoot.post_reply(account_id, conversation_id, result["answer"])
    except Exception as exc:
        return {"status": "error", "detail": str(exc)}
    return {"status": "answered", "mode": result["mode"]}
