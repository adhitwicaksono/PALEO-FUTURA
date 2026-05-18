import pandas as pd


def classify_kaks(value: float, low_threshold: float = 0.8, high_threshold: float = 1.2) -> str:
    """Classify Ka/Ks or dN/dS values using broad heuristic thresholds.

    This is intentionally simple for v0.1 and should not replace formal tests.
    """
    if pd.isna(value):
        return "uncertain"
    if value < low_threshold:
        return "purifying"
    if value > high_threshold:
        return "positive_candidate"
    return "neutral_or_relaxed"
