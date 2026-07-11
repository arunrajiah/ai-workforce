---
title: Hospitality & Restaurants — AI-native open source
description: Open-source AI voice agents and assistants for hotels and restaurants — reservations, guest FAQs, and review analysis.
sidebar_label: Hospitality
slug: /industries/hospitality
keywords: [hospitality ai open source, ai reservation agent, restaurant ai assistant, voice ai hotel, guest experience ai]
---

# 🏨 Hospitality & Restaurants — AI-native open source

> AI in hospitality is mostly conversational: voice agents that answer the phone and take reservations, and LLM assistants that answer guest questions and turn reviews and menus into content.

### [Vocode-Core](https://github.com/vocodedev/vocode-core)

> Build voice AI agents for reservations, reception, and callbacks — replaces a host or front-desk phone attendant.

| | |
|---|---|
| **Stars** | ~3.8k |
| **AI** | LLM voice agents (STT + LLM + TTS streaming pipeline) |
| **Replaces** | reservation line staff, phone host |
| **Self-host** | Medium |
| **License** | MIT |

### [LiveKit Agents](https://github.com/livekit/agents)

> Framework for realtime voice AI agents — front-desk reception and booking calls with semantic turn detection and telephony integration.

| | |
|---|---|
| **Stars** | ~11k |
| **AI** | Realtime multimodal voice agents (STT/LLM/TTS + turn detection) |
| **Replaces** | front-desk reception, call handling |
| **Self-host** | Medium |
| **License** | Apache-2.0 |

### [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)

> Private ChatGPT over your own documents — a guest-facing FAQ/concierge chatbot and a tool to draft menu descriptions and marketing copy.

| | |
|---|---|
| **Stars** | ~62k |
| **AI** | Local RAG chat + agents over your documents |
| **Replaces** | guest-services FAQ staff; ad-hoc marketing copy |
| **Self-host** | Easy |
| **License** | MIT |

### [Onyx](https://github.com/onyx-dot-app/onyx)

> Agentic RAG answer engine — a review-and-knowledge assistant that answers staff and guest questions over policies, menus, and feedback.

| | |
|---|---|
| **Stars** | ~31k |
| **AI** | Agentic RAG over your knowledge base |
| **Replaces** | internal knowledge lookup, guest-query triage |
| **Self-host** | Easy |
| **License** | MIT |

### [Jack The Butler](https://github.com/JackTheButler/JackTheButler)

> Self-hosted AI concierge that handles guest communication across WhatsApp, SMS, email, and web chat, routing complex requests to staff — one Docker container, guest data never leaves your server.

| | |
|---|---|
| **Stars** | ~5 (new, actively developed — 300+ commits, 80+ releases) |
| **AI** | LLM guest-chat agent (multi-provider, incl. local Ollama) with knowledge base and escalation logic |
| **Replaces** | a 24/7 front-desk phone/chat attendant; paid hotel-chatbot SaaS |
| **Self-host** | Easy — single Docker container, SQLite |
| **License** | Elastic License 2.0 (source-available; free for own-property use) |

---

> 🏨 **Sparse vertical, still.** There is almost no *dedicated* AI-native OSS for hospitality — most restaurant chatbots and review-sentiment repos are small tutorials, not production tools. Jack The Butler is a genuine exception on the hotel side (purpose-built, well-documented, source-available) despite a low star count so far — it's a very recent launch. The genuinely AI-native path is voice agents (Vocode/LiveKit) for reservations and reception, Jack The Butler for self-hosted guest chat, plus general LLM assistants (AnythingLLM, Onyx) for guest FAQ, review analysis, and menu/marketing content.

Related departments: [Support](../../departments/support/) · [Sales](../../departments/sales/)
