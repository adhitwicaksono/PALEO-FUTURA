"""Markdown report generation for PALEO v0.1."""

from __future__ import annotations

import pandas as pd


def make_paleo_report(
    summary: pd.DataFrame,
    title: str = "PALEO Report",
    source_file: str | None = None,
) -> str:
    """Create a Markdown PALEO report from an orthogroup summary."""
    n_orthogroups = len(summary)
    n_possible_dup = int((summary["paleo_status"] == "possible_paralogous_family").sum()) if "paleo_status" in summary else 0

    lines: list[str] = [
        f"# {title}",
        "",
        "## Source",
        "",
        f"- Input file: `{source_file or 'not specified'}`",
        "",
        "## Summary",
        "",
        f"- Orthogroups analyzed: **{n_orthogroups}**",
        f"- Orthogroups flagged as possible paralogous/duplicated families: **{n_possible_dup}**",
        "",
        "## Orthogroup table",
        "",
        summary.to_markdown(index=False),
        "",
        "## Interpretation notes",
        "",
        "- `single_or_low_copy_family` means no strong duplication signal was detected in this toy summary.",
        "- `possible_paralogous_family` means at least one species has multiple genes in the same orthogroup.",
        "- These flags are preliminary and should be checked with alignment, gene-tree, species-tree, and synteny evidence.",
        "",
        "## Scientific caution",
        "",
        "PALEO v0.1 summarizes orthogroup structure only. It does not perform ancestral reconstruction yet.",
        "",
        "> Inference is not resurrection. Treat this report as a hypothesis scaffold.",
        "",
    ]
    return "\n".join(lines)
