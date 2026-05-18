from pathlib import Path
import pandas as pd


def read_gff_attributes(attributes: str) -> dict:
    """Parse the attributes column of a simple GFF3 line."""
    parsed = {}
    for item in attributes.split(";"):
        if not item:
            continue
        if "=" in item:
            key, value = item.split("=", 1)
            parsed[key] = value
    return parsed


def read_gff_basic(path: str | Path) -> pd.DataFrame:
    """Read a basic GFF3 file into a DataFrame, skipping comments."""
    rows = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            parts = line.rstrip("
").split("	")
            if len(parts) != 9:
                continue
            rows.append(parts)
    return pd.DataFrame(rows, columns=["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"])
