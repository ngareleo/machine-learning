import pandas as pd
from loader import HOUSING_PATH
from os.path import join
import matplotlib.pyplot as plt


def load_housing_data(filename, housing_path=HOUSING_PATH):
    csv_path = join(housing_path, filename)
    return pd.read_csv(csv_path)


if __name__ == "__main__":
    housing_data = load_housing_data(filename="housing.csv")
    housing_data.plot(
        kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.4,
        s=housing_data["population"]/100,
        label="population",
        figsize=(10, 7),
        c="median_house_value",
        cmap=plt.get_cmap("jet"),
        colorbar=True
        )
    plt.show()