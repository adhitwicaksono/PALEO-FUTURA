## Quick start

Install in editable mode:

```bash
pip install -e .
```

Run the PALEO toy example:

```bash
paleo-futura paleo summarize examples/toy_gene_family/orthogroups.csv --out results/paleo_demo
```

Run the FUTURA toy example:

```bash
paleo-futura futura score examples/futura_salinity_demo/gene_features.csv --out results/futura_demo
```

Expected outputs:

```text
results/paleo_demo/paleo_orthogroup_summary.csv
results/paleo_demo/paleo_report.md
results/futura_demo/futura_scores.csv
results/futura_demo/futura_report.md
```

Run tests:

```bash
pytest
```
