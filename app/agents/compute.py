from base_agent import BaseAgent
from registry import register


@register
class DeveloperAgent(BaseAgent):
    name = "developer"
    domain = "compute"
    description = "Código reproducible"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Desarrollador. Código limpio y reproducible."


@register
class ComputeAgent(BaseAgent):
    name = "compute"
    domain = "compute"
    description = "Planificación HPC"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Computo. Planifica sin fingir resultados."


@register
class StructuredDataAgent(BaseAgent):
    name = "structured_data"
    domain = "compute"
    description = "Análisis tabular"
    preferred_model = "gpt-primary"
    fallback_models = ["gemini-primary"]

    @property
    def system_prompt(self):
        return "Datos tabulares. EDA y validación."


@register
class TimeSeriesAgent(BaseAgent):
    name = "time_series"
    domain = "compute"
    description = "Series temporales"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Series. Compara modelos y supuestos."


@register
class SymbolicMathAgent(BaseAgent):
    name = "symbolic_math"
    domain = "compute"
    description = "Matemática simbólica"
    preferred_model = "grok-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Simbolico. Formula y verifica expresiones cuando sea posible."
