# AGs-Core

Multi-agent scientific API with 31 specialized agents.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
# fill in .env with your keys
pytest -m unit -q
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Endpoints

- GET /health
- GET /agents
- GET /agents/domain/{domain}
- POST /run/agent/{name}
- POST /run/orchestrated
- GET /integrations
- GET /models

## Authentication

The app validates `X-API-Key` against `AGS_API_KEY` in `.env`.

## Domain split

- research: 5
- compute: 5
- domain: 6
- multimodal: 4
- lab: 4
- validation: 4
- orchestration: 3

Total: 31 agents.
