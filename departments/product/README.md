# 🔬 Product & Research

> Replace: a market/desk researcher + a survey tool + a product analyst + a "Deep Research" subscription.

Autonomous research agents run multi-source investigations and return cited
reports; feedback platforms capture user signal; analytics tools tell you what
happened. Together they cover the discovery half of product work.

**Recommended starter stack:** GPT Researcher or Open Deep Research (research briefs) + Formbricks (user feedback) + PostHog (product analytics).

---

### [GPT Researcher](https://github.com/assafelovic/gpt-researcher)

> Autonomous agent that runs deep multi-source web research and produces cited reports.

| | |
|---|---|
| **Stars** | ~28k |
| **Replaces** | a junior market/desk researcher; Perplexity-style research |
| **Self-host** | Easy — Docker / pip + API keys |
| **Ship in** | ~1 hour |
| **Stack** | Python |
| **License** | Apache-2.0 |

**Why it's on the list:** the most mature open research agent. Ask a question, get a sourced brief back.

### [Open Deep Research (LangChain)](https://github.com/langchain-ai/open_deep_research)

> Configurable, fully open deep-research agent across model and search providers.

| | |
|---|---|
| **Stars** | ~12k |
| **Replaces** | OpenAI/Gemini "Deep Research"; analyst research briefs |
| **Self-host** | Easy — LangGraph + API keys |
| **Ship in** | ~1 hour |
| **Stack** | Python |
| **License** | MIT |

**Why it's on the list:** MIT-licensed and provider-agnostic — the most hackable deep-research base.

### [deep-research (dzhng)](https://github.com/dzhng/deep-research)

> Lightweight iterative research agent combining search + LLM reasoning into reports.

| | |
|---|---|
| **Stars** | ~19k |
| **Replaces** | manual competitive/market research |
| **Self-host** | Easy — Node + API keys |
| **Ship in** | <1 hour |
| **Stack** | TypeScript |
| **License** | MIT |

**Why it's on the list:** tiny, readable codebase — the best starting point if you want to build your own researcher.

### [Formbricks](https://github.com/formbricks/formbricks)

> Open-source survey & experience platform for in-app, website, and link user feedback.

| | |
|---|---|
| **Stars** | ~13k |
| **Replaces** | Qualtrics / Typeform / Sprig |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | 1–2 hours |
| **Stack** | TypeScript |
| **License** | AGPLv3 |

**Why it's on the list:** capture user signal, then feed responses to an LLM for theme extraction.

### [PostHog](https://github.com/PostHog/posthog)

> Product analytics, session replay, feature flags, experiments, and surveys in one platform.

| | |
|---|---|
| **Stars** | ~35k |
| **Replaces** | Amplitude / Mixpanel / Hotjar + a product analyst |
| **Self-host** | Hard — heavy infra (ClickHouse, Kafka) |
| **Ship in** | 3–4 hours |
| **Stack** | Python / TypeScript |
| **License** | MIT (proprietary `ee/`) |

**Why it's on the list:** the open product-analytics standard, with an AI assistant that answers analytics questions.

### [Onyx](https://github.com/onyx-dot-app/onyx)

> RAG + chat over your docs/tools with connectors — an internal knowledge/research assistant.

| | |
|---|---|
| **Stars** | ~31k |
| **Replaces** | Glean; internal knowledge analyst |
| **Self-host** | Medium — `docker compose up` |
| **Ship in** | ~2 hours |
| **Stack** | Python / TypeScript |
| **License** | MIT |

**Why it's on the list:** turns your accumulated internal docs into a queryable research base.

---

📘 **Deploy guide:** [Ship a user-research + PRD agent](../../docs/departments/product.mdx)
