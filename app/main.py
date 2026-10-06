import uuid

import httpx
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel, Field

import agents  # noqa: F401
from config import settings
from registry import agents_by_domain, all_agents, get_agent
from orchestrator import orchestrator

app = FastAPI(title="AGs-Core", version="3.3.0")


class TaskRequest(BaseModel):
    task: str = Field(min_length=1, max_length=20000)
    context: dict | None = None


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    rid = request.headers.get("X-Request-ID") or str(uuid.uuid4())
    response = await call_next(request)
    response.headers["X-Request-ID"] = rid
    return response


def auth(x_api_key: str | None):
    if not settings.AGS_API_KEY:
        raise HTTPException(503, "AGS_API_KEY no configurada")
    if x_api_key != settings.AGS_API_KEY:
        raise HTTPException(401, "API key invalida")


@app.get("/health")
def health():
    return {
        "status": "ok",
        "agents": len(all_agents()),
        "version": "3.3.0",
        "litellm": False,
        "docker": False,
    }


@app.get("/agents")
def list_agents():
    return {
        "total": len(all_agents()),
        "agents": [
            {
                "name": a.name,
                "domain": a.domain,
                "description": a.description,
                "model": a.preferred_model,
            }
            for a in all_agents().values()
        ],
    }


@app.get("/models")
async def models(x_api_key: str | None = Header(default=None)):
    auth(x_api_key)
    async with httpx.AsyncClient(
        base_url=settings.LITELLM_BASE_URL,
        headers={"Authorization": f"Bearer {settings.LITELLM_API_KEY}"},
        timeout=15,
    ) as client:
        r = await client.get("/v1/models")
        r.raise_for_status()
        return r.json()


@app.get("/integrations")
def integrations(x_api_key: str | None = Header(default=None)):
    auth(x_api_key)
    return {
        "integrations": {
            k: ("configured" if v else "not_configured")
            for k, v in settings.INTEGRATIONS.items()
        }
    }


@app.get("/agents/domain/{domain}")
def by_domain(domain: str):
    xs = agents_by_domain(domain)
    if not xs:
        raise HTTPException(404, f"Sin agentes en {domain}")
    return {"domain": domain, "agents": [a.name for a in xs]}


@app.post("/run/agent/{name}")
async def run_single(name: str, req: TaskRequest, x_api_key: str | None = Header(default=None)):
    auth(x_api_key)
    try:
        agent = get_agent(name)
    except KeyError:
        raise HTTPException(404, f"Agente {name} no existe")
    return await agent.run(req.task, req.context)


@app.post("/run/orchestrated")
async def run_orch(req: TaskRequest, x_api_key: str | None = Header(default=None)):
    auth(x_api_key)
    return await orchestrator.execute(req.task)
