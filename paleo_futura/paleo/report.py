import pandas as pd


def make_paleo_markdown(summary: pd.DataFrame, title: str = "PALEO Report") -> str:
    """Create a simple Markdown report from a PALEO summary table."""
    lines = [
        f"# {title}",
        "",
        "## Summary",
        "",
        summary.to_markdown(index=False),
        "",
        "## Notes",
        "",
        "- This is a v0.1 prototype report.",
        "- Interpret all ancestral and selection results as hypotheses.",
        "- Add uncertainty and validation notes before scientific use.",
    ]
    return "
".join(lines)
