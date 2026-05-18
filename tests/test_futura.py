import pandas as pd
from paleo_futura.futura.scoring import score_feature_table


def test_score_feature_table():
    df = pd.DataFrame({
        "gene_id": ["g1", "g2"],
        "kaks": [0.2, 1.5],
        "pnps": [0.1, 1.2],
        "snp_density": [0.1, 1.0],
        "stress_log2fc": [0.5, 3.0],
        "te_proximity": [False, True],
        "gene_family_size": [1, 4]
    })
    out = score_feature_table(df)
    assert "adaptive_potential_score" in out.columns
    assert out.loc[out["gene_id"] == "g2", "adaptive_potential_score"].iloc[0] > out.loc[out["gene_id"] == "g1", "adaptive_potential_score"].iloc[0]
