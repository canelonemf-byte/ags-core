from base_agent import BaseAgent
from registry import register


@register
class SearcherAgent(BaseAgent):
    name = "searcher"
    domain = "research"
    description = "Rastreo científico"
    preferred_model = "perplexity-primary"
    fallback_models = ["kimi-primary"]

    @property
    def system_prompt(self):
        return "Buscador científico. Devuelve fuentes identificables y marca lo no verificado."


@register
class SummarizerAgent(BaseAgent):
    name = "summarizer"
    domain = "research"
    description = "Síntesis de corpus"
    preferred_model = "kimi-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Sintetizador. Separa datos, hipótesis y conclusiones."


@register
class CriticAgent(BaseAgent):
    name = "critic"
    domain = "research"
    description = "Detección de gaps"
    preferred_model = "claude-primary"
    fallback_models = ["grok-primary"]

    @property
    def system_prompt(self):
        return "Crítico. Busca sesgos, lagunas y alternativas."


@register
class VerifierAgent(BaseAgent):
    name = "verifier"
    domain = "research"
    description = "Validación de citas"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Verificador. No afirma una cita sin evidencia disponible."


@register
class WriterAgent(BaseAgent):
    name = "writer"
    domain = "research"
    description = "Redacción IMRyD"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Escritor. Distingue evidencia de interpretación."
