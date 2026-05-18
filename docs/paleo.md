# PALEO

**Past-Ancestral Life Evolution Oracle**

PALEO is the backward-facing module of PALEO-FUTURA.

It infers plausible ancestral gene, protein, regulatory, and pathway states from comparative evolutionary data.

## Main inputs

- proteome FASTA files
- CDS FASTA files
- genome annotation files, such as GFF3 or GTF
- orthogroup tables
- gene trees
- species trees
- multiple sequence alignments
- selection-analysis outputs
- ancestral sequence reconstruction outputs
- domain and motif annotations
- promoter sequences
- expression data, if available

## Main modules

1. **Orthogroup parsing**
   - reads orthology results
   - identifies target gene families
   - separates likely orthologs and paralogs

2. **Gene-family extraction**
   - extracts protein and CDS sequences for selected gene families

3. **Alignment and tree integration**
   - accepts or creates alignments
   - accepts or creates gene trees
   - flags suspicious long branches and fragments

4. **Ancestral reconstruction parsing**
   - reads reconstructed ancestral sequences
   - summarizes site-level uncertainty where available

5. **Selection-history summary**
   - summarizes dN/dS or Ka/Ks
   - flags positive selection, purifying selection, and relaxed constraint

6. **Regulatory archaeology**
   - compares promoter motifs
   - maps conserved and lineage-specific regulatory candidates
   - flags repeat-associated regulatory elements

7. **Report generation**
   - generates Markdown, CSV, and later HTML reports

## Example PALEO question

> What did an ancestral CAMTA-like protein probably look like before diversification in flowering plants?

## Output philosophy

PALEO should output plausible ancestral states, confidence scores, uncertainty flags, biological interpretation, and validation suggestions.
