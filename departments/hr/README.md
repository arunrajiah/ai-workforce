# 🧑‍💼 Human Resources & Recruiting

> Replace: a recruiter's ATS + an interview scheduler + an HRIS + onboarding paperwork.

From sourcing to onboarding, HR runs on structured workflows — exactly what
open-source HRMS tools plus an LLM screener handle well. Screen resumes, schedule
interviews, run payroll, and sign offer letters without a stack of SaaS seats.

**Recommended starter stack:** Frappe HR or Horilla (HRMS) + Cal.com (interview scheduling) + Documenso (offer letters). Add FoloUp for AI phone screens.

---

### [Cal.com](https://github.com/calcom/cal.com)

> Open-source scheduling — coordinates interview loops and candidate self-booking; a Calendly alternative.

| | |
|---|---|
| **Stars** | ~46k |
| **Replaces** | Calendly + an interview coordinator |
| **Self-host** | Easy — compose + Postgres |
| **Ship in** | 2–4 hours |
| **Stack** | TypeScript (Next.js, Prisma) |
| **License** | AGPL-3.0 (MIT core parts) |

**Why it's on the list:** interview scheduling is HR's biggest time sink. Round-robin and routing solve it.

### [Frappe HR](https://github.com/frappe/hrms)

> Modern open HR & payroll with 13+ modules: employee lifecycle, leave, attendance, payroll, performance.

| | |
|---|---|
| **Stars** | ~8k |
| **Replaces** | BambooHR / Workday (HRIS + payroll) |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~half a day |
| **Stack** | Python (Frappe) + Vue |
| **License** | GPL-3.0 |

**Why it's on the list:** the most complete free HRIS+payroll. Pairs with ERPNext for a full back office.

### [Horilla](https://github.com/horilla-opensource/horilla)

> Free HRMS covering recruitment, onboarding, attendance, payroll, performance, and offboarding.

| | |
|---|---|
| **Stars** | ~1.3k |
| **Replaces** | Zoho People / BambooHR (all-in-one HRMS) |
| **Self-host** | Easy — Dockerfile + compose |
| **Ship in** | 2–4 hours |
| **Stack** | Python (Django) |
| **License** | LGPL-2.1 |

**Why it's on the list:** lighter than Frappe, covers the full employee lifecycle, quick to stand up.

### [OpenCATS](https://github.com/opencats/OpenCATS)

> Open-source applicant tracking system and recruitment CRM for staffing and hiring teams.

| | |
|---|---|
| **Stars** | ~700 |
| **Replaces** | Bullhorn / Greenhouse (recruiter ATS/CRM) |
| **Self-host** | Easy — Docker |
| **Ship in** | 1–2 hours |
| **Stack** | PHP |
| **License** | GPL-family (see repo) |

**Why it's on the list:** a dedicated ATS if you recruit at volume. Add an LLM to rank inbound resumes.

### [FoloUp](https://github.com/FoloUp/FoloUp)

> AI-powered voice hiring interviews with auto-generated questions and scored responses.

| | |
|---|---|
| **Stars** | ~1.2k |
| **Replaces** | HireVue / first-round phone-screen recruiters |
| **Self-host** | Medium — needs Supabase/Clerk/Retell/OpenAI keys |
| **Ship in** | ~half a day |
| **Stack** | TypeScript (Next.js) |
| **License** | MIT |

**Why it's on the list:** automates the first-round phone screen. More wiring than others, but genuinely replaces a task.

### [OrangeHRM](https://github.com/orangehrm/orangehrm)

> Comprehensive HRM (Community edition): core HR, leave, and applicant tracking.

| | |
|---|---|
| **Stars** | ~1.1k |
| **Replaces** | BambooHR / SAP SuccessFactors (core HRIS) |
| **Self-host** | Easy — Docker images |
| **Ship in** | 2–3 hours |
| **Stack** | PHP + Vue |
| **License** | GPL-3.0 |

**Why it's on the list:** a long-established, stable HRIS for teams that want something battle-tested.

### [Documenso](https://github.com/documenso/documenso)

> Open-source DocuSign alternative — sign offer letters and onboarding paperwork.

| | |
|---|---|
| **Stars** | ~14k |
| **Replaces** | DocuSign for HR paperwork |
| **Self-host** | Easy — official Docker + compose |
| **Ship in** | 2–4 hours |
| **Stack** | TypeScript / Prisma |
| **License** | AGPL-3.0 |

**Why it's on the list:** onboarding is signatures. Close the loop without a per-envelope SaaS bill.

---

📘 **Deploy guide:** [Ship an AI resume screener + scheduler](../../docs/departments/hr.mdx)
