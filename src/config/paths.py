from pathlib import Path
from typing import NamedTuple


class Paths(NamedTuple):
    DATA_DIR = Path("data")
    INPUT_DIR = DATA_DIR / "input"
    OUTPUT_DIR = DATA_DIR / "output"
    PREPARED_DIR = DATA_DIR / "prepared"
    YAML_DIR = Path("src/config")
    DEFAULT_YAML_PATH = YAML_DIR / "default.yaml"
