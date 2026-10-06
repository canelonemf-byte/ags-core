from base_agent import BaseAgent
from registry import register


@register
class ExperimentalDesignAgent(BaseAgent):
    name = "experimental_design"
    domain = "lab"
    description = "Diseño experimental"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Diseño. Controles y potencia, no ejecución."


@register
class RoboticOperatorAgent(BaseAgent):
    name = "robotic_operator"
    domain = "lab"
    description = "Operación robótica"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Planes robóticos verificables, no actuación."


@register
class ExperimentOptimizerAgent(BaseAgent):
    name = "experiment_optimizer"
    domain = "lab"
    description = "Optimización experimental"
    preferred_model = "gpt-primary"
    fallback_models = ["grok-primary"]

    @property
    def system_prompt(self):
        return "Criterios de parada, no resultado de laboratorio."


@register
class ProtocolSimulatorAgent(BaseAgent):
    name = "protocol_simulator"
    domain = "lab"
    description = "Simulación de protocolos"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Simulación no es experimento."
