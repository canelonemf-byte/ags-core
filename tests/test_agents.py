import pytest

from orchestrator import orchestrator

pytestmark = pytest.mark.unit


class Fake:
    def __init__(self, ok):
        self.ok = ok

    async def run(self, task, ctx):
        if not self.ok:
            raise RuntimeError("fallo")
        return {"agent": "x", "output": "ok"}


async def _run(monkeypatch, flags):
    names = [f"n{i}" for i in range(len(flags))]
    fakes = {n: Fake(f) for n, f in zip(names, flags)}
    monkeypatch.setattr("orchestrator.get_agent", lambda n: fakes[n])
    return await orchestrator.execute("t", plan=names)


async def test_all_ok(monkeypatch):
    assert (await _run(monkeypatch, [True, True]))["status"] == "completed"


async def test_partial(monkeypatch):
    r = await _run(monkeypatch, [True, False])
    assert r["status"] == "partial" and r["errors"] == 1


async def test_failed(monkeypatch):
    assert (await _run(monkeypatch, [False, False]))["status"] == "failed"
