---
title: Game Development — AI-native open source
description: Open-source AI for games — LLM-driven NPCs, embodied learning agents, and multi-agent RL frameworks for training and playtesting.
sidebar_label: Game Dev
slug: /industries/gamedev
keywords: [ai npc open source, generative agents github, game ai open source, llm game agent, reinforcement learning game bots, llm procedural content generation]
---

# 🎮 Game Development — AI-native open source

> AI in games has moved past scripted dialogue trees: open LLM agents now drive
> NPCs that remember and socialize, embodied agents learn to play open worlds
> from scratch, and multi-agent RL frameworks train and playtest bots at scale.
> Every project below puts an LLM agent or ML model at the *core* — not a
> chatbot bolted onto an existing engine.

### [Generative Agents](https://github.com/joonspk-research/generative_agents)

> The Stanford "Smallville" research release: 25 LLM agents that plan their day, remember past events, and form relationships — the reference implementation for believable NPC behavior.

| | |
|---|---|
| **Stars** | ~21.7k |
| **AI** | LLM agents with memory stream, reflection, and planning loops |
| **Replaces** | hand-authored NPC schedules and dialogue trees |
| **Self-host** | Medium — Python; bring your own LLM key |
| **License** | Apache-2.0 |

### [AI Town](https://github.com/a16z-infra/ai-town)

> A deployable starter kit for a virtual town of AI characters that live, chat, and socialize — vector-memory NPCs you can ship, with Ollama/OpenAI-compatible backends.

| | |
|---|---|
| **Stars** | ~10k |
| **AI** | LLM-driven characters + vector-search memory retrieval |
| **Replaces** | bespoke NPC AI backends and dialogue services |
| **Self-host** | Medium — TypeScript + Convex; local or hosted LLM |
| **License** | MIT |

### [Voyager](https://github.com/MineDojo/Voyager)

> An embodied LLM agent that plays Minecraft with continuous learning — an auto-curriculum, a growing skill library of executable code, and iterative prompting driven by environment feedback.

| | |
|---|---|
| **Stars** | ~7k |
| **AI** | LLM agent that writes and reuses skill code from environment feedback |
| **Replaces** | hand-coded game-playing bots and behavior trees |
| **Self-host** | Medium — Python + JS; bring your own LLM key |
| **License** | MIT |

### [MineDojo](https://github.com/MineDojo/MineDojo)

> An open-ended agent-learning platform: 1000s of Minecraft tasks plus an internet-scale knowledge base (730K videos, 7K wiki pages) for training and benchmarking game-playing agents.

| | |
|---|---|
| **Stars** | ~2.2k |
| **AI** | multimodal foundation-model training environment for embodied agents |
| **Replaces** | bespoke game-AI training harnesses and eval suites |
| **Self-host** | Medium — Python simulation suite |
| **License** | MIT |

### [PettingZoo](https://github.com/Farama-Foundation/PettingZoo)

> The multi-agent counterpart to Gymnasium — a standard API and environment library (Atari, board/card games, cooperative worlds) for training and playtesting game bots with reinforcement learning.

| | |
|---|---|
| **Stars** | ~3.5k |
| **AI** | multi-agent RL environments + standardized training API |
| **Replaces** | ad-hoc self-play harnesses; manual QA playtesting |
| **Self-host** | Easy — pip-installable Python library |
| **License** | MIT OR Apache-2.0 |

### [Interactive LLM-Powered NPCs](https://github.com/AkshitIreddy/Interactive-LLM-Powered-NPCs)

> Drops talking, emoting NPCs into existing games (e.g. Cyberpunk 2077) — LLM dialogue plus speech recognition, facial animation, and emotion/face detection wired together.

| | |
|---|---|
| **Stars** | ~715 |
| **AI** | LLM dialogue + speech-to-text + emotion detection + facial animation |
| **Replaces** | pre-recorded voice lines and static NPC scripts |
| **Self-host** | Hard — multi-model pipeline with heavy dependencies |
| **License** | MIT |

### [Cradle](https://github.com/BAAI-Agents/Cradle)

> A general computer-control agent that plays games the way a human would — screenshot in, keyboard/mouse action out, with no game-specific API required.

| | |
|---|---|
| **Stars** | ~2.6k |
| **AI** | vision-language foundation-model agent mapping raw screenshots to keyboard/mouse actions |
| **Replaces** | hand-coded game bots and API-based playtesting harnesses |
| **Self-host** | Medium — Python; bring your own vision-language model |
| **License** | MIT |

### [MarioGPT](https://github.com/shyamsn97/mario-gpt)

> A fine-tuned GPT-2 language model that generates playable Super Mario levels from text prompts — a reference implementation for LLM-driven procedural content generation.

| | |
|---|---|
| **Stars** | ~1.1k |
| **AI** | fine-tuned transformer language model generating level tokens from text conditioning |
| **Replaces** | hand-authored level design; rule-based PCG algorithms |
| **Self-host** | Easy — Python; pretrained checkpoints included |
| **License** | MIT |

---

Game dev has real AI-native depth: believable NPCs (Generative Agents, AI Town,
Interactive NPCs), embodied learning agents (Voyager, MineDojo, Cradle), RL
training/playtesting (PettingZoo), and LLM-driven procedural content generation
(MarioGPT).

Related departments: [Engineering](../../departments/engineering/) · [Design](../../departments/design/) (asset and content generation).
🏭 Back to the [industry index](../README.md).
