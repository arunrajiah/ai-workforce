# 🎨 Design & Creative

> Replace: a production designer + stock-image spend + a headshot service + Figma seats.

Generative image/video pipelines produce marketing creative, product shots, and
brand assets on demand; open design platforms replace per-seat SaaS. Most of
these run locally on a GPU, so the marginal cost of a thousand assets is near zero.

## ⚡ One-click deploy (recommended)

**Run the entire design studio with one command** — ComfyUI (node-graph image/video
generation) + Caddy for automatic HTTPS, pre-wired together on your own GPU server.

```bash
git clone https://github.com/arunrajiah/ai-workforce.git
cd ai-workforce/departments/design/deploy
cp .env.example .env      # set DOMAIN and ACME_EMAIL
docker compose up -d
```

👉 **Full go-live walkthrough (GPU + NVIDIA toolkit, DNS, HTTPS, adding models,
first render, AI prompt-expansion): [deploy/GO-LIVE.md](deploy/GO-LIVE.md)** — live
on your domain in ~30–60 min. A GPU (NVIDIA + nvidia-container-toolkit) is strongly
recommended; a CPU-only mode exists for trials but is very slow.

---

## 🧩 Swap a component

The one-click stack above is the fast path. Prefer to assemble your own? Every
piece below is a strong, self-hostable, AI-native option — the **recommended starter stack**
is ComfyUI (programmable generation pipeline) or AUTOMATIC1111 (approachable UI)
for assets. A GPU is recommended for generation tools.

---

### [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

> The most powerful modular node-graph GUI/API/backend for diffusion models (image, video, 3D, audio).

| | |
|---|---|
| **Stars** | ~119k |
| **Replaces** | a creative/visual production designer; a generative-art pipeline |
| **Self-host** | Easy–Medium — portable package; GPU recommended |
| **Ship in** | ~1 hour (2–4h with custom models) |
| **Stack** | Python + PyTorch |
| **License** | GPL-3.0 |

**Why it's on the list:** the professional's choice. Build a repeatable, API-driven asset pipeline as a node graph.

### [Stable Diffusion web UI (AUTOMATIC1111)](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

> Feature-rich web interface for Stable Diffusion image generation.

| | |
|---|---|
| **Stars** | ~164k |
| **Replaces** | marketing/creative image production; stock-image spend |
| **Self-host** | Easy — one-click install scripts; GPU recommended |
| **Ship in** | ~1 hour |
| **Stack** | Python (Gradio) |
| **License** | AGPL-3.0 |

**Why it's on the list:** the most popular entry point to local image generation. Approachable, huge ecosystem.

### [InvokeAI](https://github.com/invoke-ai/InvokeAI)

> Professional creative engine for Stable Diffusion with a polished web UI and workflows.

| | |
|---|---|
| **Stars** | ~28k |
| **Replaces** | a brand/creative asset designer |
| **Self-host** | Easy — official Launcher or Docker |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript + Python |
| **License** | Apache-2.0 (model licenses apply) |

**Why it's on the list:** the most "designed" of the generation UIs — good for teams that want structure over knobs.

### [HivisionIDPhotos](https://github.com/Zeyi-Lin/HivisionIDPhotos)

> Auto-generates standardized ID/portrait photos (segmentation, background swap, sizing).

| | |
|---|---|
| **Stars** | ~21k |
| **Replaces** | a photo-retouch/headshot service |
| **Self-host** | Easy — compose (Gradio UI + API) |
| **Ship in** | ~1 hour |
| **Stack** | Python (Gradio + FastAPI) |
| **License** | Apache-2.0 |

**Why it's on the list:** a narrow but genuinely useful task fully automated — team headshots and ID photos on demand.

### [StableStudio](https://github.com/Stability-AI/StableStudio)

> Stability AI's open-source DreamStudio UI — a pluggable image generate/edit front-end.

| | |
|---|---|
| **Stars** | ~9k |
| **Replaces** | a front-end for a creative image-gen studio |
| **Self-host** | Easy — clone + `yarn dev` |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript / Node |
| **License** | MIT |

**Why it's on the list:** MIT-licensed, swappable-backend studio UI. A clean base to build a branded creative tool on. Less actively maintained.

---

