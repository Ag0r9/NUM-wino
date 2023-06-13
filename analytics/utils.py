import numpy as np
import pandas as pd

from src.config.paths import Paths
from src.utils import read_csv, save_csv


def calculate_wine_price():
    paths: Paths = Paths()
    data = read_csv(paths.INPUT_DIR / "WineQT.csv")
    data["price"] = (data["quality"] * 10) + (np.random.rand(data.shape[0]) * 10 )
    data["price"] = data["price"].round(2)
    save_csv(data.loc[:, ["Id", "price"]], paths.INPUT_DIR / "WinePrices.csv")
