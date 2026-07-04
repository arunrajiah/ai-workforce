# 🤖 Robotics & Manufacturing — AI-native open source

> Robotics has shifted from hand-tuned controllers to *learned* policies: open
> vision-language-action models let robots follow natural-language commands,
> imitation-learning frameworks turn demonstrations into skills, and vision
> models catch defects on the line. Every project below puts an ML model or
> policy network at the *core* — not classical middleware.

### [LeRobot](https://github.com/huggingface/lerobot)

> The de-facto open robot-learning stack: PyTorch models, datasets, and tools for real-world robots — imitation learning, RL, and vision-language-action policies with shared dataset formats.

| | |
|---|---|
| **Stars** | ~25.5k |
| **AI** | imitation-learning, RL, and VLA policies + standardized robot datasets |
| **Replaces** | bespoke per-robot control code and data pipelines |
| **Self-host** | Medium — Python + PyTorch; hardware optional |
| **License** | Apache-2.0 |

### [OpenVLA](https://github.com/openvla/openvla)

> An open vision-language-action model for generalist manipulation — take an image plus a language instruction and predict robot actions, fine-tunable to your own arm.

| | |
|---|---|
| **Stars** | ~6.6k |
| **AI** | 7B vision-language-action model for language-conditioned manipulation |
| **Replaces** | task-specific motion scripting and teach-pendant programming |
| **Self-host** | Hard — GPU for training/inference |
| **License** | MIT (code); Llama-2 community license (weights) |

### [Isaac GR00T](https://github.com/NVIDIA/Isaac-GR00T)

> A vision-language-action foundation model for generalist humanoid robots — multimodal (language + images) control across embodiments, with zero-shot inference and fine-tuning.

| | |
|---|---|
| **Stars** | ~7.5k |
| **AI** | cross-embodiment VLA foundation model for humanoid manipulation |
| **Replaces** | per-robot policy engineering and custom control stacks |
| **Self-host** | Hard — GPU; simulation + real-robot deployment |
| **License** | Apache-2.0 (code); NVIDIA Open Model License (weights) |

### [Diffusion Policy](https://github.com/real-stanford/diffusion_policy)

> Visuomotor imitation learning via action diffusion (RSS 2023) — learn manipulation policies from demonstrations, in sim and on real arms, from state or vision inputs.

| | |
|---|---|
| **Stars** | ~4.3k |
| **AI** | diffusion-model policies that predict robot action sequences from demos |
| **Replaces** | hand-tuned motion planners for contact-rich manipulation |
| **Self-host** | Medium — Python + PyTorch; GPU recommended |
| **License** | MIT |

### [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)

> The workhorse real-time vision framework — detection, segmentation, and classification models that power defect detection and quality inspection on the manufacturing line.

| | |
|---|---|
| **Stars** | ~59k |
| **AI** | real-time object-detection / segmentation CNNs (YOLO11, YOLOv8) |
| **Replaces** | manual visual QC; proprietary machine-vision inspection systems |
| **Self-host** | Easy — pip install; runs on edge or GPU |
| **License** | AGPL-3.0 (or commercial) |

### [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)

> Reliable PyTorch reinforcement-learning implementations widely used to train robot control and manipulation policies in simulation before sim-to-real transfer.

| | |
|---|---|
| **Stars** | ~13.5k |
| **AI** | reference RL algorithms (PPO, SAC, TD3) for policy training |
| **Replaces** | from-scratch RL implementations for robot control research |
| **Self-host** | Easy — pip-installable Python library |
| **License** | MIT |

---

Robotics has genuine AI-native depth: robot-learning stacks (LeRobot),
vision-language-action models (OpenVLA, Isaac GR00T), imitation learning
(Diffusion Policy), factory-floor vision (Ultralytics YOLO), and RL training
(Stable-Baselines3). Note that some VLA *model weights* carry
source-available (not fully open) licenses even where the code is Apache/MIT.

For general back-office ops, see [Veska](../../apps/veska/).

Related departments: [Engineering](../../departments/engineering/) · [Data](../../departments/data/) (sensor and telemetry analytics).
🏭 Back to the [industry index](../README.md).
