# Letta + LiveKit voice agent example

This folder contains a small example showing how to connect a LiveKit voice agent to a Letta agent.

Files
- `letta_voice_agent.py` — LiveKit agent entrypoint example (called by the LiveKit agent runner)
- `.env.example` — Example environment variables
- `requirements.txt` — Suggested packages to install

Quickstart
1. Copy `.env.example` to `.env` and fill in your credentials (LETTA_API_KEY, LETTA_AGENT_ID, LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET, DEEPGRAM_API_KEY, CARTESIA_API_KEY).

2. Create and activate a virtual environment and install packages:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r letta_example\requirements.txt
pip install python-dotenv
```

3. Run the example with a LiveKit job runner. The `letta_voice_agent.entrypoint` is intended to be used by the LiveKit agents runner (see the `letta-voice` repo for a full deployment example):

- For Letta Cloud usage: set `LETTA_API_KEY` and `LETTA_AGENT_ID`.
- For self-hosted Letta: set `LETTA_BASE_URL` to your HTTPS forwarding URL (ngrok or similar) and `LETTA_AGENT_ID`.

Notes
- The example relies on provider plugins (`livekit.plugins.openai`, `deepgram`, `cartesia`) — follow the `letta-voice` repo for exact dependency names and runtime orchestration.
- Voice agent support is experimental.

If you want, I can:
- Add a tiny runner that demonstrates a simulated (text-only) voice session locally.
- Add CI-friendly tests or a Dockerfile for running the LiveKit runner.
