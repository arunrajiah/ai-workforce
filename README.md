<div align="center">

# 🤖 AI Workforce

### Open-source, AI-native apps that run entire departments. Assemble your AI company in an afternoon.

**Every entry is AI-native — an LLM or AI agent at its core — mapped to the department it replaces.**
Sales. Marketing. Support. HR. Finance. Legal. Engineering. Data. Design. Ops. Product. Executive.

<br/>

[![Departments](https://img.shields.io/badge/departments-12-6C5CE7)](departments/)
[![Industries](https://img.shields.io/badge/industries-18_verticals_·_87_tools-0984E3)](industries/)
[![AI-native](https://img.shields.io/badge/AI--native-only-00B894)](#-the-departments)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)
[![Good first issues](https://img.shields.io/github/issues/arunrajiah/ai-workforce/good%20first%20issue?label=good%20first%20issues&color=7057ff)](https://github.com/arunrajiah/ai-workforce/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)

[**📚 Docs & Tutorials**](https://hub.arunrajiah.com/docs) · [**🏭 By Industry**](industries/) · [**🚀 Flagship apps**](apps/) · [**🤝 Contribute**](CONTRIBUTING.md)

</div>

---

## The idea

Every company is a set of departments. Every department is a set of repetitive,
well-defined workflows. In 2026, **almost every one of those workflows has a
mature, open-source, AI-native app** that can do it.

**AI Workforce** is the map. For each department, we curate the best open-source
**AI** apps — LLM- or agent-native, not legacy software with an "AI" sticker — tell
you honestly what each replaces, and show you how to ship it in hours.

> The goal isn't to fire your team. It's to give a small team — or a solo founder —
> the output of a big one. Run the company you couldn't afford to staff.

---

## 🚀 Quick start

1. Read the **[Quickstart](docs/quickstart.mdx)** — the shared foundation (an LLM endpoint, a vector store, Docker, a domain, secrets). Local Ollama works everywhere.
2. Pick your **department** below and see its options.
3. Deploy the one-click stack that fits, or run a **[flagship app](apps/)** with zero API keys via offline demo mode.

---

## 🏢 The departments

Every listed tool is **AI-native**. Most departments have a specialized primary; a
few (Sales, Support, HR, Finance, Ops) don't yet have a strong single-purpose
AI-native tool that covers the whole job, so [Veska](apps/veska/) — an open-source,
AI-native ERP — is listed there as an all-in-one option alongside the individual tools.

| Department | AI-native options |
|---|---|
| [📈 Sales & Revenue](departments/sales/) | SalesGPT · our [AI SDR](apps/ai-sdr) · [Veska](apps/veska/) (all-in-one) |
| [📣 Marketing & Growth](departments/marketing/) | [Dify](departments/marketing/deploy/) · Activepieces |
| [🎧 Customer Support](departments/support/) | Onyx · AnythingLLM · Botpress · [Veska](apps/veska/) (all-in-one) |
| [🧑‍💼 Human Resources](departments/hr/) | FoloUp · Aural · [Veska](apps/veska/) (all-in-one) |
| [💰 Finance & Accounting](departments/finance/) | Unstract · [Veska](apps/veska/) (all-in-one) |
| [⚖️ Legal & Compliance](departments/legal/) | [AnythingLLM](departments/legal/deploy/) · Onyx · PrivateGPT |
| [🛠️ Engineering / DevOps](departments/engineering/) | [OpenHands](departments/engineering/deploy/) · Aider |
| [📊 Data & Analytics](departments/data/) | [AI Analyst](departments/data/deploy/) · Vanna · Wren AI |
| [🎨 Design & Creative](departments/design/) | [ComfyUI](departments/design/deploy/) · InvokeAI |
| [⚙️ Operations & PM](departments/operations/) | [Veska](apps/veska/) (no strong single-purpose alternative yet) |
| [🔬 Product & Research](departments/product/) | [GPT Researcher](departments/product/deploy/) · Open Deep Research |
| [🧭 Executive / Assistant](departments/executive/) | [Khoj](departments/executive/deploy/) · Fabric · Meetily |

---

## 🏭 Browse by industry

Same AI-native tools, re-sliced by vertical — **87 tools across 18 industries**. Each page lists the best AI-native OSS for that sector (and flags where a vertical is still thin).

| | | | |
|---|---|---|---|
| 🏥 [Healthcare](industries/healthcare/) | ⚖️ [Legal](industries/legal/) | 💳 [Fintech](industries/fintech/) | 🛡️ [Insurance](industries/insurance/) |
| 🛒 [E-commerce](industries/ecommerce/) | 🎬 [Media & Creative](industries/media/) | 🎥 [Film & Video](industries/film/) | 🎵 [Music & Audio](industries/music/) |
| 🎓 [Education](industries/education/) | 🏠 [Real Estate](industries/real-estate/) | 🚚 [Logistics](industries/logistics/) | 🍽️ [Hospitality](industries/hospitality/) |
| 🏛️ [Government](industries/government/) | 🌾 [Agriculture](industries/agriculture/) | 🔐 [Cybersecurity](industries/cybersecurity/) | 🧪 [Scientific Research](industries/scientific-research/) |
| 🎮 [Game Dev](industries/gamedev/) | 🤖 [Robotics](industries/robotics/) | | |

→ Full [Industry Index](industries/)

---

## ⭐ Starter kits (copy-paste stacks)

| Kit | Stack | You get |
|---|---|---|
| **The One-Person Company** | [Veska](apps/veska/) | CRM + support + finance + HR + ops, run from Slack |
| **The Private Brain** | Ollama + AnythingLLM + Onyx | Fully offline AI RAG over your company's docs |
| **The Growth Engine** | Dify + Activepieces | AI content generation and campaign automation |
| **The Autonomous Dev** | OpenHands + Aider | Issues → pull requests, and a terminal pair-programmer |
| **The Research Desk** | GPT Researcher + Khoj | Cited market research + a personal AI second brain |

---

## 🧱 Flagship apps

Original, runnable reference apps — each with an **offline mode** (zero API keys). Provider-neutral: point them at any OpenAI-compatible endpoint (Ollama, LiteLLM, …).

| App | What it does | Stack |
|---|---|---|
| [`apps/ai-sdr`](apps/ai-sdr) | Researches a lead from a URL and drafts personalized outreach | Python / FastAPI |
| [`apps/ai-support-agent`](apps/ai-support-agent) | RAG support agent that answers from your docs with citations | Python / FastAPI |
| [`apps/ai-analyst`](apps/ai-analyst) | Ask your data questions in English, get answers + SQL | Python / FastAPI |

---

## 🤝 Contributing

This list gets better — and more starred — with every good addition. The bar:
**open-source and AI-native** (an LLM or AI agent at its core), self-hostable, and
shippable in ~a day.

**🌱 New here? Start with a [good first issue](https://github.com/arunrajiah/ai-workforce/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22).** The easiest is *verifying a page* — re-checking that a page's entries are still accurate. It takes 20 minutes and is exactly the judgment we look for in reviewers.

**Ways to contribute** (each has a [guided issue template](https://github.com/arunrajiah/ai-workforce/issues/new/choose)):
add an AI-native app · report a broken/stale entry · verify a page · propose a new department or industry · fix a deploy · or [start a discussion](https://github.com/arunrajiah/ai-workforce/discussions).

How submissions are reviewed — the rubric, approval thresholds, and verification cadence — is in **[REVIEWING.md](REVIEWING.md)**; the format and quality bar are in **[CONTRIBUTING.md](CONTRIBUTING.md)**. One app per PR. No affiliate links, ever.

<div align="center">

### If this map saved you a week of research, give it a ⭐ — it's how other people find it.

<br/>

**Maintained by [Arun Rajiah](https://hub.arunrajiah.com)** · Docs on [hub.arunrajiah.com/docs](https://hub.arunrajiah.com/docs)

</div>

---

<details>
<summary><b>FAQ</b></summary>

**What counts as "AI-native"?**
The tool's core is an LLM or an AI agent — it does the work with AI, not a legacy
app with an AI add-on bolted on. That's why you won't find generic CRMs, ERPs, or
helpdesks here.

**Can I actually run a company on this?**
A small or solo team can run a *lot* of it. These are real, production-grade projects.
You still need judgment, security, and (for regulated work) compliance sign-off.

**Do I need API keys?**
No — everything is provider-agnostic and runs against a local [Ollama](https://github.com/ollama/ollama)
for a fully private, free setup. Point at a hosted OpenAI-compatible endpoint if you prefer.

**Are the licenses safe for commercial use?**
Most are MIT/Apache/AGPL/GPL. Some are source-available or have commercial gates —
every card flags this; check the linked repo before you ship.

</details>
