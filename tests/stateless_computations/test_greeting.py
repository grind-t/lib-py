from lib._stateless_computations.greeting import format_greeting


def test_format_greeting() -> None:
    assert format_greeting("Alice") == "Hello, Alice!"
