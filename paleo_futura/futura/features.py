import pandas as pd

REQUIRED_COLUMNS = {"gene_id"}


def validate_feature_table(df: pd.DataFrame) -> None:
    """Validate minimal FUTURA feature table."""
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required feature columns: {sorted(missing)}")
