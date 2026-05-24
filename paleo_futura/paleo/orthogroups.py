"""Orthogroup parsing and summary functions for PALEO v0.1."""

from __future__ import annotations

from pathlib import Path
import pandas as pd

from paleo_futura.utils.tables import read_table, require_columns
from paleo_futura.utils.uncertainty import paleo_orthogroup_flags

REQUIRED_ORTHOGROUP_COLUMNS = {"orthogroup", "species", "gene_id"}


def read_orthogroups(path: str | Path) -> pd.DataFrame:
    """Read and validate an orthogroup table.

    Required columns:
    - orthogroup
    - species
    - gene_id

    Optional columns:
    - sequence_id
    - notes
    """
    df = read_table(path)
    require_columns(df, REQUIRED_ORTHOGROUP_COLUMNS, table_name="orthogroup table")

    # Normalize key columns as strings for stable grouping.
    for col in REQUIRED_ORTHOGROUP_COLUMNS:
        df[col] = df[col].astype(str)

    return df


def summarize_orthogroups(
    df: pd.DataFrame,
    duplication_threshold: int = 2,
) -> pd.DataFrame:
    """Summarize orthogroup membership and uncertainty flags.

    Parameters
    ----------
    df:
        Orthogroup table with columns orthogroup, species, gene_id.
    duplication_threshold:
        If an orthogroup has at least this many genes in any species,
        it is flagged as possible duplication/paralogy.

    Returns
    -------
    pandas.DataFrame
        One row per orthogroup.
    """
    require_columns(df, REQUIRED_ORTHOGROUP_COLUMNS, table_name="orthogroup table")

    basic = (
        df.groupby("orthogroup")
        .agg(
            n_species=("species", "nunique"),
            n_genes=("gene_id", "count"),
            species_list=("species", lambda x: ";".join(sorted(set(map(str, x))))),
            gene_list=("gene_id", lambda x: ";".join(map(str, x))),
        )
        .reset_index()
    )

    per_species = (
        df.groupby(["orthogroup", "species"])
        .size()
        .reset_index(name="genes_in_species")
    )

    max_per_species = (
        per_species.groupby("orthogroup")
        .agg(max_genes_per_species=("genes_in_species", "max"))
        .reset_index()
    )

    summary = basic.merge(max_per_species, on="orthogroup", how="left")

    summary["paleo_status"] = summary.apply(
        lambda row: (
            "possible_paralogous_family"
            if row["max_genes_per_species"] >= duplication_threshold
            else "single_or_low_copy_family"
        ),
        axis=1,
    )

    summary["uncertainty_flags"] = summary.apply(
        lambda row: paleo_orthogroup_flags(
            n_species=int(row["n_species"]),
            n_genes=int(row["n_genes"]),
            max_genes_per_species=int(row["max_genes_per_species"]),
            duplication_threshold=duplication_threshold,
        ),
        axis=1,
    )

    return summary.sort_values(
        ["n_species", "n_genes", "orthogroup"],
        ascending=[False, False, True],
    ).reset_index(drop=True)
