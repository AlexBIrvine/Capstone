# Steps: 
# ------
# Import data
# Clean data
# Split data into training/tests (separate the result from the rest (in our case, ratings))
# Create a model
# train model
# make predictions
# evaluate and improve

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from CSV_tools import data_prep

df = data_prep()


kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'fuelType']])

df['Clusters'].kmeans.labels_

print(df)
