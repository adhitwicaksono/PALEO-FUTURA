"""Command-line interface for PALEO-FUTURA v0.1."""

from __future__ import annotations

import argparse
from pathlib import Path

from paleo_futura.paleo.orthogroups import read_orthogroups, summarize_orthogroups
from paleo_futura.paleo.report import make_paleo_report
from paleo_futura.futura.features import read_gene_features
from paleo_futura.futura.scoring import score_feature_table
from paleo_futura.futura.report import make_futura_report


def _ensure_output_dir(path: str | Path) -> Path:
    outdir = Path(path)
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir


def run_paleo_summarize(args: argparse.Namespace) -> None:
    """Run PALEO orthogroup summary workflow."""
    outdir = _ensure_output_dir(args.out)

    orthogroups = read_orthogroups(args.orthogroups)
    summary = summarize_orthogroups(
        orthogroups,
        duplication_threshold=args.duplication_threshold,
    )

    summary_path = outdir / "paleo_orthogroup_summary.csv"
    report_path = outdir / "paleo_report.md"

    summary.to_csv(summary_path, index=False)
    report_path.write_text(
        make_paleo_report(
            summary,
            title="PALEO Orthogroup Summary Report",
            source_file=str(args.orthogroups),
        ),
        encoding="utf-8",
    )

    print(f"[PALEO] Wrote summary: {summary_path}")
    print(f"[PALEO] Wrote report:  {report_path}")


def run_futura_score(args: argparse.Namespace) -> None:
    """Run FUTURA adaptive-potential scoring workflow."""
    outdir = _ensure_output_dir(args.out)

    features = read_gene_features(args.features)
    scored = score_feature_table(features)

    scores_path = outdir / "futura_scores.csv"
    report_path = outdir / "futura_report.md"

    scored.to_csv(scores_path, index=False)
    report_path.write_text(
        make_futura_report(
            scored,
            title="FUTURA Adaptive-Potential Report",
            source_file=str(args.features),
        ),
        encoding="utf-8",
    )

    print(f"[FUTURA] Wrote scores: {scores_path}")
    print(f"[FUTURA] Wrote report: {report_path}")


def build_parser() -> argparse.ArgumentParser:
    """Build CLI parser."""
    parser = argparse.ArgumentParser(
        prog="paleo-futura",
        description="PALEO-FUTURA v0.1 command-line interface.",
    )
    subparsers = parser.add_subparparsers if False else parser.add_subparsers
    top = subparsers(dest="module", required=True)

    paleo = top.add_parser("paleo", help="Run PALEO workflows.")
    paleo_sub = paleo.add_subparsers(dest="command", required=True)

    paleo_summary = paleo_sub.add_parser(
        "summarize",
        help="Summarize orthogroup membership and uncertainty flags.",
    )
    paleo_summary.add_argument(
        "orthogroups",
        type=Path,
        help="Input orthogroup table in CSV or TSV format.",
    )
    paleo_summary.add_argument(
        "--out",
        type=Path,
        default=Path("results/paleo_demo"),
        help="Output directory. Default: results/paleo_demo",
    )
    paleo_summary.add_argument(
        "--duplication-threshold",
        type=int,
        default=2,
        help="Genes per species above this value are flagged as duplication. Default: 2",
    )
    paleo_summary.set_defaults(func=run_paleo_summarize)

    futura = top.add_parser("futura", help="Run FUTURA workflows.")
    futura_sub = futura.add_subparsers(dest="command", required=True)

    futura_score = futura_sub.add_parser(
        "score",
        help="Score gene adaptive potential from a feature table.",
    )
    futura_score.add_argument(
        "features",
        type=Path,
        help="Input gene feature table in CSV or TSV format.",
    )
    futura_score.add_argument(
        "--out",
        type=Path,
        default=Path("results/futura_demo"),
        help="Output directory. Default: results/futura_demo",
    )
    futura_score.set_defaults(func=run_futura_score)

    return parser


def main(argv: list[str] | None = None) -> None:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
