# ags-core

AGs-Core FastAPI multi-agent API and registry project

## Autoría

- **Autor:** Lázaro López Paz, El Prat de Llobregat, Barcelona, España
- **ORCID:** [0000-0001-8601-1963](https://orcid.org/0000-0001-8601-1963)
- Elaborado con asistencia de inteligencia artificial
- Sin afiliaciones institucionales

## Estado

Proyecto en desarrollo / documentación. No afirmar validación experimental salvo que el código o los informes del propio repositorio lo demuestren.

## Contenido (raíz)

```
.env.example
app/
docker-compose.yml
Dockerfile
litellm_config.yaml
pytest.ini
README.md
requirements-dev.txt
requirements.txt
tests/
```

## Instalación

```bash
pip install -r requirements.txt
```


## Uso

Archivos Python principales (revisar cada uno antes de ejecutar):
- `app/__init__.py`
- `app/agents/__init__.py`
- `app/agents/compute.py`
- `app/agents/domain.py`
- `app/agents/lab.py`
- `app/agents/multimodal.py`
- `app/agents/orchestration.py`
- `app/agents/research.py`
- `app/agents/validation.py`
- `app/base_agent.py`
- `app/config.py`
- `app/main.py`


## Licencia

Ver archivo `LICENSE` (o `LICENSE.md`) en la raíz. Documentación bajo CC BY 4.0 cuando aplique; código habitualmente MIT, salvo indicación contraria.
