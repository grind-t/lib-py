from lib._adapters import EnvName
from lib._service import greet_from


def greet() -> str:
    return greet_from(EnvName())
