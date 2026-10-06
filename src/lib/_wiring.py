from lib._adapters import EnvName
from lib._usecases import greet_from


def greet() -> str:
    return greet_from(EnvName())
