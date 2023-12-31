import pickle

import yaml
from sklearn.ensemble import RandomForestRegressor

from src.config.paths import Paths
from src.utils import read_csv


def train_model():
    paths: Paths = Paths()
    params = yaml.safe_load(open(paths.DEFAULT_YAML_PATH)).get("train")
    X_train = read_csv(paths.PREPARED_DIR / "X_train")
    y_train = read_csv(paths.PREPARED_DIR / "y_train")
    model = RandomForestRegressor(**params.get("model_params"))
    model.fit(X_train, y_train)
    paths.MODELS_DIR.mkdir(exist_ok=True)
    with open(paths.MODELS_DIR / f"{params.get('model_name')}.p", "wb") as f:
        pickle.dump(model, f)
