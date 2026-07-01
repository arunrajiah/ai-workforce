# ⚙️ Operations & Project Management

> Replace: a Zapier/Make bill + an internal-tools engineer + Jira/Notion/Confluence seats.

Operations is glue work: connect systems, track projects, and keep the company's
knowledge in one place. Open automation engines plus a project tracker and a wiki
cover it — and the automation layer is what every other department plugs into.

**Recommended starter stack:** n8n or Windmill (automation) + Plane (projects) + AppFlowy or Outline (docs/wiki). Huly if you want it all in one.

---

### [n8n](https://github.com/n8n-io/n8n)

> Visual workflow automation with 400+ integrations and native AI/agent nodes.

| | |
|---|---|
| **Stars** | ~195k |
| **Replaces** | Zapier / Make + ops-automation staff |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript / Vue |
| **License** | Sustainable Use (fair-code) |

**Why it's on the list:** the automation hub of the whole AI Workforce. Every department's workflows live here.

### [Windmill](https://github.com/windmill-labs/windmill)

> Turns scripts (Python/TS/Go/Bash) into APIs, cron jobs, workflows, and auto-generated UIs.

| | |
|---|---|
| **Stars** | ~17k |
| **Replaces** | Retool / Airplane / Temporal + an internal-tools engineer |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | 1–2 hours |
| **Stack** | Rust + Svelte |
| **License** | AGPLv3 + Apache-2.0 (dual) |

**Why it's on the list:** when your automation is really code, Windmill is faster and more scalable than a node canvas.

### [Plane](https://github.com/makeplane/plane)

> Project & issue tracking with cycles, modules, views, and pages — a Jira/Linear alternative.

| | |
|---|---|
| **Stars** | ~54k |
| **Replaces** | Jira / Linear / ClickUp |
| **Self-host** | Medium — `docker compose up` |
| **Ship in** | 2–3 hours |
| **Stack** | TypeScript (React) + Python (Django) |
| **License** | AGPL-3.0 |

**Why it's on the list:** the best-looking open project tracker, moving fast toward Linear parity.

### [Huly](https://github.com/hcengineering/platform)

> All-in-one team platform: project management, CRM, chat, HR, ATS.

| | |
|---|---|
| **Stars** | ~26k |
| **Replaces** | Linear + Jira + Slack + Notion |
| **Self-host** | Medium — `docker compose up` |
| **Ship in** | 2–3 hours |
| **Stack** | TypeScript / Svelte |
| **License** | EPL-2.0 |

**Why it's on the list:** the most ambitious "everything app." One deploy replaces a stack of SaaS.

### [AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)

> AI collaborative workspace: docs, wikis, databases, project boards — a Notion alternative, data stays local.

| | |
|---|---|
| **Stars** | ~73k |
| **Replaces** | Notion |
| **Self-host** | Medium — self-host server + client |
| **Ship in** | 2–3 hours |
| **Stack** | Dart (Flutter) + Rust |
| **License** | AGPL-3.0 |

**Why it's on the list:** the leading open Notion alternative, with local-first data and built-in AI.

### [Outline](https://github.com/outline/outline)

> Realtime collaborative team knowledge base / wiki, markdown-native.

| | |
|---|---|
| **Stars** | ~39k |
| **Replaces** | Confluence / Notion wiki |
| **Self-host** | Medium — needs OAuth provider + S3 |
| **Ship in** | ~2 hours |
| **Stack** | TypeScript (React / Node) |
| **License** | BSL 1.1 (converts to Apache over time) |

**Why it's on the list:** the cleanest open wiki, and a great knowledge source to point support/legal RAG agents at.

---

📘 **Deploy guide:** [Ship a workflow-automation backbone](../../docs/departments/operations.mdx)
