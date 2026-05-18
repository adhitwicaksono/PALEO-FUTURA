# FUTURA

**Future Evolutionary Trajectory and Utility Risk Analyzer**

FUTURA is the forward-facing module of PALEO-FUTURA.

It estimates scenario-dependent evolutionary potential and candidate future adaptation using comparative genomics, population genomics, functional annotation, and simulation.

## Main inputs

- gene annotation table
- orthogroup table
- dN/dS or Ka/Ks values
- pN/pS values, if available
- SNP/VCF data
- allele-frequency data
- FST, Tajima's D, and other population-genetic summaries
- stress-expression data
- GO, KEGG, MapMan, or pathway annotation
- promoter/regulatory motif data
- TE proximity or repeat annotations
- protein-domain and structural constraint data
- environmental or experimental scenario definition

## Main modules

1. **Feature integration**
   - combines comparative, population, regulatory, and functional data

2. **Scenario definition**
   - defines stress or future conditions such as heat, drought, salinity, pathogen pressure, radiation, or microgravity

3. **Constraint scoring**
   - estimates whether genes are likely constrained or evolvable

4. **Adaptive-potential scoring**
   - ranks genes by likely relevance to a scenario and capacity for evolutionary response

5. **Selection-class prediction**
   - classifies genes as constrained, relaxed, adaptive-potential, regulatory-adaptive, or uncertain

6. **Forward simulation**
   - later versions may integrate SLiM or related tools to model allele-frequency trajectories

7. **Report generation**
   - generates ranked candidate lists and validation recommendations

## Example FUTURA question

> Which rice genes may have high adaptive potential under future salinity and heat stress?

## Output philosophy

FUTURA should output probability-based predictions, scenario dependence, uncertainty flags, feature explanations, and validation priorities.
