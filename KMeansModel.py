import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from CSV_tools import data_prep

data_prep()

df = pd.read_csv('./CarRentalDataCleaned.csv')

# Run KMeans on fuel type & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'fuelType_cat']])
df['fuelType_Clusters'] = kmeans.labels_

# Run KMeans on trips taken & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'renterTripsTaken']])
df['tripsTaken_Clusters'] = kmeans.labels_

# Run KMeans on daily rate & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'rate.daily']])
df['dailyRate_Clusters'] = kmeans.labels_

# Run KMeans on vehicle make & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'vehicle.make_cat']])
df['vehicleMake_Clusters'] = kmeans.labels_

# Run KMeans on vehicle type & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'vehicle.type_cat']])
df['vehicleType_Clusters'] = kmeans.labels_

# Run KMeans on age & add results to dataframe
kmeans = KMeans(n_clusters=5)
kmeans = kmeans.fit(df[['rating', 'vehicle.age']])
df['vehicleAge_Clusters'] = kmeans.labels_

df.to_csv('./CarRentalDataCleaned.csv')

print(df)