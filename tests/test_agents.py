import pytest

from registry import agents_by_domain, all_agents, get_agent

pytestmark = pytest.mark.unit
EXPECTED = 31


def test_registry_count():
    assert len(all_agents()) == EXPECTED


def test_required_fields():
    for name, a in all_agents().items():
        assert a.name == name and a.domain and a.description and a.system_prompt
        assert a.preferred_model and isinstance(a.fallback_models, list)


def test_domains():
    assert len(agents_by_domain("research")) == 5
    assert len(agents_by_domain("compute")) == 5
    assert len(agents_by_domain("domain")) == 6
    assert len(agents_by_domain("multimodal")) == 4
    assert len(agents_by_domain("lab")) == 4
    assert len(agents_by_domain("validation")) == 4
    assert len(agents_by_domain("orchestration")) == 3


def test_unknown_agent():
    with pytest.raises(KeyError):
        get_agent("nonexistent")
