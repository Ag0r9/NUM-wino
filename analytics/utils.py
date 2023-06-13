import numpy as np
import pandas as pd

from src.config.paths import Paths
from src.utils import save_csv


def calculate_wine_price():
    paths: Paths = Paths()
    data = pd.read_csv(paths.INPUT_DIR / "WineQT.csv")
    random_numbers = np.random.normal(loc=0.5, scale=0.1, size=data.shape[0])
    random_numbers = np.clip(random_numbers, 0, 1)
    data["price"] = random_numbers * data["quality"] * 10
    data["price"] = data["price"].round()
    save_csv(data.loc[:, ["Id", "price"]], paths.INPUT_DIR / "WinePrices.csv")

    
