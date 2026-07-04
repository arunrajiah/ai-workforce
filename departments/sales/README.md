# 📈 Sales & Revenue

> Replace: an SDR/BDR + a CRM admin + a meeting-booking tool + a lead-enrichment subscription.

Wire a CRM, a scraper, and an automation engine together with an LLM and you have
a system that researches leads, writes personalized outreach, books demos, and
keeps the pipeline clean — the core loop of a sales development team.

**Recommended starter stack:** SalesGPT (AI sales agent) + our [AI SDR](../../apps/ai-sdr) flagship for outreach.

## AI-native options

### [SalesGPT](https://github.com/filip-michalsky/SalesGPT)

> Context-aware AI sales agent for voice, email, and chat that advances prospects through configurable sales stages.

| | |
|---|---|
| **Stars** | ~2.7k |
| **Replaces** | Scripted SDR sequences / first-touch sales reps |
| **Self-host** | Medium — Docker Compose or Python, bring your own LLM keys |
| **Ship in** | ~1 hour |
| **Stack** | Python + LangChain / LiteLLM |
| **License** | MIT |

**Why it's on the list:** the sales-stage agent loop, product-knowledge tools, email follow-ups, and meeting/payment handoffs are the core product. It is more of an agent framework than a polished CRM, so pair it with a pipeline system rather than expecting a full sales suite.

### [Veska](https://github.com/arunrajiah/veska)

> AI-native ERP that configures a CRM (plus support, finance, and HR) from a plain-English description of your business, then runs from Slack/WhatsApp/Email. Covers this whole department, not just sales.

| | |
|---|---|
| **Stars** | ~2 (new project) |
| **Replaces** | a full CRM + the rest of the back office, in one deploy |
| **Self-host** | Medium — `docker compose up`, bring your own LLM |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript (Next.js) |
| **License** | Apache-2.0 |

**Why it's on the list:** there isn't yet a strong single-purpose AI-native CRM in this space, so an all-in-one option is worth including. **Disclosure:** built by this repo's maintainer — judge it on the same bar as everything else here. [Go-live guide](../../apps/veska/GO-LIVE.md).

---

Also: our [AI SDR](../../apps/ai-sdr) flagship drafts personalized outreach.

🚀 **Flagship app:** [`apps/ai-sdr`](../../apps/ai-sdr)
🏭 **Industry cross-links:** [Real Estate](../../industries/README.md#real-estate) · [E-commerce](../../industries/README.md#e-commerce--retail)
