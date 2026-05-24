# Architecture

PALEO-FUTURA is designed as a modular framework.

## High-level structure

```text
Input data
   ↓
Quality control
   ↓
Evolutionary Evidence Matrix
   ↓
PALEO modules      FUTURA modules
   ↓                    ↓
Ancestral hypotheses   Future adaptive hypotheses
   ↓                    ↓
Uncertainty layer
   ↓
Validation planner
   ↓
Reports
```

---

## Shared Evidence Matrix

The Evidence Matrix is the shared data layer.

Each row may represent:

- a gene
- a transcript
- an orthogroup
- a regulatory element
- a protein domain
- a candidate allele
- a pathway module

Suggested columns:

```text
gene_id
species
orthogroup
gene_family
protein_id
cds_id
domain_summary
copy_number
synteny_status
kaks
dn_ds
pnps
snp_density
fst
tajimas_d
stress_log2fc
expression_specificity
promoter_motifs
te_proximity
repeat_overlap
protein_constraint
network_centrality
scenario
evidence_quality
uncertainty_flags
```

---

## PALEO module flow

```text
orthogroups
   ↓
gene family extraction
   ↓
alignment and gene tree
   ↓
ancestral reconstruction
   ↓
selection-history parsing
   ↓
domain and motif interpretation
   ↓
ancestral hypothesis report
```

---

## FUTURA module flow

```text
feature table
   ↓
scenario definition
   ↓
constraint scoring
   ↓
adaptive-potential scoring
   ↓
selection-class prediction
   ↓
optional forward simulation
   ↓
future hypothesis report
```

---

## Report types

PALEO-FUTURA should eventually produce:

```text
paleo_report.md
futura_report.md
evidence_matrix.csv
uncertainty_flags.csv
validation_priorities.csv
candidate_summary.md
```

---

## Recommended first implementation

Start with:

1. simple CSV/TSV input
2. deterministic rule-based scoring
3. Markdown report generation
4. toy examples
5. unit tests
6. no heavy AI dependency yet

Then later add:

1. workflow automation
2. ML models
3. simulation integration
4. interactive dashboard
5. LLM-assisted interpretation layer
