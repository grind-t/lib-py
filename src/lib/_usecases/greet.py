from lib._core.greeting import format_greeting
from lib._ports.name_source import NameSource


def greet_from(source: NameSource) -> str:
    return format_greeting(source.get_name())
