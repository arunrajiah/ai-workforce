# 🛡️ Insurance — AI-native open source

> Insurance is document-heavy: claims, policies, and forms flow through people who read and re-key them. The AI-native opportunity is exactly there — LLM/vision extraction that structures claim and policy documents, and RAG that answers questions over a policy library.

> ⚠️ **Sparse vertical, stated honestly.** There is no large, dedicated *insurance-specific* AI-native OSS project yet — the insurance-branded repos on GitHub are small demos, workshop labs, and course projects (single- to low-double-digit stars), not production software. So this page lists the mature, genuinely AI-native document and RAG tools that map directly onto claims and policy work. Point them at your forms and policy library.

### [Unstract](https://github.com/Zipstack/unstract)

> LLM extraction that turns claim forms, loss reports, and policy schedules into structured JSON from a plain-language schema — replacing manual re-keying of every submission. (Insurance is a stated target use case.)

| | |
|---|---|
| **Stars** | ~7k |
| **AI** | Prompt-defined extraction over any LLM (OpenAI/Bedrock/Gemini/Ollama); deploys as an API or ETL step |
| **Replaces** | claims data-entry clerks; per-form parsers; SaaS IDP |
| **Self-host** | Medium — Docker Compose, wire in an LLM |
| **License** | AGPL-3.0 |

---

### [MinerU](https://github.com/opendatalab/MinerU)

> A VLM + OCR engine that converts messy claim packets and scanned policies — including handwriting and tables — into clean structured markdown/JSON for downstream automation.

| | |
|---|---|
| **Stars** | ~73k |
| **AI** | Vision-language + OCR dual engine; layout, table, and formula parsing across 100+ languages |
| **Replaces** | manual document triage; traditional OCR that chokes on scans |
| **Self-host** | Medium — Python; GPU recommended for the VLM path |
| **License** | Apache-2.0-based (MinerU license) |

---

### [Zerox](https://github.com/getomni-ai/zerox)

> Dead-simple vision-model OCR — hand it a claim PDF or ACORD form and get markdown back — ideal as the ingestion front-end before extraction or a policy chatbot.

| | |
|---|---|
| **Stars** | ~12k |
| **AI** | Vision-model OCR (OpenAI/Bedrock/Gemini) that reads document images to markdown |
| **Replaces** | brittle template OCR for varied claim/policy formats |
| **Self-host** | Easy — small Node/Python lib, bring a vision-model key |
| **License** | MIT |

---

### [Onyx](https://github.com/onyx-dot-app/onyx)

> Agentic RAG over your document set — build a private assistant that answers coverage and policy questions with citations, replacing "let me check the policy wording and get back to you."

| | |
|---|---|
| **Stars** | ~31k |
| **AI** | RAG + deep-research agents over 50+ connectors; runs local with Ollama |
| **Replaces** | manual policy lookup; a paid AI knowledge-assistant SaaS |
| **Self-host** | Easy — single-command install |
| **License** | MIT |

---
For general back-office ops (intake, billing, records admin), see [Veska](../../apps/veska/).
Related departments: [Support](../../departments/support/) · [Legal](../../departments/legal/)
