import pickle
import numpy as np

import pandas as pd
import yaml

from src.config.paths import Paths
from src.utils import read_csv, save_csv


def show_trends():
    paths: Paths = Paths()
    params = yaml.safe_load(open(paths.DEFAULT_YAML_PATH)).get("evaluate")
    X_test = read_csv(paths.PREPARED_DIR / "X_test")
    y_test = read_csv(paths.PREPARED_DIR / "y_test")
    with open(paths.MODELS_DIR / f"{params.get('model_name')}.p", "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(X_test)
    
    trends = y_test.copy().rename(columns={"price": "current_price"})
    trends["suggested_price"] = y_pred.round(2)
    trends["trend"] = (trends["suggested_price"] - trends["current_price"])
    
    
    paths.OUTPUT_DIR.mkdir(exist_ok=True)
    save_csv(trends,
        paths.OUTPUT_DIR / "trends", index=True
    )
