from lib._core import format_greeting
from lib._ports import NameSource


def greet_from(source: NameSource) -> str:
    return format_greeting(source.get_name())
