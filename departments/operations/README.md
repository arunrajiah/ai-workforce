# ⚙️ Operations & Project Management

> Replace: a Zapier/Make bill + an internal-tools engineer + Jira/Notion/Confluence seats.

Operations is glue work: connect systems, track projects, and keep the company's
knowledge in one place. Open automation engines plus a project tracker and a wiki
cover it — and the automation layer is what every other department plugs into.

This is a genuinely thin department for dedicated AI-native OSS — there isn't yet
a strong single-purpose AI-native tool for general ops/workflow automation. For AI
automation glue, see the coding-agent tools in [Engineering](../engineering/).

## AI-native options

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

**Why it's on the list:** the only AI-native option we've found that covers general ops end-to-end. **Disclosure:** built by this repo's maintainer — judge it on the same bar as everything else here. [Go-live guide](../../apps/veska/GO-LIVE.md).

---

