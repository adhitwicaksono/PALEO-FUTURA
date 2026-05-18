import pandas as pd

REQUIRED_COLUMNS = {"orthogroup", "species", "gene_id"}


def validate_orthogroup_table(df: pd.DataFrame) -> None:
    """Validate minimal orthogroup table columns."""
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required orthogroup columns: {sorted(missing)}")


def summarize_orthogroups(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize species and gene counts per orthogroup."""
    validate_orthogroup_table(df)
    return (
        df.groupby("orthogroup")
        .agg(n_species=("species", "nunique"), n_genes=("gene_id", "count"))
        .reset_index()
        .sort_values(["n_species", "n_genes"], ascending=False)
    )
