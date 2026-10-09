import pytest

from lib._adapters.env_name import env_name


def test_env_name(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LIB_NAME", "Alice")
    assert env_name() == "Alice"


def test_env_name_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LIB_NAME", raising=False)
    assert env_name() == "World"
