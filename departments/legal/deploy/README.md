# ⚖️ Legal & Compliance — one-click deploy

The core legal department in one command: **AnythingLLM** (private
chat-with-your-contracts Q&A) + **Caddy** for automatic HTTPS.

```bash
cp .env.example .env      # set DOMAIN, ACME_EMAIL, and JWT_SECRET
docker compose up -d
```

👉 **Full walkthrough (domain, DNS, first login, wiring a local/OpenAI-compatible
LLM): [GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | outside-counsel review hours |
| **Time to live** | ~30–60 min |
| **Needs** | a VPS (2 vCPU / 4 GB), a domain, Docker |
| **Includes** | AnythingLLM, Caddy (HTTPS) |

> ⚠️ **Not legal advice.** These tools assist review and signing; a qualified
> lawyer must sign off on anything that matters.

Want alternatives to any piece? See the [Legal directory](../README.md).
