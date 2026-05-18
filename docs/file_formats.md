# File Formats

This document defines planned input and output formats for PALEO-FUTURA.

## FASTA

Recommended header format:

```text
>species_id|gene_id|optional_annotation
```

## Orthogroup table

Simple CSV/TSV format for v0.1:

```text
orthogroup,species,gene_id,sequence_id,notes
OG0001,Arabidopsis_thaliana,AT1G67310,AT1G67310.1,CAMTA
```

## Gene feature table

For FUTURA v0.1:

```text
gene_id,orthogroup,kaks,pnps,snp_density,stress_log2fc,te_proximity,gene_family_size,domain_count,scenario
```

## Selection summary table

```text
gene_id,orthogroup,method,kaks_or_dn_ds,selection_class,p_value,notes
```

## Scenario definition file

YAML format proposed for FUTURA:

```yaml
scenario_name: salinity_heat
species: rice
stressors:
  - salinity
  - heat
time_horizon: short_term
notes: "Toy scenario for FUTURA v0.1"
```

## Output files

```text
paleo_report.md
paleo_summary.csv
futura_report.md
futura_scores.csv
uncertainty_flags.csv
validation_priorities.csv
```
