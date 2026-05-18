import pandas as pd
from paleo_futura.paleo.orthogroups import summarize_orthogroups
from paleo_futura.paleo.selection import classify_kaks


def test_summarize_orthogroups():
    df = pd.DataFrame({
        "orthogroup": ["OG1", "OG1", "OG2"],
        "species": ["A", "B", "A"],
        "gene_id": ["g1", "g2", "g3"]
    })
    out = summarize_orthogroups(df)
    assert "n_species" in out.columns
    assert out.loc[out["orthogroup"] == "OG1", "n_species"].iloc[0] == 2


def test_classify_kaks():
    assert classify_kaks(0.2) == "purifying"
    assert classify_kaks(1.0) == "neutral_or_relaxed"
    assert classify_kaks(1.5) == "positive_candidate"
