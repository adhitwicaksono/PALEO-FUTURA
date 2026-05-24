"""Uncertainty flag helpers for PALEO-FUTURA."""

from __future__ import annotations

import pandas as pd


def join_flags(flags: list[str]) -> str:
    """Join uncertainty flags into a semicolon-separated string."""
    cleaned = [flag for flag in flags if flag]
    return ";".join(cleaned) if cleaned else "none"


def flag_missing(row: pd.Series, column: str, flag_name: str | None = None) -> str | None:
    """Return a flag if a column is missing or contains a null value."""
    if column not in row.index or pd.isna(row.get(column)):
        return flag_name or f"missing_{column}"
    return None


def paleo_orthogroup_flags(
    n_species: int,
    n_genes: int,
    max_genes_per_species: int,
    min_species: int = 2,
    duplication_threshold: int = 2,
) -> str:
    """Create uncertainty flags for a summarized orthogroup."""
    flags: list[str] = []

    if n_species < min_species:
        flags.append("low_species_count")

    if max_genes_per_species >= duplication_threshold:
        flags.append("possible_duplication_or_paralogy")

    if n_genes == 0:
        flags.append("empty_orthogroup")

    return join_flags(flags)


def futura_gene_flags(row: pd.Series) -> str:
    """Create uncertainty flags for a FUTURA gene-feature row."""
    flags: list[str] = []

    for col in ["kaks", "pnps", "snp_density", "stress_log2fc"]:
        flag = flag_missing(row, col)
        if flag:
            flags.append(flag)

    if "scenario" not in row.index or pd.isna(row.get("scenario")) or str(row.get("scenario")).strip() == "":
        flags.append("missing_scenario")

    if "gene_id" not in row.index or pd.isna(row.get("gene_id")):
        flags.append("missing_gene_id")

    return join_flags(flags)
