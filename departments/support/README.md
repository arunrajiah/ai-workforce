# 🎧 Customer Support & Success

> Replace: a Tier-1 support team + a live-chat tool + a knowledge base + a ticket-deflection add-on.

An omnichannel helpdesk plus a RAG agent over your docs deflects the majority of
Tier-1 tickets and drafts answers for the rest. This is the most immediately
ROI-positive department to automate.

**Recommended starter stack:** Chatwoot (omnichannel inbox) + Onyx or AnythingLLM (AI answers over your docs). See the [support deploy guide](../../docs/departments/support.mdx) and the bundled [`apps/ai-support-agent`](../../apps/ai-support-agent) flagship.

---

### [Chatwoot](https://github.com/chatwoot/chatwoot)

> Omnichannel support platform (live chat, email, social) with AI features — an Intercom/Zendesk alternative.

| | |
|---|---|
| **Stars** | ~34k |
| **Replaces** | a support team + Intercom/Zendesk/Freshdesk |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | Ruby on Rails + Vue |
| **License** | MIT (+ enterprise) |

**Why it's on the list:** the best open-source support inbox. MIT core, huge community, real AI assist features.

### [Onyx](https://github.com/onyx-dot-app/onyx) (formerly Danswer)

> Self-hosted AI chat + RAG over your docs with 50+ connectors — powers ticket deflection and internal knowledge.

| | |
|---|---|
| **Stars** | ~31k |
| **Replaces** | a Tier-1 support agent + a knowledge base |
| **Self-host** | Easy — single-command install |
| **Ship in** | 1–3 hours |
| **Stack** | Python + TypeScript |
| **License** | MIT |

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

### [Zammad](https://github.com/zammad/zammad)

> Web-based helpdesk consolidating email, chat, phone, and social into one ticketing system.

| | |
|---|---|
| **Stars** | ~5.7k |
| **Replaces** | a support desk + Zendesk |
| **Self-host** | Medium — needs Elasticsearch |
| **Ship in** | ~1 hour |
| **Stack** | Ruby on Rails |
| **License** | AGPL-3.0 |

**Why it's on the list:** mature, auditable ticketing for teams that need SLAs and reporting.

### [FreeScout](https://github.com/FreeScout-help-desk/freescout)

> Lightweight self-hosted help desk & shared inbox — a Help Scout alternative with unlimited seats.

| | |
|---|---|
| **Stars** | ~4.4k |
| **Replaces** | a shared-inbox support role + Help Scout |
| **Self-host** | Easy — Docker or LAMP |
| **Ship in** | 30–60 min |
| **Stack** | PHP (Laravel) |
| **License** | AGPL-3.0 |

**Why it's on the list:** the low-footprint choice. Runs on a cheap VPS, unlimited users and tickets.

### [Typebot](https://github.com/baptisteArno/typebot.io)

> Visual chatbot builder with OpenAI blocks — lead-capture and conversational support flows, embeddable anywhere.

| | |
|---|---|
| **Stars** | ~10k |
| **Replaces** | a conversational-forms/chatbot role + Landbot/Drift |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | TypeScript (Next.js) |
| **License** | Functional Source License (AGPL fallback) |

**Why it's on the list:** design deflection and qualification flows visually, drop them on any site.

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

---

📘 **Deploy guide:** [Ship a support agent](../../docs/departments/support.mdx) · 🚀 **Flagship app:** [`apps/ai-support-agent`](../../apps/ai-support-agent)
🏭 **Industry cross-links:** [E-commerce](../../industries/README.md#e-commerce--retail) · [SMB / Local](../../industries/README.md#smb--local-business)
