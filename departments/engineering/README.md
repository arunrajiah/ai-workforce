# 🛠️ Engineering / DevOps / IT

> Replace: junior dev hours + an internal-tools engineer + an IT helpdesk + a Zapier/Retool bill.

Autonomous coding agents now take a ticket to a pull request; low-code builders
ship internal tools in an afternoon; automation engines replace integration glue.
This is where AI most directly does the work, not just assists it.

## ⚡ One-click deploy (recommended)

**Run an autonomous coding agent with one command** — OpenHands (turns issues into
pull requests) + Caddy for automatic HTTPS, pre-wired together.

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/engineering/deploy
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and (optionally) your LLM endpoint
docker compose up -d
```

👉 **Full go-live walkthrough (server, DNS, HTTPS, connecting an LLM, running your
first task): [deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live on your domain in ~30–60 min.

> ⚠️ OpenHands mounts the host Docker socket to run the agent's code in sandbox
> containers — effectively root on the host. Keep the box dedicated and
> access-restricted; see the security note in the go-live guide.

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable, AI-native option — the **recommended starter stack**
is OpenHands or Aider (autonomous/pair coding).

---

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

---

📘 **Deploy guide:** [Ship an autonomous coding + internal-tools stack](../../docs/departments/engineering.mdx)
