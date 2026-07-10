---
title: Healthcare — AI-native open source
description: Open-source medical AI — imaging models, clinical LLMs, AI scribes, and biomedical research agents you can self-host.
sidebar_label: Healthcare
slug: /industries/healthcare
keywords: [healthcare ai open source, medical imaging ai github, ai scribe open source, clinical llm, biomedical ai agent]
---

# 🏥 Healthcare — AI-native open source

> AI in healthcare has moved past chatbots: open models now read scans, reason
> over patient records, draft clinical notes from a conversation, and run
> autonomous biomedical research. The projects below put an ML model or LLM agent
> at the *core* of the tool — not a wrapper around an EHR.

> ⚕️ **Regulated data.** Everything here is self-hostable so PHI stays on your own
> infra. None of it is a medical device or a substitute for a clinician — get
> compliance and clinical sign-off before anything touches a patient.

### [MONAI](https://github.com/Project-MONAI/MONAI)

> PyTorch-native deep-learning framework for medical imaging — the model *is* the product: segmentation, detection, and classification over radiology and pathology.

| | |
|---|---|
| **Stars** | ~8.4k |
| **AI** | domain-optimized deep-learning models + training workflows for 2D/3D medical images |
| **Replaces** | proprietary imaging-AI toolchains; bespoke research pipelines |
| **Self-host** | Medium — Python + GPU |
| **License** | Apache-2.0 |

### [Biomni](https://github.com/snap-stanford/Biomni)

> A general-purpose biomedical AI agent (Stanford SNAP Lab) that plans, retrieves, and writes/executes code to run research tasks autonomously.

| | |
|---|---|
| **Stars** | ~3.3k |
| **AI** | LLM-agent reasoning + retrieval-augmented planning + code execution over biomedical tools |
| **Replaces** | manual research-analyst / bioinformatics legwork |
| **Self-host** | Medium — Python; bring your own LLM |
| **License** | Apache-2.0 |

### [Meditron](https://github.com/epfLLM/meditron)

> An open suite of medical LLMs (7B/70B) pretrained on PubMed, clinical guidelines, and medical corpora — a domain model, not a prompt template.

| | |
|---|---|
| **Stars** | ~2.2k |
| **AI** | medical-domain LLM for clinical reasoning and guideline-grounded Q&A |
| **Replaces** | general-purpose LLMs for medical reasoning tasks |
| **Self-host** | Hard — large-model inference / GPU |
| **License** | Apache-2.0 (code); Llama-2 community license (weights) |

### [MONAI Label](https://github.com/Project-MONAI/MONAILabel)

> AI-assisted image labeling — an interactive server that learns from clinician corrections to auto-segment radiology, pathology, and endoscopy images.

| | |
|---|---|
| **Stars** | ~850 |
| **AI** | active-learning segmentation models in the annotation loop |
| **Replaces** | manual slice-by-slice annotation labor |
| **Self-host** | Medium — Python + viewer integration |
| **License** | Apache-2.0 |

### [Phlox](https://github.com/bloodworks-io/phlox)

> Local-first AI medical scribe — transcribes the encounter, generates the clinical note, and adds RAG + agentic tool-calling, all runnable offline via Ollama.

| | |
|---|---|
| **Stars** | ~90 |
| **AI** | speech-to-text + LLM note generation + RAG over your knowledge base |
| **Replaces** | ambient-scribe SaaS (Nuance DAX-style tools) |
| **Self-host** | Medium — local LLM + transcription |
| **License** | MIT |

### [OpenScribe](https://github.com/sammargolis/OpenScribe)

> Open ambient scribe that records a patient encounter and drafts structured clinical notes; provider-configurable LLM, local-first by default.

| | |
|---|---|
| **Stars** | ~190 |
| **AI** | Whisper transcription + LLM-generated structured notes (SOAP) |
| **Replaces** | commercial medical-scribe subscriptions |
| **Self-host** | Medium — configurable local/cloud models |
| **License** | MIT |

---

Healthcare has real AI-native depth: imaging (MONAI), domain LLMs (Meditron),
research agents (Biomni), and ambient documentation (Phlox, OpenScribe). The
scribe tools are young and low-star — pilot carefully.

Related departments: [Support](../../departments/support/) (private RAG over protocols) · [Data](../../departments/data/) (analytics on clinical data).
🏭 Back to the [industry index](../README.md).
