from collections.abc import Callable

from lib._stateless_computations.greeting import format_greeting


def greet(read_env: Callable[[str], str | None]) -> str:
    """Greet the name from the ``LIB_NAME`` variable returned by ``read_env``."""
    name = read_env("LIB_NAME")
    return format_greeting("World" if name is None else name)
