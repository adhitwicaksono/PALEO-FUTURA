import pandas as pd


def make_futura_markdown(scored: pd.DataFrame, title: str = "FUTURA Report") -> str:
    """Create a simple Markdown report from a FUTURA scored table."""
    lines = [
        f"# {title}",
        "",
        "## Ranked candidates",
        "",
        scored.sort_values("adaptive_potential_score", ascending=False).to_markdown(index=False),
        "",
        "## Notes",
        "",
        "- This is a v0.1 prototype report.",
        "- Scores are heuristic and not validated biological predictions.",
        "- Use this output for hypothesis prioritization only.",
    ]
    return "
".join(lines)
