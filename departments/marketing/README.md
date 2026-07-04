# 📣 Marketing & Growth

> Replace: a content marketer + a social-media manager + an email-marketing manager + a growth analyst.

Content generation, SEO research, social scheduling, email campaigns, and product
analytics can all run on open-source infrastructure. Add an LLM content agent on
top and one person can run the output of a whole marketing team.

## ⚡ One-click deploy (recommended)

**Run an AI content/agent platform with one command** — [Dify](https://github.com/langgenius/dify)
(open-source LLM app & agent platform: build ad-copy, blog, and SEO agents with RAG)
behind Caddy for automatic HTTPS.

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
```

Then layer HTTPS + your domain on top with the Caddy overlay in
[`deploy/`](deploy/):

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/marketing/deploy
cp .env.example .env      # set DOMAIN and ACME_EMAIL
docker compose --env-file .env -f caddy-compose.yml up -d
```

👉 **Full go-live walkthrough (server, DNS, HTTPS overlay, first-run setup, wiring
your LLM): [deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live on your domain in
~30–60 min.

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable, AI-native option — the "recommended
starter stack" is Dify (content/SEO agents) + Activepieces (AI-first campaign automation).

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

---

🏭 **Industry cross-links:** [E-commerce](../../industries/README.md#e-commerce--retail) · [Education](../../industries/README.md#education)
