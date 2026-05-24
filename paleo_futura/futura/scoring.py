"""Transparent FUTURA v0.1 adaptive-potential scoring."""

from __future__ import annotations

import pandas as pd

from paleo_futura.utils.uncertainty import futura_gene_flags


def score_adaptive_potential(row: pd.Series) -> float:
    """Score adaptive potential using transparent heuristic rules.

    This is a v0.1 prototype score, not a validated biological model.

    The score intentionally rewards:
    - possible positive/relaxed coding evolution
    - population-level variation
    - strong stress response
    - TE/regulatory proximity
    - gene-family duplication

    Missing values simply contribute no points and are flagged separately.
    """
    score = 0.0

    kaks = row.get("kaks")
    if pd.notna(kaks):
        if kaks > 1.0:
            score += 2.0
        elif kaks >= 0.5:
            score += 0.75
        else:
            score += 0.1

    pnps = row.get("pnps")
    if pd.notna(pnps):
        if pnps > 1.0:
            score += 1.5
        elif pnps >= 0.5:
            score += 0.75
        else:
            score += 0.1

    snp_density = row.get("snp_density")
    if pd.notna(snp_density):
        score += min(max(float(snp_density), 0.0), 2.0)

    stress_log2fc = row.get("stress_log2fc")
    if pd.notna(stress_log2fc):
        score += min(abs(float(stress_log2fc)), 3.0)

    te_proximity = row.get("te_proximity")
    if bool(te_proximity):
        score += 0.5

    gene_family_size = row.get("gene_family_size")
    if pd.notna(gene_family_size):
        if float(gene_family_size) > 5:
            score += 0.75
        elif float(gene_family_size) > 1:
            score += 0.5

    return round(score, 3)


def classify_adaptive_score(score: float) -> str:
    """Classify FUTURA adaptive-potential score."""
    if score >= 6.0:
        return "high_adaptive_potential"
    if score >= 3.5:
        return "moderate_adaptive_potential"
    if score >= 1.5:
        return "low_adaptive_potential"
    return "uncertain_or_constrained"


def infer_selection_hint(row: pd.Series) -> str:
    """Give a simple interpretation hint from Ka/Ks and pN/pS."""
    kaks = row.get("kaks")
    pnps = row.get("pnps")

    if pd.notna(kaks) and kaks < 0.5 and (pd.isna(pnps) or pnps < 0.5):
        return "coding_constraint_likely"

    if (pd.notna(kaks) and kaks > 1.0) or (pd.notna(pnps) and pnps > 1.0):
        return "adaptive_or_relaxed_candidate"

    if pd.notna(kaks) and 0.5 <= kaks <= 1.0:
        return "moderate_constraint_or_relaxation"

    return "insufficient_selection_evidence"


def score_feature_table(df: pd.DataFrame) -> pd.DataFrame:
    """Add FUTURA score, class, selection hint, and uncertainty flags."""
    scored = df.copy()
    scored["adaptive_potential_score"] = scored.apply(score_adaptive_potential, axis=1)
    scored["futura_class"] = scored["adaptive_potential_score"].apply(classify_adaptive_score)
    scored["selection_hint"] = scored.apply(infer_selection_hint, axis=1)
    scored["uncertainty_flags"] = scored.apply(futura_gene_flags, axis=1)

    sort_cols = ["adaptive_potential_score", "gene_id"]
    return scored.sort_values(sort_cols, ascending=[False, True]).reset_index(drop=True)
