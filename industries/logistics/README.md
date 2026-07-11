---
title: Logistics & Supply Chain — AI-native open source
description: Open-source AI for supply chain — demand-forecasting models, warehouse vision, and document extraction for invoices and BOLs.
sidebar_label: Logistics
slug: /industries/logistics
keywords: [logistics ai open source, supply chain ai github, demand forecasting open source, warehouse vision ai, ai invoice extraction, multi-agent warehouse ai]
---

# 🚚 Logistics & Supply Chain — AI-native open source

> This is the vertical with the most real AI-native OSS: ML models for demand forecasting, vision models for warehouse and shelf detection, and LLMs that read invoices, BOLs, and customs paperwork.

### [Nixtla (TimeGPT SDK)](https://github.com/Nixtla/nixtla)

> A pre-trained time-series foundation model for demand and inventory forecasting — zero-shot forecasts and anomaly detection from a few lines of code.

| | |
|---|---|
| **Stars** | ~3.9k |
| **AI** | Time-series foundation model (transformer) + open forecasting SDK |
| **Replaces** | manual demand planning, spreadsheet forecasts |
| **Self-host** | Medium (SDK open; also see StatsForecast/MLForecast) |
| **License** | Apache-2.0 (SDK) |

### [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)

> State-of-the-art vision models for warehouse and shelf monitoring — detect, count, and track pallets, cartons, and inventory from camera feeds.

| | |
|---|---|
| **Stars** | ~59k |
| **AI** | Vision ML (detection, segmentation, tracking) |
| **Replaces** | manual stock counts, cycle-count labor |
| **Self-host** | Medium |
| **License** | AGPL-3.0 |

### [Unstract](https://github.com/Zipstack/unstract)

> LLM-driven extraction of structured data from invoices, bills of lading, and customs documents — natural-language prompts to JSON, deployable as an API or ETL step.

| | |
|---|---|
| **Stars** | ~6.7k |
| **AI** | LLM document extraction (Prompt Studio → JSON) |
| **Replaces** | manual invoice/BOL data entry, OCR-and-key teams |
| **Self-host** | Medium |
| **License** | AGPL-3.0 |

### [Sparrow](https://github.com/katanaml/sparrow)

> Document intelligence with ML, LLMs, and Vision LLMs — structured extraction from invoices, statements, and tables plus workflow/decision agents.

| | |
|---|---|
| **Stars** | ~5.2k |
| **AI** | Vision LLM + agent document intelligence |
| **Replaces** | manual document processing, AP data entry |
| **Self-host** | Medium |
| **License** | GPL-3.0 (dual-licensed) |

### [Multi-Agent Intelligent Warehouse](https://github.com/NVIDIA-AI-Blueprints/Multi-Agent-Intelligent-Warehouse)

> A LangGraph-orchestrated multi-agent system for warehouse operations — equipment/asset tracking, operations coordination, safety compliance, forecasting, and document-processing agents coordinating together, not a chatbot bolted onto a WMS.

| | |
|---|---|
| **Stars** | ~101 |
| **AI** | Multi-agent LLM orchestration (LangGraph) + GPU-accelerated forecasting |
| **Replaces** | manual warehouse-ops coordination, siloed WMS dashboards |
| **Self-host** | Hard — Docker/Kubernetes infra is open (Apache-2.0), but the conversational agents need NVIDIA NIM/API keys |
| **License** | Apache-2.0 |

---

> 🚚 This vertical is the least sparse: forecasting (Nixtla), warehouse vision (YOLO), document extraction (Unstract, Sparrow), and now multi-agent warehouse orchestration (Multi-Agent Intelligent Warehouse) are all genuinely AI-native. Note: route optimization is well served by open engines like VROOM, but those are OR/heuristic solvers rather than LLM/ML-model-at-the-core AI, so they're out of scope here.

Related departments: [Data](../../departments/data/) · [Support](../../departments/support/)
