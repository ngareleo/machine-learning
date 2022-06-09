import os
import tarfile
import numpy as np
from sklearn.datasets import fetch_openml
from six.moves import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

MNIST_PATH = os.path.join("datasets", "mnist")


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)

    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def get_mnist_data(file_location=MNIST_PATH):
    mnist = fetch_openml("mnist_784", version=1)
    digits, labels = np.array(mnist.get("data")), np.array(mnist.get("target"))

    return (digits, labels)


if __name__ == "__main__":

    fetch_housing_data()