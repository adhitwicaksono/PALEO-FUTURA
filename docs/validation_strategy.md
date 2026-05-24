# Validation Strategy

PALEO-FUTURA is only useful if its outputs can guide validation.

This document defines possible validation routes.

---

## PALEO validation

### 1. Ancestral protein reconstruction

Prediction:

> An ancestral protein sequence had a specific domain or functional property.

Validation:

- synthesize ancestral sequence
- express protein
- test folding/stability
- test biochemical activity
- test interaction partners
- compare with modern proteins

### 2. Regulatory motif reconstruction

Prediction:

> A promoter motif is ancestral, derived, or lineage-specific.

Validation:

- promoter-reporter assay
- motif deletion assay
- transient expression
- stable transgenic line
- TF-binding assay
- ATAC-seq or ChIP-seq if available

### 3. Gene-family history

Prediction:

> A gene duplication, loss, or expansion is biologically meaningful.

Validation:

- synteny analysis
- improved genome annotation
- PCR confirmation if needed
- expression analysis
- functional redundancy testing

---

## FUTURA validation

### 1. Adaptive-potential prediction

Prediction:

> A gene has high adaptive potential under a scenario.

Validation:

- stress assay
- mutant or edited line
- natural accession comparison
- allele-specific expression
- association with phenotype

### 2. Regulatory adaptation prediction

Prediction:

> Future adaptation may occur through promoter/regulatory change rather than coding change.

Validation:

- promoter haplotype comparison
- reporter assay
- eQTL analysis
- CRISPR promoter editing
- stress-induced expression profiling

### 3. Candidate allele prediction

Prediction:

> A specific allele or variant may be beneficial under a future scenario.

Validation:

- base editing
- introgression line
- growth chamber stress trial
- reciprocal transplant, if ecological
- allele-frequency monitoring

### 4. Simulation prediction

Prediction:

> An allele may increase under defined selection and population assumptions.

Validation:

- experimental evolution
- artificial selection experiment
- population resequencing
- comparison with known local adaptation datasets

---

## Validation priority scoring

Candidate validation priority should consider:

- strength of evidence
- uncertainty level
- biological relevance
- experimental feasibility
- novelty
- connection to phenotype
- availability of material
- risk of annotation artifact

A high-scoring prediction with no feasible validation should be marked as exploratory, not priority.
