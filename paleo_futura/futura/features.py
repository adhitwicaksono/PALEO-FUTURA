"""Feature-table handling for FUTURA v0.1."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

from paleo_futura.utils.tables import read_table, require_columns

REQUIRED_FEATURE_COLUMNS = {"gene_id"}

OPTIONAL_NUMERIC_COLUMNS = [
    "kaks",
    "pnps",
    "snp_density",
    "stress_log2fc",
    "gene_family_size",
]


def read_gene_features(path: str | Path) -> pd.DataFrame:
    """Read and validate a FUTURA gene-feature table.

    Required columns:
    - gene_id

    Recommended columns:
    - orthogroup
    - kaks
    - pnps
    - snp_density
    - stress_log2fc
    - te_proximity
    - gene_family_size
    - scenario
    """
    df = read_table(path)
    require_columns(df, REQUIRED_FEATURE_COLUMNS, table_name="gene feature table")

    df["gene_id"] = df["gene_id"].astype(str)

    for col in OPTIONAL_NUMERIC_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "te_proximity" in df.columns:
        df["te_proximity"] = df["te_proximity"].apply(_parse_bool)

    return df


def _parse_bool(value) -> bool:
    """Parse common truthy/falsy values."""
    if isinstance(value, bool):
        return value
    if pd.isna(value):
        return False
    return str(value).strip().lower() in {"true", "1", "yes", "y"}
