import pandas as pd

from paleo_futura.paleo.orthogroups import summarize_orthogroups
from paleo_futura.paleo.orthogroups import read_orthogroups


def test_summarize_orthogroups_flags_duplication():
    df = pd.DataFrame({
        "orthogroup": ["OG1", "OG1", "OG1", "OG2"],
        "species": ["A", "A", "B", "A"],
        "gene_id": ["g1", "g2", "g3", "g4"],
    })

    summary = summarize_orthogroups(df)
    og1 = summary[summary["orthogroup"] == "OG1"].iloc[0]

    assert og1["n_species"] == 2
    assert og1["n_genes"] == 3
    assert og1["paleo_status"] == "possible_paralogous_family"
    assert "possible_duplication_or_paralogy" in og1["uncertainty_flags"]


def test_read_orthogroups_missing_file_raises(tmp_path):
    missing = tmp_path / "missing.csv"

    try:
        read_orthogroups(missing)
    except FileNotFoundError:
        assert True
    else:
        assert False
