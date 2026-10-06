from base_agent import BaseAgent
from registry import register


@register
class BioinformaticsAgent(BaseAgent):
    name = "bioinformatics"
    domain = "domain"
    description = "Genómica"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Bioinformatica. Pipelines con trazabilidad."


@register
class ChemoinformaticsAgent(BaseAgent):
    name = "chemoinformatics"
    domain = "domain"
    description = "Quimioinformatica"
    preferred_model = "gpt-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Quimioinformatica computacional, no experimento."


@register
class Structure3DAgent(BaseAgent):
    name = "structure_3d"
    domain = "domain"
    description = "Estructuras 3D"
    preferred_model = "claude-primary"
    fallback_models = ["gemini-primary"]

    @property
    def system_prompt(self):
        return "Estructuras. PDB/CIF y RMSD como análisis."


@register
class PhysicsAgent(BaseAgent):
    name = "physics"
    domain = "domain"
    description = "Física computacional"
    preferred_model = "gpt-primary"
    fallback_models = ["grok-primary"]

    @property
    def system_prompt(self):
        return "Fisica. Unidades, supuestos y verificación."


@register
class AstronomyAgent(BaseAgent):
    name = "astronomy"
    domain = "domain"
    description = "Astronomía de datos"
    preferred_model = "gemini-primary"
    fallback_models = ["claude-primary"]

    @property
    def system_prompt(self):
        return "Astronomia de catalogos."


@register
class NeuroscienceAgent(BaseAgent):
    name = "neuroscience"
    domain = "domain"
    description = "Neurociencia computacional"
    preferred_model = "claude-primary"
    fallback_models = ["gpt-primary"]

    @property
    def system_prompt(self):
        return "Neurociencia computacional, no diagnostico."
