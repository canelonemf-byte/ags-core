from typing import Type

from base_agent import BaseAgent

_REGISTRY = {}


def register(cls: Type[BaseAgent]):
    instance = cls()
    if instance.name in _REGISTRY:
        raise RuntimeError(f"Agente duplicado: {instance.name}")
    _REGISTRY[instance.name] = instance
    return cls


def get_agent(name):
    return _REGISTRY[name]


def all_agents():
    return _REGISTRY


def agents_by_domain(domain):
    return [a for a in _REGISTRY.values() if a.domain == domain]
