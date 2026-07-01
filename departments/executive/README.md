# 🧭 Executive / Personal Assistant

> Replace: an executive assistant's inbox triage + scheduling + meeting notes + briefings.

The chief-of-staff loop — triage email, schedule, capture meetings, summarize —
is now a set of self-hostable agents. Run them locally with Ollama and your
calendar and inbox never leave your machine.

**Recommended starter stack:** Inbox Zero (email triage) + Meetily (meeting notes) + LobeChat (assistant chat/agent workspace) + Fabric or Khoj (briefings & second brain).

## ⚡ One-click deploy (recommended)

**Run a personal AI assistant with one command** — Khoj (a "second brain" that
chats with and semantically searches your own docs) + Caddy for automatic HTTPS,
pre-wired together and able to run on a local/private LLM.

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/executive/deploy
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and generated secrets
docker compose up -d
```

👉 **Full go-live walkthrough (server, DNS, HTTPS, pointing Khoj at a local LLM,
indexing your docs): [deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live on your domain in ~30–60 min.

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable, AI-native option — the "recommended starter stack"
is Inbox Zero (email) + Meetily (notes) + LobeChat (assistant workspace) + Fabric or Khoj
(briefings & second brain).

---

### [Inbox Zero](https://github.com/elie222/inbox-zero)

> AI email assistant: triage, auto-draft replies, bulk unsubscribe, rules; Slack/Telegram alerts.

| | |
|---|---|
| **Stars** | ~12k |
| **Replaces** | EA email triage; SaneBox / Superhuman AI |
| **Self-host** | Medium — Google OAuth + LLM keys |
| **Ship in** | 2–3 hours |
| **Stack** | TypeScript (Next.js / Prisma) |
| **License** | AGPL-3.0 (+ commercial for 5+ business users) |

**Why it's on the list:** the closest open equivalent to an EA managing your inbox. Note the commercial-use gate.

### [Meetily](https://github.com/Zackriya-Solutions/meeting-minutes)

> Privacy-first AI meeting assistant: local transcription + summarization, no cloud.

| | |
|---|---|
| **Stars** | ~13k |
| **Replaces** | Otter.ai / Fireflies note-taker |
| **Self-host** | Easy — local app + Whisper |
| **Ship in** | 1–2 hours |
| **Stack** | Rust / TypeScript / C++ |
| **License** | MIT |

**Why it's on the list:** meeting notes without sending your conversations to a third party. Fully local.

### [Khoj](https://github.com/khoj-ai/khoj)

> Personal "AI second brain": semantic search + chat over your docs, agents, automations.

| | |
|---|---|
| **Stars** | ~35k |
| **Replaces** | a personal research assistant / knowledge aide |
| **Self-host** | Medium — Docker / pip |
| **Ship in** | 1–2 hours |
| **Stack** | Python / TypeScript |
| **License** | AGPL-3.0 |

**Why it's on the list:** your notes, docs, and email become a chattable brain — local or cloud LLMs.

### [Fabric](https://github.com/danielmiessler/fabric)

> Curated prompt "Patterns" (summarize, extract, brief, analyze) wired into your CLI/workflows.

| | |
|---|---|
| **Stars** | ~43k |
| **Replaces** | ad-hoc chief-of-staff drafting/briefing tasks |
| **Self-host** | Easy — single Go binary + API keys |
| **Ship in** | <1 hour |
| **Stack** | Go |
| **License** | MIT |

**Why it's on the list:** a library of battle-tested prompts you can pipe anything through. Install once, use daily.

### [LobeChat](https://github.com/lobehub/lobe-chat)

> Polished self-hostable AI chat/agent workspace with plugins, knowledge base, multi-model.

| | |
|---|---|
| **Stars** | ~79k |
| **Replaces** | ChatGPT Team as an assistant front-end |
| **Self-host** | Easy — Docker / one-click |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (Next.js) |
| **License** | LobeHub Community License (source-available) |

**Why it's on the list:** the nicest self-hosted chat UI to sit in front of all your models and tools.

---

> **Local & private:** pair any of these with [Ollama](https://github.com/ollama/ollama) (~175k ⭐, MIT) to run entirely offline.
