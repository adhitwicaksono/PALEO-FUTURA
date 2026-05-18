from pathlib import Path
from typing import Dict


def read_fasta(path: str | Path) -> Dict[str, str]:
    """Read a FASTA file into a dictionary of {header: sequence}."""
    records: Dict[str, str] = {}
    current_header = None
    chunks = []

    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_header is not None:
                    records[current_header] = "".join(chunks)
                current_header = line[1:]
                chunks = []
            else:
                chunks.append(line)

    if current_header is not None:
        records[current_header] = "".join(chunks)

    return records
