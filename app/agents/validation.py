from base_agent import BaseAgent
from registry import register


@register
class ReproducibilityAuditorAgent(BaseAgent):
    name = "reproducibility_auditor"
    domain = "validation"
    description = "Reproducibilidad"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Auditor de semillas, versiones y pasos."


@register
class LogVerifierAgent(BaseAgent):
    name = "log_verifier"
    domain = "validation"
    description = "Trazabilidad"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Verificador de logs."


@register
class AdversaryAgent(BaseAgent):
    name = "adversary"
    domain = "validation"
    description = "Red teaming"
    preferred_model = "grok-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Adversario defensivo."


@register
class RiskEvaluatorAgent(BaseAgent):
    name = "risk_evaluator"
    domain = "validation"
    description = "Evaluación de riesgos"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Riesgos técnicos, no dictamen clínico."
