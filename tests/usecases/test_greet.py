from lib._usecases.greet import greet_from


def fake_source() -> str:
    """Port fake: no mocks, just a function with the right signature."""
    return "Alice"


def test_greet_from() -> None:
    assert greet_from(fake_source) == "Hello, Alice!"
