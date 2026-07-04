# 🎵 Music & Audio Production — AI-native open source

> "Open source Suno alternative," "AI music generator open source," "AI voice
> cloning open source," "stem separation AI GitHub," "text to speech open
> source" — music is one of the few creative domains where the whole
> pipeline is now covered by self-hostable models: text-to-song generation,
> singing voice conversion, and audio-to-MIDI transcription all run on your
> own GPU instead of a subscription. The projects below put a generative or
> transcription model at the *core*, not a plugin wrapped around a DAW.

> 🎙️ **A note on voice tools.** RVC and OpenVoice can clone or convert a
> singing/speaking voice from a short sample. Use them on your own voice,
> material you have rights to, or performers who've given consent — covers,
> dubbing your own work, and VTubing are the intended use, not impersonating
> people who haven't agreed to it.

### [AudioCraft (MusicGen / AudioGen)](https://github.com/facebookresearch/audiocraft)

> A text-and-melody-conditioned music and sound generation library — the model behind "type a genre and mood, get a full instrumental," replacing a Suno/Udio subscription for instrumental beds and sound design.

| | |
|---|---|
| **Stars** | ~23.4k |
| **AI** | Transformer language model over neural audio codecs (EnCodec), text + melody conditioning |
| **Replaces** | Suno/Udio subscription for instrumental tracks; stock production-music licensing |
| **Self-host** | Medium — GPU recommended, PyTorch |
| **License** | MIT (code); CC-BY-NC 4.0 (pretrained weights) |

---

### [Stable Audio Tools](https://github.com/Stability-AI/stable-audio-tools)

> Stability AI's training and inference stack for text-to-audio diffusion models — the engine behind Stable Audio Open, generating music, sound effects, and stems from a prompt, replacing a sample-library or stock-SFX subscription.

| | |
|---|---|
| **Stars** | ~3.8k |
| **AI** | Latent diffusion + autoencoder models for conditional audio generation |
| **Replaces** | stock sound-effects/sample libraries; hosted text-to-audio APIs |
| **Self-host** | Medium — GPU, PyTorch 2.5+ |
| **License** | MIT |

---

### [YuE](https://github.com/multimodal-art-projection/YuE)

> A lyrics-to-song foundation model that generates minutes-long tracks with vocals *and* instrumental accompaniment from a lyric sheet and genre tag — the closest open answer to "open source Suno alternative" that actually sings.

| | |
|---|---|
| **Stars** | ~6.3k |
| **AI** | Transformer foundation model for full-song generation (vocals + accompaniment) |
| **Replaces** | Suno/Udio for full songs with lyrics |
| **Self-host** | Hard — large model, significant GPU memory |
| **License** | Apache-2.0 |

---

### [ACE-Step](https://github.com/ace-step/ACE-Step-1.5)

> A fast music foundation model that turns a prompt into a full song blueprint — lyrics, structure, and arrangement — then synthesizes it via a hybrid LM-planner + diffusion-transformer, generating a complete track in seconds on consumer GPUs.

| | |
|---|---|
| **Stars** | ~11.5k |
| **AI** | LLM planner + diffusion-transformer synthesizer, 50+ languages, voice cloning and lyric editing |
| **Replaces** | Suno/Udio subscription; a composer/arranger for demo production |
| **Self-host** | Medium — runs on consumer GPUs (and CPU/Mac, per project docs) |
| **License** | MIT |

---

### [RVC (Retrieval-based Voice Conversion WebUI)](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)

> Train a convincing voice-conversion model from as little as 10 minutes of audio — the tool behind most AI "sing in this voice" covers online — replacing a session vocalist or dub artist for demo and cover production.

| | |
|---|---|
| **Stars** | ~36.3k |
| **AI** | VITS + HiFi-GAN neural vocoder with retrieval-based feature matching, RMVPE pitch extraction |
| **Replaces** | a session vocalist/voice actor for covers, dubbing, and demo work |
| **Self-host** | Medium — GPU for training, WebUI for inference |
| **License** | MIT |

---

### [OpenVoice](https://github.com/myshell-ai/OpenVoice)

> An instant voice-cloning and multilingual text-to-speech model (MIT + MyShell) — clone a reference voice's tone from a short sample and generate speech in a different language or accent, replacing a paid voice-cloning API for narration and dubbing.

| | |
|---|---|
| **Stars** | ~36.9k |
| **AI** | Neural TTS foundation model (VITS-based) with zero-shot cross-lingual voice cloning |
| **Replaces** | ElevenLabs-style voice-cloning APIs; a voiceover artist for multilingual dubbing |
| **Self-host** | Medium — GPU for real-time use |
| **License** | MIT |

---

### [basic-pitch](https://github.com/spotify/basic-pitch)

> Spotify's lightweight neural network for automatic music transcription — feed it an audio file, get back MIDI with pitch bends — replacing manual transcription or a paid audio-to-MIDI service for producers who write by ear.

| | |
|---|---|
| **Stars** | ~5.2k |
| **AI** | Compact neural network for polyphonic pitch/note detection (ICASSP 2022) |
| **Replaces** | manual ear-transcription; paid audio-to-MIDI tools |
| **Self-host** | Easy — pip-installable, runs on CPU |
| **License** | Apache-2.0 |

---

Music has real end-to-end AI-native depth now: full-song generation (YuE,
ACE-Step, AudioCraft), voice conversion and cloning (RVC, OpenVoice), and
transcription (basic-pitch). A few well-known names were left off deliberately —
so-vits-svc and the original Demucs and Riffusion repos are archived or
explicitly unmaintained, so they didn't clear this page's bar.

See also the [Media & Creative](../media/README.md) industry page for
image/video generation, speech-to-text (Whisper), and general TTS
(Chatterbox). Related departments: [Design](../../departments/design/) ·
[Marketing](../../departments/marketing/).

🏭 Back to the [industry index](../README.md).
