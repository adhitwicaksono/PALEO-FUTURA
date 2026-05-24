"""Table utilities for PALEO-FUTURA."""

from __future__ import annotations

from pathlib import Path
import pandas as pd


def read_table(path: str | Path) -> pd.DataFrame:
    """Read a CSV or TSV table.

    The separator is inferred from the file extension:
    - .tsv or .txt = tab-separated
    - anything else = comma-separated
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Input file does not exist: {path}")

    if path.suffix.lower() in {".tsv", ".txt"}:
        return pd.read_csv(path, sep="\t")

    return pd.read_csv(path)


def require_columns(df: pd.DataFrame, required: set[str], table_name: str = "table") -> None:
    """Raise a clear error if required columns are missing."""
    missing = sorted(required - set(df.columns))
    if missing:
        raise ValueError(
            f"Missing required column(s) in {table_name}: {missing}. "
            f"Available columns: {list(df.columns)}"
        )
