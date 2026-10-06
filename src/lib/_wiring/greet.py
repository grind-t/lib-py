from lib._adapters.env_name import env_name
from lib._usecases.greet import greet_from


def greet() -> str:
    return greet_from(env_name)
