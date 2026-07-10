---
title: Scientific Research & Academia — AI-native open source
description: Open-source AI for research — literature-review agents, autonomous lab agents, and RAG over scientific papers.
sidebar_label: Scientific Research
slug: /industries/scientific-research
keywords: [ai research agent open source, literature review ai, autonomous science agent, rag scientific papers, ai lab assistant]
---

# 🧪 Scientific Research & Academia — AI-native open source

> AI is moving into the research loop itself: agents that read the literature,
> plan and run experiments, reason over chemistry, and draft papers. The projects
> below put an LLM agent or ML model at the *core* of the workflow — not a
> reference manager with autocomplete.

> 📚 **Assistants, not authors.** These tools accelerate literature review,
> hypothesis generation, and analysis — but results still need human validation,
> and journal/venue policies on AI-assisted work vary. Cite your sources and
> disclose your tooling.

### [GPT Researcher](https://github.com/assafelovic/gpt-researcher)

> An autonomous "deep research" agent that plans sub-questions, gathers 20+ sources across web and local docs, and writes a cited, multi-page report — the grunt work of a lit review, automated.

| | |
|---|---|
| **Stars** | ~28k |
| **AI** | planner/executor LLM agents (LangGraph) for multi-source research and synthesis |
| **Replaces** | manual literature scanning; junior research-assistant legwork |
| **Self-host** | Medium — Python; bring your own LLM + search keys |
| **License** | Apache-2.0 |

### [PaperQA2](https://github.com/Future-House/paper-qa)

> High-accuracy RAG over scientific PDFs — asks and answers questions against your paper corpus with grounded, per-claim citations, using an agentic retrieve-and-refine loop.

| | |
|---|---|
| **Stars** | ~8.8k |
| **AI** | agentic RAG: contextual summarization + evidence gathering + cited generation |
| **Replaces** | manual paper skimming; unreliable "chat with PDF" wrappers |
| **Self-host** | Medium — Python; configurable LLM providers via LiteLLM |
| **License** | Apache-2.0 |

### [ChemCrow](https://github.com/ur-whitelab/chemcrow-public)

> An LLM chemistry agent that reasons over reaction-intensive tasks by calling real chemistry tools — RDKit, PubChem, chem-space, and paper-qa — instead of hallucinating structures.

| | |
|---|---|
| **Stars** | ~930 |
| **AI** | LLM agent augmented with chemistry-specific tools for reasoning-heavy tasks |
| **Replaces** | manual lookups across disconnected cheminformatics tools |
| **Self-host** | Medium — Python; bring your own LLM |
| **License** | MIT |

### [scispaCy](https://github.com/allenai/scispacy)

> Allen AI's spaCy pipeline and models tuned for scientific and biomedical text — NER, entity linking to knowledge bases, and abbreviation detection over papers at scale.

| | |
|---|---|
| **Stars** | ~2k |
| **AI** | domain-trained NLP/NER models for scientific and biomedical corpora |
| **Replaces** | generic NLP pipelines that miss biomedical entities and abbreviations |
| **Self-host** | Easy — pip install pretrained models |
| **License** | Apache-2.0 |

---

Honest note: dedicated, well-licensed AI-native OSS for autonomous research is
still thin — several high-profile "AI scientist" projects ship under restrictive
or unspecified licenses, so we left them off. The four above are the ones we could
verify as genuinely open and AI-native: autonomous research (GPT Researcher),
grounded literature Q&A (PaperQA2), domain agents (ChemCrow), and scientific NLP
(scispaCy). See also [Biomni](../healthcare/) for a biomedical research agent.

Related departments: [Product & Research](../../departments/product/) · [Data](../../departments/data/) (analysis pipelines).
🏭 Back to the [industry index](../README.md).
