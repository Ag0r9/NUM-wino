from pathlib import Path
from typing import NamedTuple


class Paths(NamedTuple):
    INPUT_DIR = Path("data/input")
    OUTPUT_DIR = Path("data/output")