# 🛒 E-commerce / Retail — AI-native open source

> Most retail AI is either an agent that acts on a storefront or a model that
> ranks and matches products. The dedicated open-source layer here is thinner
> than in other verticals — self-host the pieces that are genuinely AI-native
> and lean on a general RAG stack for support.

### [browser-use](https://github.com/browser-use/browser-use)

> An LLM agent that drives a real browser — shopping automation, price checks, checkout flows, competitor monitoring — replacing hand-scripted scrapers and RPA bots.

| | |
|---|---|
| **Stars** | ~102k |
| **AI** | LLM agent that plans and executes browser actions autonomously |
| **Replaces** | brittle scraper scripts, RPA seats, manual research |
| **Self-host** | Medium — Python + browser harness, bring your own LLM key |
| **License** | MIT |

---

### [Gorse](https://github.com/gorse-io/gorse)

> An AI recommender engine with classical and LLM rankers plus multimodal embeddings — the "customers also bought" / personalized-feed layer, replacing a hosted recommendations SaaS.

| | |
|---|---|
| **Stars** | ~9.7k |
| **AI** | Embedding-based + LLM rankers over user/item behavior |
| **Replaces** | paid recommendation-as-a-service |
| **Self-host** | Medium — Go service + a datastore (Postgres/MySQL/Mongo) |
| **License** | Apache-2.0 |

---

### [Onyx](https://github.com/onyx-dot-app/onyx)

> Agentic RAG answer engine — point it at product docs, policies, and order data to power AI customer support and internal catalog Q&A, replacing a tier-1 support tool.

| | |
|---|---|
| **Stars** | ~31k |
| **AI** | RAG + agents over your knowledge base, any LLM |
| **Replaces** | paid AI-support/help-desk SaaS |
| **Self-host** | Easy — single-command install |
| **License** | MIT |

---

### [SalesGPT](https://github.com/filip-michalsky/SalesGPT)

> A context-aware AI sales agent for outreach and product Q&A across voice, email, and chat — replacing a scripted outbound tool or a first-touch sales rep.

| | |
|---|---|
| **Stars** | ~2.7k |
| **AI** | LLM agent that tracks conversation stage + product knowledge |
| **Replaces** | scripted outbound / lead-qualification tooling |
| **Self-host** | Medium — Python, 50+ LLMs via LiteLLM |
| **License** | MIT |

---

> ⚠️ **Sparse vertical.** Beyond agents and recommenders, most retail AI OSS
> (product-description generators, review-sentiment, catalog tagging) is small
> hobby-scale code, not production projects. Store platforms and CMSs are
> deliberately excluded — they're infrastructure, not AI-native.

---
For general back-office ops, see [Veska](../../apps/veska/).
Related departments: [Support](../../departments/support/) · [Marketing](../../departments/marketing/) · [Data](../../departments/data/)
