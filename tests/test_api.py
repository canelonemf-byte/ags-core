import pytest
from fastapi.testclient import TestClient

from main import app

pytestmark = pytest.mark.unit
client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200 and r.json()["agents"] == 31


def test_request_id():
    r = client.get("/health", headers={"X-Request-ID": "test-123"})
    assert r.headers["X-Request-ID"] == "test-123"


def test_agents():
    r = client.get("/agents")
    assert r.status_code == 200 and r.json()["total"] == 31


def test_auth():
    assert client.post("/run/agent/searcher", json={"task": "x"}).status_code == 401


def test_unknown_agent_with_auth():
    r = client.post(
        "/run/agent/nope",
        headers={"X-API-Key": "test-key"},
        json={"task": "x"},
    )
    assert r.status_code == 404


def test_unknown_domain():
    assert client.get("/agents/domain/nope").status_code == 404


def test_integrations_configurable():
    r = client.get("/integrations", headers={"X-API-Key": "test-key"})
    assert r.status_code == 200
