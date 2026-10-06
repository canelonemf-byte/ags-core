from base_agent import BaseAgent
from registry import register


@register
class ProjectManagerAgent(BaseAgent):
    name = "project_manager"
    domain = "orchestration"
    description = "Gestión de proyecto"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Divide objetivos en tareas verificables."


@register
class ResourceOptimizerAgent(BaseAgent):
    name = "resource_optimizer"
    domain = "orchestration"
    description = "Optimización de recursos"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Presupuesto y llamadas, sin fingir coste real."


@register
class ProvenanceAuditorAgent(BaseAgent):
    name = "provenance_auditor"
    domain = "orchestration"
    description = "Procedencia"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Trazabilidad de entradas y salidas."
