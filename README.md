<p align="center">
  <img src="assets/paleo_futura_banner.png" alt="PALEO-FUTURA project banner" width="100%">
</p>

# PALEO-FUTURA

**AI-assisted evolutionary genomics framework for ancestral inference and future evolutionary forecasting**

> **PALEO asks what evolution left behind; FUTURA asks what evolution may do next.**

PALEO-FUTURA is an early-stage bioinformatics and research-software framework for connecting **ancestral evolutionary inference** with **scenario-based future evolutionary forecasting**.

It is designed to generate, organize, rank, and validate **testable evolutionary hypotheses**.

PALEO-FUTURA is **not** a resurrection engine.  
It is **not** a prophecy machine.  
It is **not** a black-box AI oracle.

It is a scientific time machine with error bars.

---

## Project soul

Modern biology has powerful tools for comparative genomics, phylogenetics, ancestral sequence reconstruction, population genomics, functional genomics, and evolutionary simulation.

However, these analyses often remain separated.

PALEO-FUTURA exists to connect them into a transparent reasoning framework.

The project asks:

- What is ancient?
- What is conserved?
- What has changed?
- What is under selection?
- What is flexible enough to evolve?
- What may adapt under future stress?
- What should be tested experimentally?

The central object of this project is not only a gene, genome, or phenotype.

The central object is an **evolutionary trajectory**.

---

## Concept

PALEO-FUTURA has two complementary modules:

| Module | Direction | Core question | Main output |
|---|---:|---|---|
| **PALEO** | Past | What ancestral biological states can we infer? | ancestral genes/proteins, conserved motifs, gene-family history, regulatory hypotheses |
| **FUTURA** | Future | What evolutionary trajectories are plausible under defined scenarios? | adaptive-potential scores, selection-class predictions, future-risk maps, validation priorities |

Together, they connect:

```text
past evolutionary history
        ↓
present genomic evidence
        ↓
future adaptive potential
        ↓
testable biological hypotheses
```

---

## What PALEO does

**PALEO** stands for:

**Past-Ancestral Life Evolution Oracle**

PALEO is the backward-facing module.

It reconstructs or infers **plausible ancestral states** using comparative and evolutionary genomics.

Planned PALEO tasks include:

- parsing orthogroups and gene families
- extracting target gene-family sequences
- summarizing orthology, paralogy, duplication, and loss patterns
- integrating multiple sequence alignments and gene trees
- parsing ancestral sequence reconstruction outputs
- summarizing Ka/Ks or dN/dS selection history
- annotating domains and conserved motifs
- comparing promoter/regulatory motifs across lineages
- generating uncertainty-aware reports

PALEO may help infer:

- ancestral protein sequences
- ancestral gene-family states
- gene duplication and loss histories
- conserved domains and motifs
- pseudogene relics
- conserved noncoding elements
- regulatory motif evolution
- pathway history
- candidate ancestral functions

PALEO does **not** claim to resurrect extinct organisms.

Preferred wording:

> PALEO infers plausible ancestral states.

Avoid wording:

> PALEO reconstructs extinct life.

---

## What FUTURA does

**FUTURA** stands for:

**Future Evolutionary Trajectory and Utility Risk Analyzer**

FUTURA is the forward-facing module.

It estimates **scenario-dependent evolutionary potential** using comparative genomics, population genomics, functional annotation, environmental context, and forward simulation.

Planned FUTURA tasks include:

- summarizing historical selection metrics such as Ka/Ks or dN/dS
- integrating population-level variation such as SNP density, pN/pS, FST, and allele frequencies
- incorporating stress-expression and functional annotation
- classifying genes into evolutionary response categories
- estimating adaptive potential under user-defined scenarios
- prioritizing candidate alleles, genes, or regulatory regions
- integrating forward evolutionary simulation in later versions
- generating validation recommendations

FUTURA may help estimate:

- genes likely under strong constraint
- genes likely under relaxed selection
- genes with adaptive potential
- regulatory-adaptive candidates
- pathway vulnerabilities under future stress
- candidate alleles or regulatory features for validation
- scenario-specific evolutionary risk

FUTURA does **not** predict exact future genomes.

Preferred wording:

> FUTURA forecasts plausible evolutionary trajectories under defined scenarios.

Avoid wording:

> FUTURA predicts the future of evolution.

---

