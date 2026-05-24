"""Markdown report generation for FUTURA v0.1."""

from __future__ import annotations

import pandas as pd


def make_futura_report(
    scored: pd.DataFrame,
    title: str = "FUTURA Report",
    source_file: str | None = None,
) -> str:
    """Create a Markdown FUTURA report from a scored feature table."""
    n_genes = len(scored)
    class_counts = (
        scored["futura_class"].value_counts().rename_axis("futura_class").reset_index(name="n_genes")
        if "futura_class" in scored
        else pd.DataFrame()
    )

    display_cols = [
        col for col in [
            "gene_id",
            "orthogroup",
            "scenario",
            "adaptive_potential_score",
            "futura_class",
            "selection_hint",
            "uncertainty_flags",
        ]
        if col in scored.columns
    ]

    lines: list[str] = [
        f"# {title}",
        "",
        "## Source",
        "",
        f"- Input file: `{source_file or 'not specified'}`",
        "",
        "## Summary",
        "",
        f"- Genes analyzed: **{n_genes}**",
        "",
    ]

    if not class_counts.empty:
        lines.extend([
            "## Class counts",
            "",
            class_counts.to_markdown(index=False),
            "",
        ])

    lines.extend([
        "## Ranked candidates",
        "",
        scored[display_cols].to_markdown(index=False),
        "",
        "## Interpretation notes",
        "",
        "- `adaptive_potential_score` is a transparent v0.1 heuristic score.",
        "- `futura_class` is a preliminary category, not a validated prediction.",
        "- `selection_hint` gives a simplified interpretation from Ka/Ks and pN/pS.",
        "- `uncertainty_flags` indicate missing evidence or caution points.",
        "",
        "## Scientific caution",
        "",
        "FUTURA v0.1 does not predict exact future mutations or genomes.",
        "",
        "> Forecasting is not prophecy. Treat this report as a prioritization scaffold.",
        "",
    ])

    return "\n".join(lines)
