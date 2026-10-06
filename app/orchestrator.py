import json

import httpx

from config import settings
from registry import all_agents, get_agent


class Orchestrator:
    def _catalog(self):
        return "\n".join(
            f"- {n} [{a.domain}] {a.description}" for n, a in all_agents().items()
        )

    async def plan(self, task):
        prompt = (
            'Selecciona agentes SOLO del catálogo. Responde SOLO JSON '
            '{"agents":["nombre"]}. No inventes nombres. Máximo 8 agentes. '
            f"\n\nCATÁLOGO:\n{self._catalog()}\n\nOBJETIVO:\n{task}"
        )
        async with httpx.AsyncClient(
            base_url=settings.LITELLM_BASE_URL,
            headers={"Authorization": f"Bearer {settings.LITELLM_API_KEY}"},
            timeout=90.0,
        ) as client:
            r = await client.post(
                "/chat/completions",
                json={
                    "model": "claude-primary",
                    "messages": [{"role": "user", "content": prompt}],
                    "response_format": {"type": "json_object"},
                },
            )
            r.raise_for_status()
            payload = r.json()
        try:
            chosen = json.loads(
                payload["choices"][0]["message"]["content"]
            ).get("agents", [])
        except (KeyError, TypeError, json.JSONDecodeError):
            chosen = []
        return [x for x in chosen if x in all_agents()][:8] or [
            "searcher",
            "summarizer",
            "critic",
        ]

    async def execute(self, task, plan=None):
        plan = plan or await self.plan(task)
        results = []
        context = {"objetivo": task}
        for name in plan:
            try:
                out = await get_agent(name).run(task, context)
                context[f"resultado_{name}"] = out["output"][:2000]
                results.append(out)
            except Exception as exc:
                results.append({"agent": name, "status": "error", "error": str(exc)})
        return {"status": "completed", "plan": plan, "results": results}


orchestrator = Orchestrator()
