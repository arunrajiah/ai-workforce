# 📊 Data & Analytics / BI

> Replace: a BI analyst + a Looker/Tableau seat + ad-hoc SQL requests + a data-pipeline engineer.

Modern open BI tools let anyone ask questions in plain English and get charts
back; text-to-SQL engines turn "what were sales last quarter by region?" into a
query. Together they replace the analyst-in-the-loop for most routine reporting.

**Recommended starter stack:** Metabase (self-serve BI + NL questions) + Vanna or Wren AI (text-to-SQL agent) + Airflow (pipelines) if you need orchestration.

---

### [Metabase](https://github.com/metabase/metabase)

> Easy open-source BI and embedded analytics — ask questions in plain language, build dashboards.

| | |
|---|---|
| **Stars** | ~48k |
| **Replaces** | a BI analyst / Looker / Tableau seat |
| **Self-host** | Easy — official Docker image |
| **Ship in** | ~1 hour |
| **Stack** | Clojure + React/TS |
| **License** | AGPL-3.0 (+ commercial editions) |

**Why it's on the list:** the friendliest open BI. Non-technical teams self-serve; it has native NL questions.

### [Apache Superset](https://github.com/apache/superset)

> Data exploration and visualization at scale — SQL Lab, rich charts, dashboards.

| | |
|---|---|
| **Stars** | ~74k |
| **Replaces** | a BI/analytics engineer / Tableau / Looker |
| **Self-host** | Medium — compose for dev; prod needs tuning |
| **Ship in** | 2–4 hours |
| **Stack** | Python/Flask + React |
| **License** | Apache-2.0 |

**Why it's on the list:** the most powerful fully-permissive BI. Apache-2.0 makes it safe for any commercial use.

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

### [Redash](https://github.com/getredash/redash)

> Connect any data source, query, visualize, dashboard, and share; scheduled refreshes + alerts.

| | |
|---|---|
| **Stars** | ~29k |
| **Replaces** | a SQL analyst / lightweight BI |
| **Self-host** | Easy — Dockerfile + compose |
| **Ship in** | 2–4 hours |
| **Stack** | Python + JS/TS |
| **License** | BSD-2-Clause |

**Why it's on the list:** 35+ data sources and simple alerting. Permissive BSD license.

### [Lightdash](https://github.com/lightdash/lightdash)

> Open-source Looker alternative; agentic BI with metrics defined as code (dbt-native).

| | |
|---|---|
| **Stars** | ~6k |
| **Replaces** | a Looker seat / analytics engineer |
| **Self-host** | Easy — Dockerfile + compose |
| **Ship in** | 2–4 hours |
| **Stack** | TypeScript |
| **License** | MIT-family |

**Why it's on the list:** metrics-as-code keeps definitions consistent — the right choice for dbt teams.

### [Apache Airflow](https://github.com/apache/airflow)

> Author, schedule, and monitor data pipelines as code.

| | |
|---|---|
| **Stars** | ~46k |
| **Replaces** | a data engineer maintaining ETL/orchestration |
| **Self-host** | Medium — Docker + Helm |
| **Ship in** | 2–4 hours |
| **Stack** | Python |
| **License** | Apache-2.0 |

**Why it's on the list:** when analytics needs fresh data, this is the industry-standard orchestrator.

---

📘 **Deploy guide:** [Ship a talk-to-your-data BI agent](../../docs/departments/data.mdx)
