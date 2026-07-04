# 🧑‍💼 Human Resources & Recruiting

> Replace: a recruiter's ATS + an interview scheduler + an HRIS + onboarding paperwork.

From sourcing to onboarding, HR runs on structured workflows — exactly what
open-source HRMS tools plus an LLM screener handle well. Screen resumes, schedule
interviews, run payroll, and sign offer letters without a stack of SaaS seats.

**Recommended starter stack:** FoloUp for AI phone screens + Aural for structured AI interviews.

## AI-native options

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

### [Aural](https://github.com/1146345502/aural-oss)

> AI interview platform that conducts structured voice, chat, and video interviews, then generates scored reports.

| | |
|---|---|
| **Stars** | ~100 |
| **Replaces** | Async interview tools / first-pass interview coordination |
| **Self-host** | Medium — Next.js, Supabase, and LLM/voice provider keys |
| **Ship in** | ~half a day |
| **Stack** | TypeScript (Next.js) + Supabase |
| **License** | MIT |

**Why it's on the list:** the AI interviewer, follow-up questions, resume import, and post-interview scoring are core to the product. It is newer and much smaller than FoloUp, but covers structured chat/video/coding interviews instead of only phone screens.

### [Veska](https://github.com/arunrajiah/veska)

> AI-native ERP with built-in HR that configures from a plain-English description of your business, then runs from Slack/WhatsApp/Email. Covers this whole department, not just HR.

| | |
|---|---|
| **Stars** | ~2 (new project) |
| **Replaces** | a full HRIS + the rest of the back office, in one deploy |
| **Self-host** | Medium — `docker compose up`, bring your own LLM |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (Next.js) |
| **License** | Apache-2.0 |

**Why it's on the list:** there isn't yet a strong single-purpose AI-native HRIS in this space, so an all-in-one option is worth including. **Disclosure:** built by this repo's maintainer — judge it on the same bar as everything else here. [Go-live guide](../../apps/veska/GO-LIVE.md).

---
