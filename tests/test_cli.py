from pathlib import Path

from paleo_futura.cli import main


def test_cli_paleo_summarize(tmp_path):
    infile = tmp_path / "orthogroups.csv"
    infile.write_text(
        "orthogroup,species,gene_id\n"
        "OG1,A,g1\n"
        "OG1,B,g2\n",
        encoding="utf-8",
    )

    outdir = tmp_path / "paleo_out"
    main(["paleo", "summarize", str(infile), "--out", str(outdir)])

    assert (outdir / "paleo_orthogroup_summary.csv").exists()
    assert (outdir / "paleo_report.md").exists()


def test_cli_futura_score(tmp_path):
    infile = tmp_path / "features.csv"
    infile.write_text(
        "gene_id,kaks,pnps,snp_density,stress_log2fc,te_proximity,gene_family_size,scenario\n"
        "g1,1.2,1.0,0.5,2.0,true,3,salinity\n",
        encoding="utf-8",
    )

    outdir = tmp_path / "futura_out"
    main(["futura", "score", str(infile), "--out", str(outdir)])

    assert (outdir / "futura_scores.csv").exists()
    assert (outdir / "futura_report.md").exists()
