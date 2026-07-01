# 🔬 Product & Research

> Replace: a market/desk researcher + a survey tool + a product analyst + a "Deep Research" subscription.

Autonomous research agents run multi-source investigations and return cited
reports; feedback platforms capture user signal; analytics tools tell you what
happened. Together they cover the discovery half of product work.

**Recommended starter stack:** GPT Researcher or Open Deep Research (research briefs) + Onyx (internal knowledge research).

## ⚡ One-click deploy (recommended)

**Run the core of the product-research department with one command** — GPT
Researcher (autonomous cited research briefs) + Caddy for automatic HTTPS,
pre-wired together.

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/product/deploy
cp .env.example .env      # set DOMAIN, ACME_EMAIL, TAVILY_API_KEY, LLM_*
docker compose up -d
```

👉 **Full go-live walkthrough (server, DNS, HTTPS, API keys, first research run):
[deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live on your domain in ~30–60 min.

The LLM is provider-neutral: point `LLM_BASE_URL`/`LLM_API_KEY` at any
OpenAI-compatible endpoint (self-hosted, Ollama, a gateway).

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable option — the "recommended starter stack"
is GPT Researcher (research briefs) + Onyx (internal knowledge research).

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

