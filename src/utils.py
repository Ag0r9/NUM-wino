from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config.paths import Paths


def save_csv(data: pd.DataFrame, path: Path):
    data.to_csv(path, index=False, encoding="utf-8", sep=",")


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8", sep=",")
