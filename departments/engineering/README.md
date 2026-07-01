# 🛠️ Engineering / DevOps / IT

> Replace: junior dev hours + an internal-tools engineer + an IT helpdesk + a Zapier/Retool bill.

Autonomous coding agents now take a ticket to a pull request; low-code builders
ship internal tools in an afternoon; automation engines replace integration glue.
This is where AI most directly does the work, not just assists it.

**Recommended starter stack:** OpenHands or Aider (autonomous/pair coding) + Appsmith or Budibase (internal tools) + n8n (automation) + Frappe Helpdesk (IT tickets).

---

### [n8n](https://github.com/n8n-io/n8n)

> Fair-code workflow automation with 400+ integrations and native AI/agent nodes.

| | |
|---|---|
| **Stars** | ~195k |
| **Replaces** | Zapier + an integrations engineer |
| **Self-host** | Easy — `docker run` |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript + Vue |
| **License** | Sustainable Use (fair-code) |

**Why it's on the list:** the automation backbone for every department. If you self-host one thing, start here.

### [OpenHands](https://github.com/All-Hands-AI/OpenHands)

> Self-hosted control center for autonomous coding agents that turn issues into pull requests.

| | |
|---|---|
| **Stars** | ~79k |
| **Replaces** | junior SWE / contract dev shop for scoped tickets |
| **Self-host** | Easy — Docker image + volume mounts |
| **Ship in** | ~1 hour |
| **Stack** | Python + TypeScript |
| **License** | MIT |

**Why it's on the list:** the leading open autonomous-SWE platform. Give it a repo and an issue, review the PR.

### [Aider](https://github.com/Aider-AI/aider)

> Terminal AI pair-programmer that edits your codebase and auto-commits via git.

| | |
|---|---|
| **Stars** | ~47k |
| **Replaces** | pair-programmer / staff-aug dev hours |
| **Self-host** | Easy — `pip install`, runs locally |
| **Ship in** | ~15 min |
| **Stack** | Python |
| **License** | Apache-2.0 |

**Why it's on the list:** the fastest ROI in this whole repo — installed and productive in minutes.

### [Appsmith](https://github.com/appsmithorg/appsmith)

> Low-code platform for internal tools, admin panels, and dashboards — a Retool alternative.

| | |
|---|---|
| **Stars** | ~40k |
| **Replaces** | Retool + an internal-tools engineer |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | 2–4 hours |
| **Stack** | React/TS + Java |
| **License** | Apache-2.0 |

**Why it's on the list:** build the admin panel every ops team asks for, over your existing databases.

### [Budibase](https://github.com/Budibase/budibase)

> Build apps, automations, and AI agents over your business data.

| | |
|---|---|
| **Stars** | ~28k |
| **Replaces** | an internal-tools dev / low-code admin builder |
| **Self-host** | Easy — single Docker image |
| **Ship in** | 2–4 hours |
| **Stack** | TypeScript + Svelte |
| **License** | GPL-3.0 core |

**Why it's on the list:** slightly more app-centric than Appsmith, with built-in automations and AI blocks.

### [Coder](https://github.com/coder/coder)

> Self-hosted cloud development environments and AI coding-agent workspaces defined in Terraform.

| | |
|---|---|
| **Stars** | ~14k |
| **Replaces** | IT/DevOps managing dev environments; Gitpod/Codespaces |
| **Self-host** | Easy — compose provided |
| **Ship in** | 2–4 hours |
| **Stack** | Go + TypeScript |
| **License** | AGPL-3.0 |

**Why it's on the list:** standardize dev environments — and give coding agents clean, reproducible sandboxes.

### [Frappe Helpdesk](https://github.com/frappe/helpdesk)

> Open-source ticket management for IT & customer support with SLAs and a knowledge base.

| | |
|---|---|
| **Stars** | ~3k |
| **Replaces** | Zendesk / Freshdesk for internal IT |
| **Self-host** | Easy — compose, ~5 min |
| **Ship in** | ~1 hour |
| **Stack** | Vue + Python (Frappe) |
| **License** | AGPL-3.0 |

**Why it's on the list:** a clean IT ticketing desk you can wire an LLM into for auto-triage and replies.

---

📘 **Deploy guide:** [Ship an autonomous coding + internal-tools stack](../../docs/departments/engineering.mdx)
