from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

def save_csv(data: pd.DataFrame, path: Path):
    data.to_csv(path, index=False, encoding="utf-8")


def split_data(data_path: Path, target: str, test_size: float, random_state: int):
    data = pd.read_csv(data_path)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
