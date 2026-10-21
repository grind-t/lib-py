from lib._stateless_workflows.greet import greet


def test_greet() -> None:
    assert greet({"LIB_NAME": "Alice"}.get) == "Hello, Alice!"


def test_greet_default() -> None:
    assert greet({}.get) == "Hello, World!"
