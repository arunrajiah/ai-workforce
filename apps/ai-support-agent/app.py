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

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

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
