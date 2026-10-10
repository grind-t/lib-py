import pytest

from lib._shell.greeting import greet


def test_greet(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("LIB_NAME", "Alice")
    assert greet() == "Hello, Alice!"


def test_greet_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LIB_NAME", raising=False)
    assert greet() == "Hello, World!"
