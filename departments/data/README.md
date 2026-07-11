# 📊 Data & Analytics / BI

> Replace: a BI analyst + a Looker/Tableau seat + ad-hoc SQL requests + a data-pipeline engineer.

Modern open BI tools let anyone ask questions in plain English and get charts
back; text-to-SQL engines turn "what were sales last quarter by region?" into a
query. Together they replace the analyst-in-the-loop for most routine reporting.

**Recommended starter stack:** our [AI Analyst](../../apps/ai-analyst) (plain-English → SQL over your data) + Vanna or Wren AI (text-to-SQL engine) when you outgrow a single CSV.

## ⚡ One-click deploy (recommended)

**Run a talk-to-your-data analyst with one command** — our flagship
[**AI Analyst**](../../apps/ai-analyst) (ask plain-English questions over a CSV and
get the SQL it ran plus a results table) behind Caddy for automatic HTTPS.
[Vanna](https://github.com/vanna-ai/vanna) is the text-to-SQL engine to graduate
to when you point it at a full warehouse.

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/data/deploy
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and your LLM endpoint
docker compose up -d
```

👉 **Full go-live walkthrough (server, DNS, HTTPS, connecting your data):
[deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live on your domain in ~30–60 min.

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable option — the "recommended starter stack"
is our [AI Analyst](../../apps/ai-analyst) + Vanna/Wren AI (text-to-SQL).

---

### [Vanna](https://github.com/vanna-ai/vanna)

> Text-to-SQL framework: chat with your SQL database via LLMs + agentic retrieval.

| | |
|---|---|
| **Stars** | ~24k |
| **Replaces** | a data analyst answering ad-hoc SQL questions |
| **Self-host** | Easy — pip / FastAPI embed |
| **Ship in** | 2–4 hours |
| **Stack** | Python + TypeScript |
| **License** | MIT |

**Why it's on the list:** train it on your schema and it answers questions in SQL. Note: repo archived (read-only) March 2026 — still fully usable.

### [Wren AI](https://github.com/Canner/WrenAI)

> Generative BI engine; AI agents generate, deploy, and govern BI over 22+ data sources.

| | |
|---|---|
| **Stars** | ~16k |
| **Replaces** | a text-to-SQL analyst / self-serve BI |
| **Self-host** | Medium |
| **Ship in** | 2–4 hours |
| **Stack** | Python + Rust |
| **License** | Apache-2.0 (mixed) |

**Why it's on the list:** actively developed text-to-SQL with a semantic layer — the maintained alternative to Vanna.

### [DB-GPT](https://github.com/eosphoros-ai/DB-GPT)

> Agentic AI data assistant: connects to your databases and autonomously plans SQL, runs code, and generates reports from natural language.

| | |
|---|---|
| **Stars** | ~19k |
| **Replaces** | a data analyst chaining SQL + Python for a report |
| **Self-host** | Medium — Docker Compose |
| **Ship in** | 2–4 hours |
| **Stack** | Python |
| **License** | MIT |

**Why it's on the list:** goes beyond single-query text-to-SQL into multi-step agentic analysis (plan, query, execute, chart) — the pick when the ask is a full report, not one query.

---

