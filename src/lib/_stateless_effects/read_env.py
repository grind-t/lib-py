import os


def read_env(key: str) -> str | None:
    """Read a process environment variable."""
    return os.environ.get(key)
