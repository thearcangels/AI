##classification###
from matplotlib import pyplot as plt
import numpy as np

##load data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()

##load_iris returns an object with several fields
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names


