"""AI SDR — research a lead from its website and draft personalized outreach.

Runs fully offline (no API key). Configure an OpenAI-compatible LLM endpoint for
fully written emails.

    pip install -r requirements.txt
    uvicorn app:app --reload            # web UI at http://localhost:8000
    # or CLI:
    python app.py --company "Acme" --website acme.com --value "cutting onboarding time"
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from llm import draft as draft_email
from llm import llm_enabled
from research import research as run_research

app = FastAPI(title="AI SDR", version="1.0.0")


class Lead(BaseModel):
    company: str
    website: Optional[str] = None
    notes: Optional[str] = None
    value_prop: str = "getting more done with a smaller team"


@app.get("/", response_class=HTMLResponse)
def index():
    return (Path(__file__).parent / "static" / "index.html").read_text()


@app.get("/api/health")
def health():
    return {"status": "ok", "mode": "llm" if llm_enabled() else "offline"}


@app.post("/api/draft")
def make_draft(lead: Lead):
    research = run_research(lead.website, lead.notes)
    result = draft_email(lead.company, research, lead.value_prop)
    result["research"] = research
    return result


def _cli():
    p = argparse.ArgumentParser(description="AI SDR — draft personalized outreach")
    p.add_argument("--company", required=True)
    p.add_argument("--website", default=None)
    p.add_argument("--notes", default=None)
    p.add_argument("--value", dest="value_prop", default="getting more done with a smaller team")
    args = p.parse_args()
    research = run_research(args.website, args.notes)
    result = draft_email(args.company, research, args.value_prop)
    print(f"\n[mode: {result['mode']}]  [research source: {research.get('source')}]\n")
    print(result["draft"])


if __name__ == "__main__":
    _cli()
