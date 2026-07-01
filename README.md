<div align="center">

# 🤖 AI Workforce

### Open-source AI apps that run entire departments. Assemble your AI company in an afternoon.

**90+ hand-picked, self-hostable AI apps — mapped to the department they replace.**
Sales. Marketing. Support. HR. Finance. Legal. Engineering. Data. Design. Ops. Product. Executive.

<br/>

[![Departments](https://img.shields.io/badge/departments-12-6C5CE7)](departments/)
[![Apps](https://img.shields.io/badge/curated_apps-90+-00B894)](#-the-departments)
[![Industries](https://img.shields.io/badge/industries-7-0984E3)](industries/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)](CONTRIBUTING.md)

[**📚 Docs & Tutorials**](https://hub.arunrajiah.com) · [**🏭 By Industry**](industries/) · [**🚀 Flagship apps**](apps/) · [**🤝 Contribute**](CONTRIBUTING.md)

</div>

---

## The idea

Every company is a set of departments. Every department is a set of repetitive,
well-defined workflows. In 2026, **almost every one of those workflows has a
mature, open-source, self-hostable app** — and an LLM to drive it.

**AI Workforce** is the map. For each department, we curate the best open-source
apps, tell you honestly what each one replaces, and show you how to ship it in
hours — not a research project, a working deployment.

> The goal isn't to fire your team. It's to give a small team — or a solo founder —
> the output of a big one. Run the company you couldn't afford to staff.

### Why this list is different

- **Organized by department, not by framework.** You think "I need to replace my SDR," not "I need a RAG pipeline." This list matches how you actually think.
- **Every entry says what it replaces** — the role *and* the SaaS bill.
- **Ship-time on every card.** Most are `docker compose up` and under an hour.
- **Honest assessments.** We flag rough edges, restrictive licenses, and heavy infra. Trust is the whole point.
- **Verified links & star counts.** CI checks every link on every PR.

---

## 🚀 Quick start

1. Read the **[Quickstart](docs/quickstart.mdx)** — the 5 things every app here needs (an LLM key, a vector store, Docker, a domain, secrets). Set them up once.
2. Pick your **department** below.
3. Follow its deploy guide, or run a **[flagship app](apps/)** with zero API keys via offline demo mode.

```bash
git clone https://github.com/arunrajiah/ai-workforce
cd ai-workforce/apps/ai-support-agent
cp .env.example .env      # works in offline demo mode with no keys
docker compose up
```

---

## 🏢 The departments

| Department | Replaces | Apps | Deploy guide |
|---|---|:--:|---|
| [📈 Sales & Revenue](departments/sales/) | an SDR + CRM + booking + enrichment | 6 | [guide](docs/departments/sales.mdx) |
| [📣 Marketing & Growth](departments/marketing/) | content + social + email + analytics | 7 | [guide](docs/departments/marketing.mdx) |
| [🎧 Customer Support](departments/support/) | Tier-1 support + live chat + KB | 7 | [guide](docs/departments/support.mdx) |
| [🧑‍💼 Human Resources](departments/hr/) | ATS + scheduling + HRIS + onboarding | 7 | [guide](docs/departments/hr.mdx) |
| [💰 Finance & Accounting](departments/finance/) | bookkeeping + invoicing + FP&A | 8 | [guide](docs/departments/finance.mdx) |
| [⚖️ Legal & Compliance](departments/legal/) | contract review + e-sign + GRC | 7 | [guide](docs/departments/legal.mdx) |
| [🛠️ Engineering / DevOps](departments/engineering/) | junior dev + internal tools + IT desk | 7 | [guide](docs/departments/engineering.mdx) |
| [📊 Data & Analytics](departments/data/) | BI analyst + Looker seat + ad-hoc SQL | 7 | [guide](docs/departments/data.mdx) |
| [🎨 Design & Creative](departments/design/) | production designer + stock spend | 6 | [guide](docs/departments/design.mdx) |
| [⚙️ Operations & PM](departments/operations/) | Zapier + Jira + Notion | 6 | [guide](docs/departments/operations.mdx) |
| [🔬 Product & Research](departments/product/) | market research + surveys + analytics | 6 | [guide](docs/departments/product.mdx) |
| [🧭 Executive / Assistant](departments/executive/) | inbox triage + scheduling + notes | 6 | [guide](docs/departments/executive.mdx) |

**Cross-cut by vertical:** [🏭 Industry Index →](industries/) — Healthcare · Legal · Real Estate · E-commerce · Education · Fintech · SMB/Local

---

## ⭐ Starter kits (copy-paste stacks)

Don't want to choose? These proven combinations stand up a working department fast:

| Kit | Stack | You get |
|---|---|---|
| **The Solo Founder** | n8n + Twenty + Chatwoot + listmonk + Metabase | Sales, support, email, and analytics on one box |
| **The Support Desk** | Chatwoot + Onyx | Omnichannel inbox + AI answers that deflect Tier-1 |
| **The Back Office** | ERPNext + Paperless-ngx + Documenso | Accounting, receipt OCR, and signatures |
| **The Private Brain** | Ollama + AnythingLLM + Onyx | Fully offline RAG over your company's docs |
| **The Growth Engine** | Dify + Postiz + listmonk + PostHog | Content, social, email, and product analytics |

---

## 🧱 The three flagship apps

Original reference apps built by maintainers — each runs end-to-end with an
**offline/mock mode** so you can try it with **zero API keys**.

| App | What it does | Stack |
|---|---|---|
| [`apps/ai-sdr`](apps/ai-sdr) | Researches a lead from a URL and drafts personalized outreach | Python / FastAPI |
| [`apps/ai-support-agent`](apps/ai-support-agent) | RAG support agent that answers from your docs with citations | Python / FastAPI |
| [`apps/ai-analyst`](apps/ai-analyst) | Ask your data questions in English, get answers + charts | Python / FastAPI |

---

## 🤝 Contributing

This list gets better — and more starred — with every good addition. Adding an app
takes 5 minutes: see **[CONTRIBUTING.md](CONTRIBUTING.md)** for the card format and
quality bar. One app per PR. No affiliate links, ever.

**Good first contributions:** add an app to a department, fill an industry gap, or write a department deploy guide.

<div align="center">

### If this map saved you a week of research, give it a ⭐ — it's how other people find it.

<br/>

**Maintained by [Arun Rajiah](https://hub.arunrajiah.com)** · Docs on [hub.arunrajiah.com](https://hub.arunrajiah.com)

</div>

---

<details>
<summary><b>FAQ</b></summary>

**Is this just another awesome-list?**
No. Every entry is mapped to the department and role it replaces, carries a ship-time,
and is honestly assessed. Plus we ship original runnable flagship apps.

**Can I actually run a company on this?**
A small or solo team can run a *lot* of it. These are real, production-grade projects
used by thousands of companies. You still need judgment, security, and (for regulated
work) compliance sign-off.

**"Replace a department" — isn't that hype?**
For a solo founder or a lean team, these tools genuinely do the work a department
used to. For a large org, think "give your team 10x leverage." Both are true.

**Are the licenses safe for commercial use?**
Most are MIT/Apache/AGPL/GPL. Some are source-available (n8n, Outline, Twenty enterprise
files, LobeChat) or have commercial gates (Inbox Zero). Every card flags this — check the
linked repo's license before you ship.

**How are apps chosen?**
Open source, self-hostable, department-grade, and shippable in ~a day or less. See
[CONTRIBUTING.md](CONTRIBUTING.md).

</details>
