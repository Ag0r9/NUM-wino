from functools import reduce

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split

from src.config.paths import Paths
from src.utils import read_csv, save_csv


def prepare_data():
    paths: Paths = Paths()
    params = yaml.safe_load(open(paths.DEFAULT_YAML_PATH)).get("prepare")
    dfs = [
        read_csv(paths.INPUT_DIR / filename) for filename in params.get("name files")
    ]
    df = reduce(lambda left, right: pd.merge(left, right, on="Id"), dfs)
    datasets = train_test_split(
        df[params.get("x columns")],
        df[params.get("target")],
        test_size=params.get("split"),
    )
    paths.PREPARED_DIR.mkdir(parents=True, exist_ok=True)
    filenames = ["X_train", "X_test", "y_train", "y_test"]
    for dataset, filename in zip(datasets, filenames):
        save_csv(dataset, paths.PREPARED_DIR / filename)
