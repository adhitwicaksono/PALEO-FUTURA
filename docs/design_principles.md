# Design Principles

## 1. Start transparent before becoming intelligent

The first versions of PALEO-FUTURA should use explicit rules, readable scoring, and traceable feature tables.

Machine learning can come later.

A transparent weak model is better than an impressive black box that cannot be trusted.

---

## 2. Treat uncertainty as output

Uncertainty should not be hidden in logs.

It should appear in reports, tables, and candidate rankings.

Examples of uncertainty flags:

- poor alignment quality
- weak orthology confidence
- paralogy ambiguity
- missing population data
- low gene annotation confidence
- repeat overlap
- low ancestral posterior probability
- extrapolation beyond training data
- scenario mismatch

---

## 3. Separate evidence from interpretation

PALEO-FUTURA should store raw evidence separately from generated interpretation.

Example:

```text
feature_table.csv       # evidence
score_table.csv         # model output
interpretation.md       # explanation
validation_plan.md      # proposed experiments
```

---

## 4. Make every module replaceable

The framework should not depend permanently on one tool.

For example:

- OrthoFinder may be replaced by another orthology tool
- PAML may be replaced by HyPhy or IQ-TREE outputs
- rule-based scoring may be replaced by ML
- SLiM may be complemented by other simulators

The architecture should be modular.

---

## 5. Prioritize biological validation

PALEO-FUTURA should always ask:

> What experiment would make this claim stronger or weaker?

Validation examples:

- ancestral protein synthesis
- reporter assays
- CRISPR/base editing
- stress-growth assays
- qPCR/RNA-seq
- population resequencing
- experimental evolution
- protein-structure modeling
- biochemical assays

---

## 6. Avoid Jurassic World science

Do not treat DNA as magic.

Do not treat genes as simple trait cards.

Do not treat AI predictions as reality.

Do not ignore development, regulation, ecology, population structure, or uncertainty.

---

## 7. Build for plant science first

The long-term idea may be broad, but the first build should be grounded in plant biology.

Suggested first domain:

- CAMTA/CaM/CML evolution
- plant stress response
- cell wall integrity
- salinity and heat adaptation
- regulatory evolution
- gene-family expansion and loss
