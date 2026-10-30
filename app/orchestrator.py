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
            "Selecciona agentes SOLO del catalogo. Responde SOLO JSON "
            '{"agents":["nombre"]}. No inventes nombres. Maximo 8.'
            f"\n\nCATALOGO:\n{self._catalog()}\n\nOBJETIVO:\n{task}"
        )
        try:
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
            chosen = json.loads(payload["choices"][0]["message"]["content"]).get(
                "agents", []
            )
            if not isinstance(chosen, list):
                chosen = []
        except (httpx.HTTPError, KeyError, TypeError, IndexError, json.JSONDecodeError):
            chosen = []
        return [x for x in chosen if x in all_agents()][:8] or [
            "searcher",
            "summarizer",
            "critic",
        ]

    async def execute(self, task, plan=None):
        plan = plan or await self.plan(task)
        results, context = [], {"objetivo": task}
        for name in plan:
            try:
                out = await get_agent(name).run(task, context)
                context[f"resultado_{name}"] = out["output"][:2000]
                results.append(out)
            except Exception as exc:
                results.append({"agent": name, "status": "error", "error": str(exc)[:200]})

        errors = sum(1 for x in results if x.get("status") == "error")
        status = "completed" if errors == 0 else ("failed" if errors == len(results) else "partial")
        return {"status": status, "plan": plan, "errors": errors, "results": results, "escribe_ciencia": False}


orchestrator = Orchestrator()
