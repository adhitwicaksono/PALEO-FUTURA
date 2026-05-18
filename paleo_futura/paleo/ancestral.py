from pathlib import Path
from paleo_futura.utils.fasta import read_fasta


def read_ancestral_fasta(path: str | Path) -> dict:
    """Read ancestral reconstructed sequences from FASTA."""
    return read_fasta(path)
