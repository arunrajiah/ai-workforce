---
title: Government & Public Sector — AI-native open source
description: Open-source AI for the public sector — civic-data assistants, RAG over public records, and policy research agents.
sidebar_label: Government
slug: /industries/government
keywords: [government ai open source, civic ai tools, public sector rag, policy analysis ai, open data ai assistant]
---

# 🏛️ Government & Public Sector — AI-native open source

> Most public-sector AI work is document- and records-shaped: answer questions
> from mountains of public records, analyze policy and legislation, and ground
> answers in verifiable open data. Dedicated AI-native OSS for government is still
> **thin** — the strongest, safest options are horizontal RAG and research agents
> run on-prem over public data, plus one emerging civic-data tool.

### [Civic AI Tools](https://github.com/npstorey/civic-ai-tools)

> An MCP server that connects AI assistants to government **open-data portals**
> (311 complaints, inspections, Socrata datasets) so answers come from live civic
> data, not model memory.

| | |
|---|---|
| **Stars** | ~31 (emerging) |
| **AI** | LLM tool-use over public-data APIs via MCP; anti-hallucination grounding |
| **Replaces** | manual open-data lookups; bespoke civic dashboards |
| **Self-host** | Easy — MCP server |
| **License** | MIT (spec CC-BY-4.0) |

**Why it's here:** the one purpose-built civic AI-native tool with a clean design — small but exactly on-vertical. Grounds LLMs in real government data.

### [RAGFlow](https://github.com/infiniflow/ragflow)

> A production RAG engine for grounded Q&A with citations over large document sets — public records, policy libraries, FOIA archives.

| | |
|---|---|
| **Stars** | ~84k |
| **AI** | Agentic RAG with deep document understanding and citation grounding |
| **Replaces** | manual records search; a records/FOIA analyst's first pass |
| **Self-host** | Medium — `docker compose` |
| **License** | Apache-2.0 |

**Why it's here:** legislatures and archives increasingly put an LLM in front of decades of documents; this is the strongest open engine to do it on-prem.

### [Onyx](https://github.com/onyx-dot-app/onyx)

> Self-hosted agentic RAG + chat over your documents and systems — a constituent- and staff-facing knowledge assistant.

| | |
|---|---|
| **Stars** | ~31k |
| **AI** | RAG chat with 50+ connectors, agents, cited answers |
| **Replaces** | Tier-1 constituent Q&A; internal knowledge lookup |
| **Self-host** | Easy — single-command install |
| **License** | MIT |

**Why it's here:** keeps sensitive records on your own infrastructure while giving staff and citizens grounded answers.

### [GPT Researcher](https://github.com/assafelovic/gpt-researcher)

> An autonomous research agent that produces cited briefs — policy analysis, legislation summaries, and impact research.

| | |
|---|---|
| **Stars** | ~28k |
| **AI** | Multi-source autonomous research agent with citations |
| **Replaces** | a policy/legislative researcher's desk research |
| **Self-host** | Easy — Docker / pip |
| **License** | Apache-2.0 |

**Why it's here:** turns "what does this bill change and who does it affect?" into a sourced brief.

---

**Honest note:** beyond Civic AI Tools, there is little *dedicated* government AI-native
OSS — the practical path is horizontal RAG/research agents (above) run privately over
public data. Contributions of on-vertical tools welcome.

Related departments: [Legal](../../departments/legal/) · [Product & Research](../../departments/product/) · [Support](../../departments/support/)