## Scientific stance

PALEO-FUTURA is built around five principles:

1. **Inference is not resurrection.**
2. **Forecasting is not prophecy.**
3. **AI is an assistant, not an authority.**
4. **Uncertainty is part of the output.**
5. **Every hypothesis should point toward validation.**

The framework prioritizes transparent methods, interpretable scores, uncertainty flags, reproducible workflows, modular architecture, and testable biological hypotheses.

---

## AI usage philosophy

AI can help PALEO-FUTURA by:

- summarizing structured evidence
- prioritizing hypotheses
- explaining uncertainty
- drafting validation strategies
- supporting literature-aware interpretation
- assisting code development and documentation

AI should **not** be used to:

- invent unsupported biological claims
- replace statistical models
- hide uncertainty
- generate black-box conclusions without traceable features
- overrule experimental evidence

The intended role is:

> **AI-assisted interpretation, not AI-driven biological truth.**

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

## First use case: PALEO-FUTURA CAMTA

The first recommended biological use case is the **CAMTA gene family**.

CAMTA genes are suitable because they connect:

- calcium signaling
- transcriptional regulation
- plant development
- stress response
- salinity, heat, drought, and cell wall integrity
- gene-family conservation and diversification
- future plant resilience questions

### PALEO-CAMTA questions

- How conserved are CAMTA domains across land plants?
- What did ancestral CAMTA-like proteins likely look like?
- Which motifs are ancient versus lineage-specific?
- Did certain plant lineages lose, duplicate, or diversify CAMTA genes?
- Are any promoter motifs associated with stress adaptation?
- Which ancestral features are worth reconstructing or testing?

### FUTURA-CAMTA questions

- Which CAMTA genes are likely under strong purifying selection?
- Which CAMTA paralogs show signs of relaxed constraint or adaptive potential?
- Is future adaptation more likely through coding change or regulatory change?
- Which CAMTA-linked stress scenarios should be prioritized?
- Which genes or promoter variants are worth experimental validation?

---

## Repository structure

```text
paleo-futura/
├── README.md
├── CITATION.cff
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── assets/
│   └── paleo_futura_banner.png
├── docs/
│   ├── concept.md
│   ├── paleo.md
│   ├── futura.md
│   ├── file_formats.md
│   ├── ai_usage.md
│   ├── roadmap.md
│   ├── identity.md
│   ├── scientific_boundaries.md
│   ├── design_principles.md
│   ├── architecture.md
│   ├── validation_strategy.md
│   └── first_use_case_CAMTA.md
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

## Scientific boundaries

PALEO-FUTURA is ambitious, but it must remain scientifically careful.

### PALEO can infer

- plausible ancestral gene states
- plausible ancestral protein sequences
- conserved or derived motifs
- gene-family duplication/loss events
- selection-history patterns
- regulatory features worth testing
- evolutionary hypotheses

### PALEO should not claim to

- reconstruct exact ancient genomes
- resurrect extinct organisms
- recover ancient genes perfectly from noncoding DNA
- infer deep-time regulatory systems without uncertainty
- treat one large genome as a complete evolutionary archive

### FUTURA can estimate

- scenario-dependent adaptive potential
- likely constraint or relaxed selection
- candidate genes under future pressure
- regulatory-adaptive candidates
- possible allele-frequency trajectories under assumptions
- future-risk categories
- validation priorities

### FUTURA should not claim to

- predict exact future genomes
- predict exact future mutations
- determine evolutionary destiny
- forecast millions of years with high confidence
- replace population-genetic or ecological validation

---

## Validation philosophy

Every output should answer five questions:

1. What is the prediction or inference?
2. What evidence supports it?
3. What evidence is missing?
4. How uncertain is it?
5. How can it be validated?

Possible validation routes include:

- ancestral protein synthesis
- reporter assays
- motif deletion assays
- CRISPR/base editing
- stress-growth assays
- qPCR/RNA-seq
- population resequencing
- experimental evolution
- protein-structure modeling
- biochemical assays

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

The first development priority is to make a minimal working framework for:

1. PALEO gene-family reporting
2. FUTURA rule-based adaptive-potential scoring
3. uncertainty-aware Markdown/CSV output
4. plant stress adaptation demonstration

---

## Guiding sentence

> **PALEO-FUTURA is a scientific time machine with error bars.**
