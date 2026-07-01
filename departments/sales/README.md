# 📈 Sales & Revenue

> Replace: an SDR/BDR + a CRM admin + a meeting-booking tool + a lead-enrichment subscription.

Wire a CRM, a scraper, and an automation engine together with an LLM and you have
a system that researches leads, writes personalized outreach, books demos, and
keeps the pipeline clean — the core loop of a sales development team.

**Recommended starter stack:** Twenty (CRM) + Firecrawl (lead research) + n8n (outreach sequences) + Cal.com (demo booking). See the [AI SDR deploy guide](../../docs/departments/sales.mdx) and the bundled [`apps/ai-sdr`](../../apps/ai-sdr) flagship.

---

### [Twenty](https://github.com/twentyhq/twenty)

> Modern open-source CRM with custom objects, views, workflows, and AI agents — a Salesforce alternative.

| | |
|---|---|
| **Stars** | ~52k |
| **Replaces** | a Salesforce / HubSpot CRM seat |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | TypeScript (React + NestJS) |
| **License** | AGPL-3.0 |

**Why it's on the list:** the best-looking open CRM, with a real API and workflow engine an agent can drive.

### [Firecrawl](https://github.com/mendableai/firecrawl)

> Turns any website into clean markdown/JSON — the enrichment/research backbone for prospecting.

| | |
|---|---|
| **Stars** | ~142k |
| **Replaces** | an SDR's manual research + Apollo/Clearbit-style enrichment |
| **Self-host** | Medium — compose + workers/queue |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (+ Rust/Go) |
| **License** | AGPL-3.0 (SDKs MIT) |

**Why it's on the list:** feed a company URL, get structured facts back — the fuel for personalized outreach.

### [n8n](https://github.com/n8n-io/n8n)

> Workflow automation with native AI nodes; wires CRM, email, enrichment, and outreach into sequences.

| | |
|---|---|
| **Stars** | ~195k |
| **Replaces** | an SDR-automation role + Zapier/Outreach glue |
| **Self-host** | Easy — `docker run` |
| **Ship in** | ~20 min |
| **Stack** | TypeScript |
| **License** | Sustainable Use (fair-code) |

**Why it's on the list:** the connective tissue of the whole department. Almost every sales workflow is a few n8n nodes.

### [Cal.com](https://github.com/calcom/cal.com)

> Open-source scheduling — books demos and sales calls; a Calendly alternative.

| | |
|---|---|
| **Stars** | ~46k |
| **Replaces** | a Calendly / Chili Piper seat |
| **Self-host** | Medium — Next.js + Postgres |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (Next.js, Prisma) |
| **License** | AGPL-3.0 |

**Why it's on the list:** the booking layer every outbound motion needs, self-hosted and API-driven.

### [NocoBase](https://github.com/nocobase/nocobase)

> AI + no-code platform for building CRMs, deal desks, and RevOps tools with built-in AI employees.

| | |
|---|---|
| **Stars** | ~23k |
| **Replaces** | a custom CRM/RevOps internal tool + Airtable |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | TypeScript (Node + React) |
| **License** | Apache-2.0 (+ commercial plugins) |

**Why it's on the list:** when Twenty is too opinionated, build exactly the pipeline you want.

### [SuiteCRM](https://github.com/salesagility/SuiteCRM)

> Enterprise-grade open CRM: leads, opportunities, cases, quotes, reporting.

| | |
|---|---|
| **Stars** | ~5.6k |
| **Replaces** | Salesforce Sales Cloud / a legacy CRM admin |
| **Self-host** | Medium — LAMP stack |
| **Ship in** | 1–2 hours |
| **Stack** | PHP |
| **License** | AGPL-3.0 |

**Why it's on the list:** mature, feature-dense option for teams that need quotes and complex reporting on day one.

---

📘 **Deploy guide:** [Ship an AI SDR](../../docs/departments/sales.mdx) · 🚀 **Flagship app:** [`apps/ai-sdr`](../../apps/ai-sdr)
🏭 **Industry cross-links:** [Real Estate](../../industries/README.md#real-estate) · [E-commerce](../../industries/README.md#e-commerce--retail)
