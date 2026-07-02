# 🎧 Customer Support & Success

> Replace: a Tier-1 support team + a live-chat tool + a knowledge base + a ticket-deflection add-on.

An omnichannel helpdesk plus a RAG agent over your docs deflects the majority of
Tier-1 tickets and drafts answers for the rest. This is the most immediately
ROI-positive department to automate.

## ⚡ One-click deploy — Veska (recommended)

**This department runs on [Veska](../../apps/veska/) — one AI-native platform that configures CRM, support, finance, HR & ops from a plain-English description, then runs on Slack / WhatsApp / Email.** One deploy covers this department and the rest of your back office.

```bash
git clone https://github.com/arunrajiah/veska.git
cd veska && cp .env.example .env    # set your LLM (local Ollama works) + MAGIC_LINK_SECRET
docker compose up -d && docker compose exec api node apps/api/dist/db/migrate.js
```

👉 **Go live on your domain with HTTPS: [apps/veska/GO-LIVE.md](../../apps/veska/GO-LIVE.md)**

---

## 🧩 Swap a component

Prefer to assemble this department from individual AI tools? These AI-native options each do a slice of the job (Veska above does all of it):

---

### [Onyx](https://github.com/onyx-dot-app/onyx) (formerly Danswer)

> Self-hosted AI chat + RAG over your docs with 50+ connectors — powers ticket deflection and internal knowledge.

| | |
|---|---|
| **Stars** | ~31k |
| **Replaces** | a Tier-1 support agent + a knowledge base |
| **Self-host** | Easy — single-command install |
| **Ship in** | 1–3 hours |
| **Stack** | Python + TypeScript |
| **License** | MIT (core; ee dirs separate) |

**Why it's on the list:** connect your docs/Slack/Confluence and it answers with citations. The deflection engine.

### [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)

> All-in-one private ChatGPT over your documents with built-in agents — a self-hosted support/KB assistant.

| | |
|---|---|
| **Stars** | ~62k |
| **Replaces** | an internal support/KB assistant + a custom GPT |
| **Self-host** | Easy — single Docker container |
| **Ship in** | ~20 min |
| **Stack** | JavaScript (Node + React) |
| **License** | MIT |

**Why it's on the list:** fastest way to a working "chat with our docs" agent, with multi-user access built in.

### [Botpress](https://github.com/botpress/botpress)

> Open-source platform for building LLM-powered support chatbots and assistants.

| | |
|---|---|
| **Stars** | ~15k |
| **Replaces** | a chatbot/deflection agent + Intercom Fin/Ada |
| **Self-host** | Medium — Docker |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript |
| **License** | MIT |

**Why it's on the list:** a full conversational-AI builder when you need more control than a widget gives you.

Also: our [AI Support Agent](../../apps/ai-support-agent) flagship answers tickets from your docs.

---

🚀 **Flagship app:** [`apps/ai-support-agent`](../../apps/ai-support-agent)
🏭 **Industry cross-links:** [E-commerce](../../industries/README.md#e-commerce--retail) · [SMB / Local](../../industries/README.md#smb--local-business)
