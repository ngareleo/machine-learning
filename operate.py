import pandas as pd
from loader import HOUSING_PATH
from os.path import join
import matplotlib.pyplot as plt


def load_housing_data(filename, housing_path=HOUSING_PATH):
    csv_path = join(housing_path, filename)
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    housing_data = load_housing_data(filename="housing.csv")
    u = housing_data.describe()
    print(u)