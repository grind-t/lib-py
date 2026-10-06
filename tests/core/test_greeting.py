from lib._core.greeting import format_greeting


def test_format_greeting() -> None:
    assert format_greeting("Alice") == "Hello, Alice!"
