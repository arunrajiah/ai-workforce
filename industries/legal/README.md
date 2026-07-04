# ⚖️ Legal — AI-native open source

> Most legal AI lives behind closed SaaS (Harvey, Spellbook, CoCounsel). The
> open-source, *AI-native* corner is genuinely thin: a handful of document-
> intelligence platforms and RAG assistants where an LLM or agent does the real
> work. Region-specific legal LLMs exist (Chinese, German, Korean law) but don't
> generalize, so they're left off this list. The picks below are broadly usable
> and provider-neutral.

> ⚠️ **Not legal advice.** These tools assist review and research; a qualified
> lawyer must sign off on anything that matters.

### [OpenContracts](https://github.com/Open-Source-Legal/OpenContracts)

> Document-intelligence platform where AI agents reason over an annotated, citation-linked corpus — structured extraction, semantic search, and an MCP server for agents.

| | |
|---|---|
| **Stars** | ~1.4k |
| **AI** | LLM agents + structured extraction + vector search over legal documents |
| **Replaces** | contract-review / document-intelligence SaaS |
| **Self-host** | Medium — Python + TypeScript, Docker |
| **License** | MIT |

### [LawGlance](https://github.com/lawglance/lawglance)

> A RAG-based AI legal assistant — point it at a legal corpus and get grounded, retrieval-backed answers (LangChain + Chroma).

| | |
|---|---|
| **Stars** | ~270 |
| **AI** | retrieval-augmented LLM Q&A over legal documents |
| **Replaces** | paid AI legal-research assistants |
| **Self-host** | Medium — Python; bring your own LLM |
| **License** | Apache-2.0 |

### [OLAW](https://github.com/harvard-lil/olaw)

> Open Legal AI Workbench from Harvard's Library Innovation Lab — a RAG chatbot that calls legal APIs to ground its answers; built for legal-AI UX research.

| | |
|---|---|
| **Stars** | ~160 |
| **AI** | tool-using RAG over live legal APIs (OpenAI or local via Ollama) |
| **Replaces** | ad-hoc legal-research chat tools |
| **Self-host** | Medium — Python + JS |
| **License** | MIT |

---

Honest note: AI-native legal OSS is sparse. Beyond OpenContracts, the field is
early-stage and low-star, and the highest-traction legal LLMs are locked to a
single jurisdiction. For private "chat with our contracts" the general RAG stacks
in the [Legal department](../../departments/legal/) (AnythingLLM, Onyx, PrivateGPT)
are often the more practical starting point.

Related departments: [Legal & Compliance](../../departments/legal/).
🏭 Back to the [industry index](../README.md).
