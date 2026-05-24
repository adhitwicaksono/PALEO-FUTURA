<p align="center">
  <img src="assets/paleo_futura_banner.png" alt="Paleo-Futura project banner" width="100%">
</p>

# PALEO-FUTURA

**AI-assisted evolutionary genomics framework for ancestral inference and future evolutionary forecasting**

> **PALEO asks what evolution left behind; FUTURA asks what evolution may do next.**

PALEO-FUTURA is an early-stage bioinformatics framework for connecting **ancestral evolutionary inference** with **scenario-based future evolutionary forecasting**.

It is designed to generate **testable evolutionary hypotheses**, not deterministic claims about extinct organisms or future genomes.

---

## Concept

PALEO-FUTURA has two complementary modules:

| Module | Direction | Core question | Main output |
|---|---:|---|---|
| **PALEO** | Past | What ancestral biological states can we infer? | ancestral genes/proteins, conserved motifs, gene-family history, regulatory hypotheses |
| **FUTURA** | Future | What evolutionary trajectories are plausible under defined scenarios? | adaptive-potential scores, selection-class predictions, future-risk maps, validation priorities |

---

## What PALEO does

**PALEO** stands for:

**Past-Ancestral Life Evolution Oracle**

PALEO reconstructs or infers plausible ancestral states using comparative and evolutionary genomics.

Planned PALEO tasks:

- parse orthogroups and gene families
- extract target gene-family sequences
- summarize orthology/paralogy and duplication/loss patterns
- integrate multiple sequence alignments and gene trees
- parse ancestral sequence reconstruction outputs
- summarize Ka/Ks or dN/dS selection history
- annotate domains and conserved motifs
- compare promoter/regulatory motifs across lineages
- generate uncertainty-aware reports

PALEO does **not** claim to resurrect extinct organisms.

---

## What FUTURA does

**FUTURA** stands for:

**Future Evolutionary Trajectory and Utility Risk Analyzer**

FUTURA estimates scenario-dependent evolutionary potential using comparative genomics, population genomics, functional annotation, and forward simulation.

Planned FUTURA tasks:

- summarize historical selection metrics such as Ka/Ks or dN/dS
- integrate population-level variation such as SNP density, pN/pS, FST, and allele frequencies
- incorporate stress-expression and functional annotation
- classify genes into evolutionary response categories
- estimate adaptive potential under user-defined scenarios
- prioritize candidate alleles, genes, or regulatory regions
- integrate forward evolutionary simulation in later versions
- generate validation recommendations

FUTURA does **not** predict exact future genomes.

---

## Scientific stance

PALEO-FUTURA is built around three principles:

1. **Inference is not resurrection.**
2. **Forecasting is not prophecy.**
3. **Every prediction needs uncertainty and validation.**

The framework prioritizes transparent methods, interpretable scores, uncertainty flags, reproducible workflows, and testable biological hypotheses.

---

## Initial biological focus

The first intended use case is:

> **Plant stress adaptation, especially calcium signaling, CAMTA/CaM/CML gene families, cell wall integrity, salinity, heat, drought, and stress-responsive regulatory evolution.**

Possible first demonstrations:

- CAMTA gene-family evolution across land plants
- salinity-response gene adaptive potential in rice or Arabidopsis relatives
- regulatory motif evolution in plant stress-response genes
- gene retention/loss and evolutionary constraint in unusual plant genomes

---

## Repository structure

```text
paleo-futura/
├── README.md
├── CITATION.cff
├── pyproject.toml
├── requirements.txt
├── docs/
│   ├── concept.md
│   ├── paleo.md
│   ├── futura.md
│   ├── file_formats.md
│   ├── ai_usage.md
│   └── roadmap.md
├── examples/
│   ├── toy_gene_family/
│   ├── paleo_camta_demo/
│   └── futura_salinity_demo/
├── paleo_futura/
│   ├── paleo/
│   ├── futura/
│   └── utils/
├── tests/
└── workflows/
```

---

## v0.1 scope

The first release is intentionally humble.

### PALEO v0.1

- parse simple orthogroup tables
- read FASTA sequences
- summarize gene-family membership
- accept precomputed alignment/tree files
- parse simple ancestral sequence outputs
- parse selection-summary tables
- generate Markdown and CSV reports

### FUTURA v0.1

- read gene-feature tables
- score adaptive potential using transparent rule-based scoring
- classify genes into preliminary categories:
  - constrained
  - relaxed/neutral
  - adaptive potential
  - regulatory-adaptive
  - uncertain
- generate Markdown and CSV reports

---

## Roadmap

| Version | Goal |
|---|---|
| **v0.1** | repository skeleton, toy examples, PALEO/FUTURA report prototypes |
| **v0.2** | PALEO gene-family workflow |
| **v0.3** | FUTURA adaptive-potential scoring workflow |
| **v0.4** | SLiM forward-simulation integration |
| **v0.5** | plant stress adaptation demo |
| **v1.0** | reproducible PALEO-FUTURA framework with documentation, examples, and validation recommendations |

---

## Author

**Adhityo Wicaksono**  
Plant molecular biologist, bioinformatician, and evolutionary/synthetic biology enthusiast.

---

## AI usage declaration

This repository was conceptualized and drafted with assistance from AI tools, including ChatGPT/Helios, for brainstorming, documentation drafting, coding scaffolds, and conceptual organization.

All scientific claims, code, analyses, interpretations, and final repository decisions should be reviewed, tested, and validated by the human author before use in research, publication, or applied biological decision-making.

---

## Current status

🚧 **Early concept / seed repository**

PALEO-FUTURA is not yet a validated analysis tool. The current goal is to build a transparent, modular, and testable foundation.
