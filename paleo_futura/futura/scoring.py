import pandas as pd


def score_adaptive_potential(row: pd.Series) -> float:
    """Transparent toy adaptive-potential score for v0.1.

    Expected optional columns: kaks, pnps, snp_density, stress_log2fc,
    te_proximity, gene_family_size.

    This is not a validated biological model.
    """
    score = 0.0

    kaks = row.get("kaks")
    if pd.notna(kaks):
        if kaks > 1.0:
            score += 2.0
        elif kaks >= 0.5:
            score += 0.5

    pnps = row.get("pnps")
    if pd.notna(pnps):
        if pnps > 1.0:
            score += 1.5
        elif pnps >= 0.5:
            score += 0.5

    snp_density = row.get("snp_density")
    if pd.notna(snp_density):
        score += min(float(snp_density), 2.0)

    stress_log2fc = row.get("stress_log2fc")
    if pd.notna(stress_log2fc):
        score += min(abs(float(stress_log2fc)), 3.0)

    te_proximity = row.get("te_proximity")
    if pd.notna(te_proximity) and bool(te_proximity):
        score += 0.5

    gene_family_size = row.get("gene_family_size")
    if pd.notna(gene_family_size) and float(gene_family_size) > 1:
        score += 0.5

    return round(score, 3)


def classify_adaptive_score(score: float) -> str:
    """Classify adaptive-potential score into broad v0.1 categories."""
    if score >= 5:
        return "high_adaptive_potential"
    if score >= 2.5:
        return "moderate_adaptive_potential"
    if score >= 1:
        return "low_adaptive_potential"
    return "uncertain_or_constrained"


def score_feature_table(df: pd.DataFrame) -> pd.DataFrame:
    """Add FUTURA adaptive-potential score and class."""
    scored = df.copy()
    scored["adaptive_potential_score"] = scored.apply(score_adaptive_potential, axis=1)
    scored["futura_class"] = scored["adaptive_potential_score"].apply(classify_adaptive_score)
    return scored
