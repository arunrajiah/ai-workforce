"""Optional Chatwoot integration.

When CHATWOOT_BASE_URL + CHATWOOT_API_TOKEN are set, the app can post replies back
into a Chatwoot conversation — turning this RAG agent into a working Chatwoot
Agent Bot that auto-answers incoming customer messages.
"""
from __future__ import annotations

import json
import os
import urllib.request


def base_url() -> str:
    return os.getenv("CHATWOOT_BASE_URL", "").rstrip("/")


def enabled() -> bool:
    return bool(os.getenv("CHATWOOT_BASE_URL") and os.getenv("CHATWOOT_API_TOKEN"))


def post_reply(account_id, conversation_id, content: str) -> int:
    """Send an outgoing message to a Chatwoot conversation. Returns HTTP status."""
    url = f"{base_url()}/api/v1/accounts/{account_id}/conversations/{conversation_id}/messages"
    data = json.dumps({"content": content, "message_type": "outgoing"}).encode()
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "api_access_token": os.getenv("CHATWOOT_API_TOKEN", "")},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.status
