# 🌾 Agriculture & AgTech — AI-native open source

> Farming is one of the most *computer-vision- and forecasting-native* verticals:
> spot crop disease and pests from imagery, fuse satellite/drone/weather data for
> field insights, and forecast yield and demand. Dedicated end-to-end AgTech
> products are thin in OSS, but the underlying **AI models and platforms are
> strong** — here are the ones worth building on.

### [FarmVibes.AI](https://github.com/microsoft/farmvibes-ai)

> Microsoft's geospatial-ML platform for agriculture — fuse satellite imagery,
> drone data, and weather into models for soil, crop, and sustainability insights.

| | |
|---|---|
| **Stars** | ~880 |
| **AI** | Geospatial ML workflows: data fusion, model training, inference |
| **Replaces** | bespoke precision-ag data pipelines; parts of Climate FieldView / agronomy SaaS |
| **Self-host** | Medium — local cluster |
| **License** | MIT |

**Why it's here:** the most complete open platform purpose-built for agricultural ML — the base for real precision-ag insight, not a demo.

### [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)

> State-of-the-art vision models for detection, segmentation, and tracking — crop/pest/weed detection, fruit counting, livestock monitoring.

| | |
|---|---|
| **Stars** | ~59k |
| **AI** | Deep-learning object detection / segmentation / tracking |
| **Replaces** | manual field scouting; per-plant inspection |
| **Self-host** | Easy — pip / Docker (GPU helps) |
| **License** | AGPL-3.0 (commercial license available) |

**Why it's here:** the workhorse for agricultural computer vision — train it on crop imagery to flag disease, pests, and yield at scale. Note the AGPL copyleft for commercial embedding.

### [Nixtla](https://github.com/Nixtla/nixtla)

> A time-series foundation model + open forecasting SDK — yield, weather-driven demand, and inventory forecasting.

| | |
|---|---|
| **Stars** | ~3.9k |
| **AI** | Foundation-model + statistical/neural time-series forecasting |
| **Replaces** | a demand/yield forecasting analyst; planning-SaaS forecast modules |
| **Self-host** | Easy — pip SDK |
| **License** | Apache-2.0 |

**Why it's here:** forecasting is central to planning harvests and supply; this is the strongest open forecasting stack.

---

**Honest note:** crop-disease detection exists mostly as small CNN projects trained on
the open [PlantVillage dataset](https://github.com/spMohanty/PlantVillage-Dataset)
(~54k labeled leaf images across 14 crops / 26 diseases) rather than as packaged
products — a great base to fine-tune YOLO or a classifier on. Dedicated turnkey AgTech
AI OSS is a real gap; contributions welcome.

Related departments: [Data & Analytics](../../departments/data/) · [Design](../../departments/design/)
