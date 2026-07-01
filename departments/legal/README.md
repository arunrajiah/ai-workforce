# ⚖️ Legal & Compliance

> Replace: outside-counsel document review hours + an e-signature subscription + a GRC platform.

Most in-house legal work is document-shaped: review contracts, answer questions
from a policy library, generate compliance artifacts, and collect signatures. A
private RAG stack over your documents plus e-signature covers the bulk of it —
and keeps confidential material on your own servers.

**Recommended starter stack:** AnythingLLM or Onyx (contract Q&A over your docs) + PrivateGPT for on-prem-only material. Keep it fully local with Ollama for confidential matters.

> ⚠️ **Not legal advice.** These tools assist review; a qualified lawyer must sign off on anything that matters.

## ⚡ One-click deploy (recommended)

**Run the core legal department with one command** — AnythingLLM (private
chat-with-your-contracts Q&A) + Caddy for automatic HTTPS, pre-wired together.
Provider-neutral LLM; defaults to a local Ollama so confidential material never
leaves your network.

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/legal/deploy
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and JWT_SECRET
docker compose up -d
```

👉 **Full go-live walkthrough (server, DNS, HTTPS, wiring the LLM): [deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live on your domain in ~30–60 min.

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable option — the "recommended starter stack"
is AnythingLLM/Onyx (contract Q&A) + PrivateGPT for on-prem-only material. Keep
it fully local with Ollama for confidential matters.

---

### [Onyx](https://github.com/onyx-dot-app/onyx)

> Agentic RAG over your documents — strong for contract/document Q&A across a knowledge base.

| | |
|---|---|
| **Stars** | ~31k |
| **Replaces** | outside legal-research time; internal document Q&A |
| **Self-host** | Easy — single-command install |
| **Ship in** | 1–3 hours |
| **Stack** | Python + TypeScript |
| **License** | MIT |

**Why it's on the list:** point it at your contracts and policies; ask questions, get cited answers.

### [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)

> Private ChatGPT over your own documents — contract review Q&A, policy lookup, multi-user.

| | |
|---|---|
| **Stars** | ~62k |
| **Replaces** | paid AI legal-assistant SaaS |
| **Self-host** | Easy — single Docker container |
| **Ship in** | ~1 hour |
| **Stack** | JavaScript (Node + React) |
| **License** | MIT |

**Why it's on the list:** simplest path to a private "chat with our contracts" tool. Runs fully local with Ollama.

### [PrivateGPT](https://github.com/zylon-ai/private-gpt)

> Local, privacy-first document ingestion with retrieval-and-citations — for material that can't leave premises.

| | |
|---|---|
| **Stars** | ~57k |
| **Replaces** | cloud legal-AI where data must stay on-prem |
| **Self-host** | Medium — local model setup |
| **Ship in** | 2–4 hours |
| **Stack** | Python |
| **License** | Apache-2.0 |

**Why it's on the list:** when confidentiality is absolute — nothing leaves your network.

---

📘 **Deploy guide:** [Ship a private contract-review assistant](../../docs/departments/legal.mdx)
🏭 **Industry cross-links:** [Legal](../../industries/README.md#legal)
