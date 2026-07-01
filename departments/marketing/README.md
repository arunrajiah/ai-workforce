# 📣 Marketing & Growth

> Replace: a content marketer + a social-media manager + an email-marketing manager + a growth analyst.

Content generation, SEO research, social scheduling, email campaigns, and product
analytics can all run on open-source infrastructure. Add an LLM content agent on
top and one person can run the output of a whole marketing team.

**Recommended starter stack:** Dify (content/SEO agents) + listmonk (email) + Postiz (social) + PostHog (analytics). Firecrawl for competitor/SEO research.

---

### [Dify](https://github.com/langgenius/dify)

> Production platform for building AI apps/agents with RAG — ideal for ad-copy, blog, and SEO agents.

| | |
|---|---|
| **Stars** | ~147k |
| **Replaces** | a content marketer + Jasper/Copy.ai |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | TypeScript + Python |
| **License** | Dify Open Source License (Apache-based) |

**Why it's on the list:** build a branded content pipeline with prompts, knowledge, and review steps — no code.

### [Postiz](https://github.com/gitroomhq/postiz-app)

> Agentic social-media scheduling and analytics across X, LinkedIn, Instagram, TikTok, and more.

| | |
|---|---|
| **Stars** | ~33k |
| **Replaces** | a social-media manager + Buffer/Hootsuite |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~30 min |
| **Stack** | TypeScript (Next.js + NestJS) |
| **License** | AGPL-3.0 |

**Why it's on the list:** AI-assisted, multi-channel scheduling that actually looks modern. The social team in a box.

### [listmonk](https://github.com/knadh/listmonk)

> High-performance newsletter and mailing-list manager — a single binary with a clean dashboard.

| | |
|---|---|
| **Stars** | ~22k |
| **Replaces** | an email-marketing manager + Mailchimp |
| **Self-host** | Easy — single binary or compose |
| **Ship in** | ~30 min |
| **Stack** | Go (+ Vue) |
| **License** | AGPL-3.0 |

**Why it's on the list:** blisteringly fast, cheap to run at scale, great API for LLM-generated campaigns.

### [Mautic](https://github.com/mautic/mautic)

> The largest open-source marketing-automation platform: campaigns, email, segmentation, multi-channel.

| | |
|---|---|
| **Stars** | ~10k |
| **Replaces** | a marketing-automation manager + HubSpot/Marketo |
| **Self-host** | Medium — LAMP stack |
| **Ship in** | 1–2 hours |
| **Stack** | PHP (Symfony) |
| **License** | GPL-3.0 |

**Why it's on the list:** full lifecycle automation and lead scoring when you've outgrown a newsletter tool.

### [PostHog](https://github.com/PostHog/posthog)

> All-in-one product & web analytics, session replay, feature flags, experiments, surveys + AI assistant.

| | |
|---|---|
| **Stars** | ~35k |
| **Replaces** | a growth/analytics role + Amplitude/Mixpanel |
| **Self-host** | Medium — heavier stack (ClickHouse) |
| **Ship in** | 1–2 hours |
| **Stack** | Python + TypeScript |
| **License** | MIT (FOSS build available) |

**Why it's on the list:** the growth team's instrument panel; its AI assistant answers analytics questions directly.

### [Activepieces](https://github.com/activepieces/activepieces)

> Open-source Zapier alternative with AI agents/MCP — automate email, social, and publishing.

| | |
|---|---|
| **Stars** | ~23k |
| **Replaces** | a marketing-ops role + Zapier/Make |
| **Self-host** | Easy — `docker compose up` |
| **Ship in** | ~20 min |
| **Stack** | TypeScript |
| **License** | MIT (+ enterprise) |

**Why it's on the list:** MIT-licensed automation with first-class AI steps — the glue for campaign ops.

### [Firecrawl](https://github.com/mendableai/firecrawl)

> Bulk site scraping/extraction for SEO audits, competitor content, and AI content pipelines.

| | |
|---|---|
| **Stars** | ~142k |
| **Replaces** | an SEO analyst's crawls + ScreamingFrog/Ahrefs |
| **Self-host** | Medium — compose |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript |
| **License** | AGPL-3.0 |

**Why it's on the list:** SEO and content agents need clean web data. This is the best open way to get it.

---

📘 **Deploy guide:** [Ship a content + SEO engine](../../docs/departments/marketing.mdx)
🏭 **Industry cross-links:** [E-commerce](../../industries/README.md#e-commerce--retail) · [Education](../../industries/README.md#education)
