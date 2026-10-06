from lib._core import format_greeting
from lib._service import greet_from


class FakeSource:
    """Port fake: no inheritance, no mocks, just an object with the right method."""

    def get_name(self) -> str:
        return "Alice"


def test_format_greeting() -> None:
    assert format_greeting("Alice") == "Hello, Alice!"


def test_greet_from() -> None:
    assert greet_from(FakeSource()) == "Hello, Alice!"
