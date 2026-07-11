---
title: Real Estate — AI-native open source
description: Open-source AI voice agents and document tools for real estate — lead qualification, showing scheduling, and contract extraction.
sidebar_label: Real Estate
slug: /industries/real-estate
keywords: [real estate ai open source, ai lead qualification voice agent, property listing ai, ai contract extraction real estate]
---

# 🏠 Real Estate — AI-native open source

> AI in real estate is mostly conversational and document-shaped: voice agents that qualify leads and book showings, and LLMs that draft listings and pull data out of contracts and disclosures.

### [Vocode-Core](https://github.com/vocodedev/vocode-core)

> Build voice AI agents that qualify inbound leads and schedule showings over the phone — replaces an inside-sales rep or answering service.

| | |
|---|---|
| **Stars** | ~3.8k |
| **AI** | LLM voice agents (STT + LLM + TTS streaming pipeline) |
| **Replaces** | inside-sales/ISA reps, answering service |
| **Self-host** | Medium |
| **License** | MIT |

### [LiveKit Agents](https://github.com/livekit/agents)

> Framework for realtime voice AI agents — reception, callbacks, and showing coordination with semantic turn detection and telephony.

| | |
|---|---|
| **Stars** | ~11k |
| **AI** | Realtime multimodal voice agents (STT/LLM/TTS + turn detection) |
| **Replaces** | front-desk reception, call-handling staff |
| **Self-host** | Medium |
| **License** | Apache-2.0 |

### [Unstract](https://github.com/Zipstack/unstract)

> LLM-driven extraction of structured data from unstructured documents — pull fields out of leases, purchase agreements, and disclosures with natural-language prompts.

| | |
|---|---|
| **Stars** | ~6.7k |
| **AI** | LLM document extraction (Prompt Studio → JSON, ETL/API) |
| **Replaces** | manual data entry from contracts and disclosures |
| **Self-host** | Medium |
| **License** | AGPL-3.0 |

### [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)

> Private ChatGPT over your own documents — a listing/contract Q&A assistant and a way to draft property descriptions from your data.

| | |
|---|---|
| **Stars** | ~62k |
| **AI** | Local RAG chat + agents over your documents |
| **Replaces** | ad-hoc listing copywriting; paid AI-assistant SaaS |
| **Self-host** | Easy |
| **License** | MIT |

### [AI Real Estate Assistant](https://github.com/AleksNeStu/ai-real-estate-assistant)

> Conversational property search and market-analytics platform — natural-language search plus LLM-generated valuation estimates with multi-year forecasts, confidence bands, and key drivers.

| | |
|---|---|
| **Stars** | ~280 |
| **AI** | Multi-provider LLM routing (OpenAI/Google/Grok/DeepSeek/Ollama) for search, analytics, and valuation narratives |
| **Replaces** | a buyer's-agent research session; paid property-analytics SaaS |
| **Self-host** | Medium — FastAPI + Next.js + ChromaDB, Docker |
| **License** | MIT |

---

> 🏠 **Sparse vertical, less so now.** Dedicated AI-native OSS for real estate was thin — no strong open valuation-ML model or listing-generation app with real traction. AI Real Estate Assistant now covers conversational search and LLM-generated valuation narratives, though a dedicated open valuation-ML model (the "Zestimate" equivalent) still doesn't exist as a genuinely AI-native, self-hostable product — the closest analog we could verify (a mass-appraisal toolkit) treats ML as one optional module rather than the core, so it didn't clear this list's bar. The genuinely AI-native path today is voice agents (Vocode/LiveKit) for lead and showing work, conversational search/analytics (AI Real Estate Assistant), plus general LLM tools (Unstract for docs, AnythingLLM for listing/contract Q&A and description drafting).

Related departments: [Sales](../../departments/sales/) · [Support](../../departments/support/)
