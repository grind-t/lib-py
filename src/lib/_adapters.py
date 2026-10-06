import os


class EnvName:
    """Name from the ``LIB_NAME`` environment variable."""

    def get_name(self) -> str:
        return os.environ.get("LIB_NAME", "World")
