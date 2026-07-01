# 🎨 Design & Creative — one-click deploy

The whole creative studio in one command: **ComfyUI** (node-graph image/video
generation) + **Caddy** for automatic HTTPS, running on your own GPU.

```bash
cp .env.example .env      # set DOMAIN and ACME_EMAIL
docker compose up -d
```

👉 **Full walkthrough (GPU setup, domain, DNS, adding models, first render, AI
prompt-expansion): [GO-LIVE.md](GO-LIVE.md)**

| | |
|---|---|
| **Replaces** | a production designer + stock-image spend + per-render SaaS credits |
| **Time to live** | ~30–60 min |
| **Needs** | a GPU VPS (NVIDIA, 8 GB+ VRAM), a domain, Docker |
| **Includes** | ComfyUI, Caddy (HTTPS) |

> ComfyUI ships **no official Docker image**; this stack uses the well-maintained
> community image [`yanwk/comfyui-boot`](https://github.com/YanWenKun/ComfyUI-Docker)
> (verified before shipping). A CPU-only tag exists for trials, but a GPU is
> strongly recommended — see [GO-LIVE.md](GO-LIVE.md).

Want alternatives to any piece? See the [Design directory](../README.md).
