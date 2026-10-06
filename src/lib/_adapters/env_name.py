import os


def env_name() -> str:
    """Name from the ``LIB_NAME`` environment variable."""
    return os.environ.get("LIB_NAME", "World")
