# 🧑‍💼 Human Resources & Recruiting

> Replace: a recruiter's ATS + an interview scheduler + an HRIS + onboarding paperwork.

From sourcing to onboarding, HR runs on structured workflows — exactly what
open-source HRMS tools plus an LLM screener handle well. Screen resumes, schedule
interviews, run payroll, and sign offer letters without a stack of SaaS seats.

**Recommended starter stack:** Veska (runs the whole department) + FoloUp for AI phone screens.

## ⚡ One-click deploy — Veska (recommended)

**This department runs on [Veska](../../apps/veska/) — one AI-native platform that configures CRM, support, finance, HR & ops from a plain-English description, then runs on Slack / WhatsApp / Email.** One deploy covers this department and the rest of your back office.

```bash
git clone https://github.com/arunrajiah/veska.git
cd veska && cp .env.example .env    # set your LLM (local Ollama works) + MAGIC_LINK_SECRET
docker compose up -d && docker compose exec api node apps/api/dist/db/migrate.js
```

👉 **Go live on your domain with HTTPS: [apps/veska/GO-LIVE.md](../../apps/veska/GO-LIVE.md)**

---

## 🧩 Swap a component

Prefer to assemble this department from individual AI tools? These AI-native options each do a slice of the job (Veska above does all of it):

---

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

---

