from lib._adapters.env_name import EnvName
from lib._usecases.greet import greet_from


def greet() -> str:
    return greet_from(EnvName())
