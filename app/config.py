import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    LITELLM_BASE_URL = os.getenv("LITELLM_BASE_URL", "http://localhost:4000")
    LITELLM_API_KEY = os.getenv("LITELLM_MASTER_KEY", "")
    AGS_API_KEY = os.getenv("AGS_API_KEY", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    INTEGRATIONS = {
        "llp_api_gateway": os.getenv("LLP_API_GATEWAY_URL", ""),
        "omniscience": os.getenv("OMNISCIENCE_URL", ""),
        "quantum_blueprint": os.getenv("QUANTUM_BLUEPRINT_URL", ""),
        "ordenador_hibrido": os.getenv("ORDENADOR_HIBRIDO_URL", ""),
        "simulador_cuantico": os.getenv("SIMULADOR_CUANTICO_URL", ""),
        "remplast_q": os.getenv("REMPLAST_Q_URL", ""),
        "cero_a": os.getenv("CERO_A_URL", ""),
    }


settings = Settings()
