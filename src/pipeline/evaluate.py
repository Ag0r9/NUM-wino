import json
import pickle

import yaml
from pandas import read_csv

from src.config.paths import Paths
from src.utils import get_regression_metrics


def evaluate_model():
    paths: Paths = Paths()
    params = yaml.safe_load(open(paths.DEFAULT_YAML_PATH)).get("evaluate")
    X_test, y_test = read_csv(paths.PREPARED_DIR / "X_test"), read_csv(
        paths.PREPARED_DIR / "y_test"
    )
    with open(paths.MODELS_DIR / f"{params.get('model name')}.p", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)

    max_error, mse, r2 = get_regression_metrics(y_test, y_pred)
    with open(paths.MODELS_DIR / f"{params.get('model name')}_METADATA", "w") as f:
        json.dump({"max_error": max_error, "mse": mse, "r2": r2}, f)
