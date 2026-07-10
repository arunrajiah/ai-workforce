---
title: Film & Video Production — AI-native open source
description: Open-source AI video generation, upscaling, and frame interpolation — self-hosted alternatives to Runway, Pika, and Topaz Video AI.
sidebar_label: Film & Video
slug: /industries/film
keywords: [ai video generator open source, open source runway alternative, ai video upscaler, frame interpolation ai github, text to video open source]
---

# 🎥 Film & Video Production — AI-native open source

> Searching for an open-source Runway or Pika alternative, an AI video
> generator you can self-host, a GitHub project for frame interpolation, or
> an AI video upscaler that doesn't require a subscription? This page rounds
> up the open-source models that put generative AI at the center of the film
> and video pipeline — text-to-video generation, super-resolution upscaling,
> and AI-driven slow-motion/frame interpolation — the building blocks
> production and VFX teams use instead of closed, metered SaaS tools.

### [HunyuanVideo](https://github.com/Tencent/HunyuanVideo)

> A 13B-parameter open text-to-video foundation model from Tencent — turn a text prompt into a video clip, the open-source answer to "AI video generator" searches that usually lead to Runway or Pika.

| | |
|---|---|
| **Stars** | ~12.3k |
| **AI** | Diffusion transformer text-to-video generation model, 13B params |
| **Replaces** | Runway / Pika text-to-video subscriptions |
| **Self-host** | Hard — multi-GPU recommended for full model, FP8 mode for less |
| **License** | Tencent Hunyuan Community License (source-available) |

---

### [Wan2.1](https://github.com/Wan-Video/Wan2.1)

> Alibaba's open video foundation suite covering text-to-video, image-to-video, video editing, and video-to-audio — notable for running its smaller variant on consumer-grade GPUs instead of a render farm.

| | |
|---|---|
| **Stars** | ~16.5k |
| **AI** | Video foundation models (diffusion) for T2V, I2V, editing, and V2A |
| **Replaces** | paid AI video-generation APIs |
| **Self-host** | Medium — 1.3B variant runs on ~8GB VRAM; 14B variant needs a real GPU |
| **License** | Apache-2.0 |

---

### [CogVideoX](https://github.com/THUDM/CogVideo)

> THUDM's text-and-image-to-video model family (2B/5B), one of the earliest credible open alternatives to closed video-generation APIs and still actively developed.

| | |
|---|---|
| **Stars** | ~12.8k |
| **AI** | Diffusion transformer for text-to-video, image-to-video, and video continuation |
| **Replaces** | hosted text-to-video generation APIs |
| **Self-host** | Medium — 2B model fits smaller GPUs; 5B needs more VRAM |
| **License** | Apache-2.0 (code + 2B model); CogVideoX license for the 5B weights |

---

### [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN)

> A super-resolution model trained on purely synthetic degradations — the go-to answer for "AI video upscaler open source," restoring low-res footage, old masters, and anime without a cloud upscaling service.

| | |
|---|---|
| **Stars** | ~36k |
| **AI** | Real-world super-resolution GAN, with dedicated anime and video models |
| **Replaces** | paid video/image upscaling services |
| **Self-host** | Easy — pretrained weights, runs on modest GPUs or CPU (slower) |
| **License** | BSD-3-Clause |

---

### [Practical-RIFE](https://github.com/hzwer/Practical-RIFE)

> A production-tuned build of RIFE, the real-time intermediate flow estimation model — generates in-between frames for slow-motion and frame-rate conversion, the standard hit for "frame interpolation AI github" searches.

| | |
|---|---|
| **Stars** | ~1k |
| **AI** | Optical-flow-based deep learning model for video frame interpolation |
| **Replaces** | Topaz Video AI / paid frame-interpolation plugins |
| **Self-host** | Easy — single GPU, real-time on modest hardware |
| **License** | MIT |

---

### [AnimateDiff](https://github.com/guoyww/AnimateDiff)

> A motion module that turns existing Stable Diffusion checkpoints into animation generators without retraining — a lightweight route to AI-stylized animation and motion graphics.

| | |
|---|---|
| **Stars** | ~12.2k |
| **AI** | Plug-in motion module adding temporal coherence to image diffusion models |
| **Replaces** | paid AI animation/motion-graphics tools |
| **Self-host** | Medium — needs a compatible Stable Diffusion setup + GPU |
| **License** | Apache-2.0 |

---

### [Video2X](https://github.com/k4yt3x/video2x)

> A full upscaling-and-interpolation framework that wraps Real-ESRGAN, Real-CUGAN, and RIFE behind one GPU-accelerated pipeline — for teams who want the "restore and smooth this footage" workflow pre-built rather than wiring models together themselves.

| | |
|---|---|
| **Stars** | ~20.4k |
| **AI** | Real-ESRGAN/Real-CUGAN upscaling + RIFE frame interpolation, Vulkan-accelerated |
| **Replaces** | Topaz Video AI / paid video-restoration software |
| **Self-host** | Medium — cross-vendor GPU support via Vulkan |
| **License** | AGPL-3.0 |

---

Text-to-video generation is the most active area here, but it's also the most
GPU-hungry — expect to need real hardware or a rented GPU for HunyuanVideo,
Wan2.1, or CogVideoX. Upscaling (Real-ESRGAN) and interpolation
(Practical-RIFE) are far cheaper to self-host and are the more practical
starting point for restoring or smoothing existing footage.

For broader generative-media tools — ComfyUI's node-based diffusion workflows,
Whisper for transcription/subtitles, plus the video models Open-Sora and
LTX-Video — see the [Media & Creative](../media/README.md) industry page.
Related department: [Design](../../departments/design/).

🏭 Back to the [industry index](../README.md).
