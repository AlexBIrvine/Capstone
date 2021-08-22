import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from CSV_tools import data_prep, categorical_values

import json

data_prep()

cluster_d = {}

df = pd.read_csv('./CarRentalDataCleaned.csv')

# Run KMeans on fuel type & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'fuelType_cat']])
cluster_d['fuelType_Clusters'] = kmeans.labels_

# Run KMeans on trips taken & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'renterTripsTaken']])
cluster_d['tripsTaken_Clusters'] = kmeans.labels_

# Run KMeans on daily rate & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'rate.daily']])
cluster_d['dailyRate_Clusters'] = kmeans.labels_

# Run KMeans on vehicle make & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'vehicle.make_cat']])
cluster_d['vehicleMake_Clusters'] = kmeans.labels_

# Run KMeans on vehicle type & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'vehicle.type_cat']])
cluster_d['vehicleType_Clusters'] = kmeans.labels_

# Run KMeans on age & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'vehicle.age']])
cluster_d['vehicleAge_Clusters'] = kmeans.labels_

cluster_df = pd.DataFrame(data=cluster_d)

# Drop first column (indexes we no longer need)
# df.drop(df.columns[[0]], axis=1, inplace=True)
# cluster_df(cluster_df.columns[[0]], axis=1, inplace=True)

cluster_df.to_csv('./CarRentalDataClusters.csv')

print(categorical_values['vehicle_models']["civic"])
# print(json.dumps(dictt, sort_keys=True, indent=4))
# print(df)

# civic