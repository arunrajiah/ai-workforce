# ⚖️ Legal & Compliance

> Replace: outside-counsel document review hours + an e-signature subscription + a GRC platform.

Most in-house legal work is document-shaped: review contracts, answer questions
from a policy library, generate compliance artifacts, and collect signatures. A
private RAG stack over your documents plus e-signature covers the bulk of it —
and keeps confidential material on your own servers.

**Recommended starter stack:** AnythingLLM or Onyx (contract Q&A over your docs) + Documenso/DocuSeal (signatures) + Comply/Probo (compliance). Keep it fully local with Ollama for confidential matters.

> ⚠️ **Not legal advice.** These tools assist review; a qualified lawyer must sign off on anything that matters.

---

### [DocuSeal](https://github.com/docusealco/docuseal)

> Create PDF forms and collect legally-binding signatures — a DocuSign alternative.

| | |
|---|---|
| **Stars** | ~17k |
| **Replaces** | DocuSign / PandaDoc |
| **Self-host** | Easy — single `docker run` |
| **Ship in** | 30–60 min |
| **Stack** | Ruby on Rails + Vue |
| **License** | AGPL-3.0 (additional terms) |

**Why it's on the list:** the fastest self-hosted signing setup. One command to a working signature portal.

### [Documenso](https://github.com/documenso/documenso)

> Open-source e-signature platform with signing certificates.

| | |
|---|---|
| **Stars** | ~14k |
| **Replaces** | DocuSign / Adobe Sign |
| **Self-host** | Easy — official Docker + compose |
| **Ship in** | 1–2 hours |
| **Stack** | TypeScript / Prisma |
| **License** | AGPL-3.0 |

**Why it's on the list:** the most polished open e-signature product, with real audit certificates.

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

### [Probo](https://github.com/getprobo/probo)

> Open-source GRC: controls, vendor risk, access reviews, audit programs, document workflows.

| | |
|---|---|
| **Stars** | ~1.2k |
| **Replaces** | Vanta / Drata / OneTrust (broader GRC) |
| **Self-host** | Medium — multi-service compose |
| **Ship in** | 2–3 hours |
| **Stack** | Go + TypeScript |
| **License** | ISC |

**Why it's on the list:** a genuine open GRC platform, not just policy templates. Good for growing compliance needs.

### [Comply](https://github.com/strongdm/comply)

> SOC2 compliance automation: policy generator, SOC2 templates, ticketing integration.

| | |
|---|---|
| **Stars** | ~1.6k |
| **Replaces** | Vanta / Drata (lightweight, SOC2 policy generation) |
| **Self-host** | Easy — Docker, static-site output |
| **Ship in** | 1–2 hours |
| **Stack** | Go |
| **License** | Apache-2.0 |

**Why it's on the list:** get SOC2 policies published fast. Less actively maintained — good for the policy layer.

---

📘 **Deploy guide:** [Ship a private contract-review assistant](../../docs/departments/legal.mdx)
🏭 **Industry cross-links:** [Legal](../../industries/README.md#legal)
