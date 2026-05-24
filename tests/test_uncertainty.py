import pandas as pd

from paleo_futura.utils.uncertainty import futura_gene_flags, paleo_orthogroup_flags


def test_futura_gene_flags_missing_values():
    row = pd.Series({"gene_id": "g1", "scenario": ""})
    flags = futura_gene_flags(row)

    assert "missing_kaks" in flags
    assert "missing_scenario" in flags


def test_paleo_orthogroup_flags_low_species():
    flags = paleo_orthogroup_flags(
        n_species=1,
        n_genes=1,
        max_genes_per_species=1,
    )

    assert "low_species_count" in flags
