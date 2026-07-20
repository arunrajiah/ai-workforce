# ⚙️ Operations & Project Management

> Replace: a Zapier/Make bill + an internal-tools engineer + Jira/Notion/Confluence seats.

Operations is glue work: connect systems, track projects, and keep the company's
knowledge in one place. Open automation engines plus a project tracker and a wiki
cover it — and the automation layer is what every other department plugs into.

This was a genuinely thin department for dedicated AI-native OSS — general
trigger-based workflow automation (the Zapier/Make replacement) had no strong
single-purpose AI-native tool for a long time. That's now filled by a genuine
agent — task planning, tool use, persistent memory, and event/schedule-triggered
autonomous runs — alongside AI-native browser/UI automation (a vision-LLM agent
that operates software the way a person would, replacing brittle RPA scripts).
For AI automation glue, see the coding-agent tools in [Engineering](../engineering/).

## AI-native options

### [Skyvern](https://github.com/Skyvern-AI/skyvern)

> Browser automation agent that uses vision LLMs to operate websites like a human — no XPath selectors to maintain — replacing RPA-style UI automation.

| | |
|---|---|
| **Stars** | ~22k |
| **Replaces** | an RPA tool / UI-automation scripts |
| **Self-host** | Medium — Docker Compose, bring your own LLM |
| **Ship in** | ~1–2 hours |
| **Stack** | Python |
| **License** | AGPL-3.0 (core; managed cloud anti-bot features separate) |

**Why it's on the list:** vision-LLM-driven navigation is the actual product, not a bolted-on step in a trigger/action builder — it fills the ops gap for UI-level automation, though it's not a general workflow orchestrator.

### [Coworker](https://github.com/arunrajiah/coworker)

> An AI agent that plans and executes tasks with tools (create/search/update), keeps persistent vector memory across conversations, and runs automations on a schedule or triggered by events (`task_created`, `git_issue_opened`, and more) — whether or not you have the app open.

| | |
|---|---|
| **Stars** | ~6 (new project) |
| **Replaces** | Zapier/Make-style workflow automation + a task manager, in one agent |
| **Self-host** | Easy — `docker compose up` (Postgres + Redis + 3 services) |
| **Ship in** | ~30 min |
| **Stack** | TypeScript (Next.js + Hono) |
| **License** | MIT |

**Why it's on the list:** a real agent loop — multi-step tool use, memory that informs later decisions, and autonomous scheduled/event-triggered runs — not a chat UI on top of a kanban board. Provider-neutral (10+ LLM providers, incl. local Ollama). **Disclosure:** built by this repo's maintainer — judge it on the same bar as everything else here.

### [Veska](https://github.com/arunrajiah/veska)

> AI-native ERP with a built-in workflow engine that configures from a plain-English description of your business, then runs from Slack/WhatsApp/Email.

| | |
|---|---|
| **Stars** | ~2 (new project) |
| **Replaces** | Zapier/Make-style glue + Jira/Notion, in one deploy |
| **Self-host** | Medium — `docker compose up`, bring your own LLM |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (Next.js) |
| **License** | Apache-2.0 |

**Why it's on the list:** the all-in-one option — a full ERP with a workflow engine built in, not just the automation layer. **Disclosure:** built by this repo's maintainer — judge it on the same bar as everything else here. [Go-live guide](../../apps/veska/GO-LIVE.md).

---

