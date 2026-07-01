# 🏭 Industry Cross-Index

The [departments](../departments) are the primary map. This index re-slices the
same open-source apps by **industry**, so you can find what's most relevant to
your vertical fast. Each entry links back to its full card in the department it
lives in.

---

## Healthcare

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [Medplum](https://github.com/medplum/medplum) | FHIR clinical data store + auth + SDKs (HIPAA-oriented) | a custom EHR backend / Redox-style layer | ~2–3h |
| [OpenEMR](https://github.com/openemr/openemr) | Full EHR + practice management (scheduling, billing) | Epic / athenahealth (SMB clinics) | ~3–4h |
| [Onyx](../departments/legal/README.md) | Private RAG over clinical protocols & policies | internal medical knowledge lookup | ~2h |

> ⚕️ Healthcare data is regulated. Self-host, keep PHI on your own infra, and get compliance sign-off.

## Legal

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [OpenContracts](https://github.com/Open-Source-Legal/OpenContracts) | Document intelligence: citation graphs, extraction, AI agents | Kira-lite contract review / DMS | ~2–3h |
| [Documenso](../departments/legal/README.md) | E-signature for document execution | DocuSign | ~2h |
| [AnythingLLM / PrivateGPT](../departments/legal/README.md) | Private contract Q&A over your own docs | paid AI legal SaaS | ~1–4h |

→ Full department: [Legal & Compliance](../departments/legal/README.md)

## Real Estate

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [Krayin CRM](https://github.com/krayin/laravel-crm) | Laravel CRM (leads, deals, pipelines) for agents | a real-estate CRM SaaS | ~1–2h |
| [Twenty](../departments/sales/README.md) | Modern CRM with custom objects for property pipelines | Salesforce / HubSpot | ~2–3h |
| [Vocode-Core](https://github.com/vocodedev/vocode-core) | Voice AI agents for lead qualification & showing scheduling | a phone SDR / receptionist | ~2–3h |

→ Related department: [Sales & Revenue](../departments/sales/README.md)

## E-commerce / Retail

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [Medusa](https://github.com/medusajs/medusa) | Composable open commerce platform (B2B, DTC, marketplace) | Shopify / commercetools backend | ~2–3h |
| [Next.js Commerce](https://github.com/vercel/commerce) | High-performance headless storefront | a bespoke storefront build | ~1–2h |
| [Chatwoot](../departments/support/README.md) | Omnichannel support + live chat for retail CX | Intercom / Zendesk | ~2h |

→ Related departments: [Support](../departments/support/README.md) · [Marketing](../departments/marketing/README.md)

## Education

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [Moodle](https://github.com/moodle/moodle) | The most-used open LMS: courses, quizzes, grading | Canvas / Blackboard | ~3h |
| [Frappe LMS](https://github.com/frappe/lms) | Lightweight modern LMS: courses, quizzes, certificates | Teachable / Thinkific | ~2h |

→ Related department: [Marketing & Growth](../departments/marketing/README.md)

## Fintech

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [Firefly III](../departments/finance/README.md) | Double-entry personal/SMB finance manager | YNAB / Mint | ~1–2h |
| [ERPNext](../departments/finance/README.md) | Full ERP incl. accounting & financial ops | QuickBooks / NetSuite (SMB) | ~3h |
| [OpenBB](../departments/finance/README.md) | Financial data & analysis platform for AI analysts | Bloomberg Terminal | ~1–2h |

→ Full department: [Finance & Accounting](../departments/finance/README.md)

## SMB / Local Business

| Project | What it does | Replaces | Ship in |
|---|---|---|---|
| [Chatwoot](../departments/support/README.md) | Live chat + email + social support with AI-assist | Intercom / Zendesk | ~2h |
| [Cal.com](../departments/executive/README.md) | Booking/scheduling for appointments (salons, clinics, consultants) | Calendly / Acuity | ~2–3h |
| [Vocode-Core](https://github.com/vocodedev/vocode-core) | Voice AI for reservations, reception, callbacks | a phone receptionist / answering service | ~2–3h |
| [Krayin CRM](https://github.com/krayin/laravel-crm) | Lightweight CRM for lead & customer management | HubSpot Starter | ~1–2h |

---

**Don't see your industry?** [Open an issue](../.github/ISSUE_TEMPLATE/suggest-app.yml) — industry coverage grows with contributions.
