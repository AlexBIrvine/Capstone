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
import matplotlib.pyplot as plt
from CSV_tools import data_prep
