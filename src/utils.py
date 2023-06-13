from pathlib import Path

import pandas as pd
from sklearn.metrics import max_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from src.config.paths import Paths


def save_csv(data: pd.DataFrame, path: Path):
    data.to_csv(path, index=False, encoding="utf-8", sep=",")


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8", sep=",")


def get_regression_metrics(y_test, y_pred):
    return (
        max_error(y_test, y_pred),
        mean_squared_error(y_test, y_pred),
        r2_score(y_test, y_pred),
    )
