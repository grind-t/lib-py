from lib._stateless_effects.env import read_env
from lib._stateless_workflows.greeting import greet as _greet


def greet() -> str:
    """Greet the name from the ``LIB_NAME`` environment variable."""
    return _greet(read_env)


__all__ = ["greet"]
