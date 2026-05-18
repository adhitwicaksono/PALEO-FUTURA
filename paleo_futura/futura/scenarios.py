from dataclasses import dataclass
from typing import List


@dataclass
class Scenario:
    """Simple FUTURA scenario definition."""
    name: str
    stressors: List[str]
    species: str | None = None
    notes: str | None = None
