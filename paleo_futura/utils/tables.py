from pathlib import Path
import pandas as pd


def read_table(path: str | Path) -> pd.DataFrame:
    """Read CSV or TSV based on file extension."""
    path = Path(path)
    if path.suffix.lower() in [".tsv", ".txt"]:
        return pd.read_csv(path, sep="	")
    return pd.read_csv(path)
