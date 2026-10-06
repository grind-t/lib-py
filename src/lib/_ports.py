from typing import Protocol


class NameSource(Protocol):
    def get_name(self) -> str: ...
