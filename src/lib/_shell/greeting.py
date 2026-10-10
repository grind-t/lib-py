import os

from lib._core.greeting import format_greeting


def greet() -> str:
    """Greet the name from the ``LIB_NAME`` environment variable."""
    return format_greeting(os.environ.get("LIB_NAME", "World"))
