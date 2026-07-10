---
title: Cybersecurity — AI-native open source
description: Open-source AI for security — autonomous pentest agents, LLM vulnerability scanners, and AI red-teaming tools you can self-host.
sidebar_label: Cybersecurity
slug: /industries/cybersecurity
keywords: [ai pentesting open source, llm security scanner, ai red team tools, jailbreak detection open source, cybersecurity ai agent]
---

# 🔐 Cybersecurity — AI-native open source

> Security has two AI frontiers: using LLM agents to *do* offensive and defensive
> work (autonomous pentest, code-auditing, alert triage), and *securing the AI
> itself* (probing models for jailbreaks and prompt injection). The projects below
> put an LLM or ML model at the *core* — not a rules engine with a chat box bolted on.

> 🛡️ **Point it at systems you own.** Autonomous offensive tooling is powerful and
> easy to misuse. Run these only against assets you are authorized to test, keep a
> human in the loop, and never feed secrets to a hosted model you don't control.

### [PentestGPT](https://github.com/GreyDGL/PentestGPT)

> An autonomous penetration-testing agent that plans, reasons over findings, and drives the attack loop — the AI does the recon-and-exploit thinking a junior pentester would.

| | |
|---|---|
| **Stars** | ~14k |
| **AI** | LLM-agent reasoning loop that maintains context and pursues an objective across iterations |
| **Replaces** | manual junior-pentester legwork; scripted recon chains |
| **Self-host** | Medium — Python; bring your own LLM |
| **License** | MIT |

### [NVIDIA garak](https://github.com/NVIDIA/garak)

> An LLM vulnerability scanner — the "nmap for language models," probing your model for jailbreaks, prompt injection, data leakage, and toxic-output failure modes.

| | |
|---|---|
| **Stars** | ~8.3k |
| **AI** | model-red-teaming probes + detectors that attack and evaluate LLMs directly |
| **Replaces** | ad-hoc manual jailbreak testing; commercial LLM-security scanners |
| **Self-host** | Easy — pip install; targets local or hosted models |
| **License** | Apache-2.0 |

### [Vulnhuntr](https://github.com/protectai/vulnhuntr)

> LLM-driven vulnerability discovery that traces full call chains from user input to sink — finding remotely exploitable bugs (RCE, SQLi, SSRF, XSS) that static analysers miss.

| | |
|---|---|
| **Stars** | ~2.7k |
| **AI** | LLM reasoning over whole code call-chains for exploit-path discovery |
| **Replaces** | rules-only SAST for complex multi-step vulnerabilities |
| **Self-host** | Easy — Python CLI; bring your own LLM (any OpenAI-compatible endpoint) |
| **License** | AGPL-3.0 |

### [agentic_security](https://github.com/msoedov/agentic_security)

> An open red-teaming scanner for LLMs and agent workflows — runs multi-step jailbreaks, fuzzing, and RL-based probes across text, image, and audio inputs.

| | |
|---|---|
| **Stars** | ~1.9k |
| **AI** | adversarial attack generation + RL probes targeting LLM/agent robustness |
| **Replaces** | manual jailbreak QA; paid AI-safety testing services |
| **Self-host** | Easy — Python; runs in CI against your endpoints |
| **License** | Apache-2.0 |

### [Nebula](https://github.com/berylliumsec/nebula)

> An AI-powered pentest assistant that wraps offensive tooling in an LLM CLI — ask in natural language and it suggests scans, interprets output, and proposes exploitation paths.

| | |
|---|---|
| **Stars** | ~1k |
| **AI** | LLM (OpenAI / Llama-3.1 / Mistral-7B) for real-time analysis and tool orchestration |
| **Replaces** | context-switching between recon tools and manual result reading |
| **Self-host** | Medium — Python; supports local models |
| **License** | BSD-2-Clause |

---

Cybersecurity has genuine AI-native depth on both sides of the line: offensive
agents (PentestGPT, Nebula), LLM-driven code auditing (Vulnhuntr), and — the
fastest-growing slice — tools that secure the models themselves (garak,
agentic_security). If you deploy LLMs in production, treat the last two as
table stakes.

Related departments: [Engineering](../../departments/engineering/) (code review, CI) · [Data](../../departments/data/) (log and alert analytics).
🏭 Back to the [industry index](../README.md).
