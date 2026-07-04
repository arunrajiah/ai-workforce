---
title: Go live — Design & Creative in one command
description: Deploy a self-hosted generative-image studio (ComfyUI) with HTTPS on your own GPU server in under an hour.
sidebar_label: Design — Go Live
slug: /departments/design/deploy
keywords: [comfyui self-host, generative image pipeline, ai design studio docker, one click deploy]
---

# 🎨 Design & Creative — go live in one command

This stack **is** a creative studio:

```
                         ┌──────────────── Caddy (auto-HTTPS) ────────────────┐
   designers ──────────▶ │  https://studio.yourdomain.com                     │
   (browser / API)                            │                               │
                         └───────────────────┼───────────────────────────────┘
                                             ▼
                                    ComfyUI (node-graph generation)
                                     │            ▲
                        /prompt API  │            │  rendered assets
                                     ▼            │
                              NVIDIA GPU  ·  ./storage (models, outputs)
```

You get a programmable, API-driven image/video generation pipeline — behind real
HTTPS on your domain, running on your own hardware.

- **Replaces:** a production designer + stock-image spend + per-render SaaS credits
- **Time to live:** ~30–60 minutes (longer if you download large models)
- **You need:** a server with an **NVIDIA GPU**, a public IP, a domain, and Docker

> **A note on the image.** ComfyUI ships **no official Docker image**. This stack
> uses [`yanwk/comfyui-boot`](https://github.com/YanWenKun/ComfyUI-Docker) — a
> well-maintained community image (~1.6k★, releases through 2025, active commits).
> A solid alternative is [`ghcr.io/ai-dock/comfyui`](https://github.com/ai-dock/comfyui);
> swap `COMFYUI_IMAGE` in `.env` if you prefer it. Both were verified before shipping;
> neither is published by the ComfyUI project itself.

---

## Step 1 — Get a GPU server

ComfyUI is a diffusion-model engine: a **GPU is strongly recommended**. Any Ubuntu
22.04+ host with an **NVIDIA GPU (8 GB+ VRAM)** works — a GPU VPS from Lambda,
RunPod, Vast.ai, Hetzner GEX, or a cloud `g5`/`A10`/`RTX` instance. SSH in, then
install Docker:

```bash
curl -fsSL https://get.docker.com | sh
```

Open ports **80** and **443** in your provider's firewall.

> **CPU-only caveat.** You *can* run without a GPU by setting
> `COMFYUI_IMAGE=yanwk/comfyui-boot:cpu` and commenting out the `deploy:` block in
> `docker-compose.yml` — but renders will be **extremely slow** (minutes to tens of
> minutes per image). Fine for kicking the tires; not for real work.

## Step 2 — Install the NVIDIA container toolkit

Docker needs the NVIDIA runtime to hand the GPU to the container:

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \
  | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
  | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
  | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker && sudo systemctl restart docker
```

Verify the GPU is visible to Docker:

```bash
docker run --rm --gpus all nvidia/cuda:12.6.0-base-ubuntu22.04 nvidia-smi
```

You should see your GPU listed. (Skip this whole step for a CPU-only trial.)

## Step 3 — Point your domain at it

Create a DNS **A record** for `studio.yourdomain.com` → your server's IP.
Verify it resolves before continuing (HTTPS issuance depends on it):

```bash
dig +short studio.yourdomain.com   # should print your server IP
```

## Step 4 — Get the stack

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/design/deploy
cp .env.example .env
```

## Step 5 — Fill in `.env`

In `.env`, set at minimum:

- `DOMAIN` → `studio.yourdomain.com`
- `ACME_EMAIL` → your email (for Let's Encrypt)
- `COMFYUI_IMAGE` → leave the default GPU image, or pick the CPU tag for a trial

## Step 6 — Launch

```bash
docker compose up -d
```

Caddy will fetch a TLS certificate automatically. The ComfyUI image is large
(several GB) and pulls on first run, so give it a few minutes. Then open
**https://studio.yourdomain.com** — the node-graph editor loads in your browser.

> Watch it come up: `docker compose logs -f comfyui caddy`

## Step 7 — Add models

ComfyUI needs at least one checkpoint to generate. The `./storage` folder is
mounted into the container, so drop model files on the host and they appear inside:

```bash
# from the deploy/ folder — put a checkpoint where ComfyUI expects it
mkdir -p storage/ComfyUI/models/checkpoints
cd storage/ComfyUI/models/checkpoints
# e.g. an SDXL / SD1.5 checkpoint from Hugging Face or Civitai
wget <URL-to-a-.safetensors-checkpoint>
```

Reload the ComfyUI tab — the checkpoint appears in the **Load Checkpoint** node.
Drop LoRAs, VAEs, and ControlNets under the matching `storage/ComfyUI/models/*`
folders the same way.

## Step 8 — Render your first asset

In the browser: load the default workflow, pick your checkpoint in **Load
Checkpoint**, type a prompt, and hit **Queue Prompt**. Rendered images land in
`storage/ComfyUI/output/` on the host as well as in the UI.

You're live. 🎉

---

## Optional — AI prompt-expansion (brief → prompt → render)

ComfyUI exposes a **`/prompt` HTTP API**, so you can drive it from an automation
tool. A simple, provider-neutral pattern:

1. From a small script or automation step, take a short creative brief.
2. Build a flow: **a short brief** → **HTTP Request to an
   OpenAI-compatible endpoint** (set `LLM_BASE_URL` / `LLM_MODEL` / `LLM_API_KEY`
   in that flow) that expands the brief into a rich, detailed prompt.
3. Inject the expanded text into a ComfyUI workflow JSON and **POST it to
   `http://comfyui:8188/prompt`** (inside the Docker network) or
   `https://studio.yourdomain.com/prompt` from outside.
4. Poll `/history/<prompt_id>` for the finished image.

Any OpenAI-compatible model works (a local Ollama server, a hosted gateway, etc.) —
the studio stays vendor-neutral.

## Operate it

| Task | Command |
|---|---|
| View logs | `docker compose logs -f comfyui caddy` |
| Confirm the GPU is in use | `docker compose exec comfyui nvidia-smi` |
| Update ComfyUI | `docker compose pull && docker compose up -d` |
| Back up models & outputs | `tar czf studio-backup.tgz storage/` |
| Stop everything | `docker compose down` (your `storage/` folder persists) |

## Troubleshooting

- **No HTTPS certificate** — DNS isn't pointing at the server yet, or ports 80/443 are blocked. Check `docker compose logs caddy`.
- **CUDA / GPU not found** — Step 2 didn't finish. Re-run the `nvidia-smi` container test; if it fails, reinstall the toolkit and `systemctl restart docker`.
- **502 / blank page** — the image is still pulling or ComfyUI is booting. Watch `docker compose logs -f comfyui`; first start can take several minutes.
- **"No checkpoints" in the UI** — you haven't added a model yet. See Step 7; files go under `storage/ComfyUI/models/checkpoints/`.
- **Out-of-memory during a render** — the checkpoint is too large for your VRAM. Use a smaller model (SD1.5), lower the resolution/batch size, or add `--lowvram` support via the image's env options.

## Swap a component

Prefer a different generation engine or a lighter footprint? Every piece is
replaceable — see the [Design & Creative directory](../README.md) for alternatives
(AUTOMATIC1111, InvokeAI, HivisionIDPhotos, StableStudio).
