from pathlib import Path


def file_exists(path: str | Path) -> bool:
    """Placeholder helper for future trees.py integration."""
    return Path(path).exists()
