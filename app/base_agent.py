from abc import ABC, abstractmethod
from typing import Any

import httpx

from config import settings


class BaseAgent(ABC):
    name = "base"
    domain = "general"
    description = ""
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary", "gemini-primary"]

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        ...

    async def run(self, task: str, context: dict[str, Any] | None = None):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self._prompt(task, context or {})},
        ]
        last_error = None
        async with httpx.AsyncClient(
            base_url=settings.LITELLM_BASE_URL,
            headers={"Authorization": f"Bearer {settings.LITELLM_API_KEY}"},
            timeout=120.0,
        ) as client:
            for model in [self.preferred_model, *self.fallback_models]:
                try:
                    response = await client.post(
                        "/chat/completions",
                        json={"model": model, "messages": messages},
                    )
                    response.raise_for_status()
                    data = response.json()
                    return {
                        "agent": self.name,
                        "domain": self.domain,
                        "model_used": model,
                        "output": data["choices"][0]["message"]["content"],
                    }
                except Exception as exc:
                    last_error = exc
        raise RuntimeError(f"{self.name}: todos los modelos fallaron: {last_error}")

    def _prompt(self, task, context):
        if not context:
            return task
        ctx = "\n".join(f"- {k}: {v}" for k, v in context.items())
        return f"TAREA:\n{task}\n\nCONTEXTO:\n{ctx}"
