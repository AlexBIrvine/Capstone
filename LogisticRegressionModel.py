# Steps: 
# ------
# Just decide what data to use, drop more columns probably



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 

df = pd.read_csv('./CarRentalDataCleaned.csv')
df.drop(df.columns[[0]], axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(df.drop(['rating', 'renterTripsTaken', 'recommended'], axis=1), df['recommended'])

LogReg = LogisticRegression()
LogReg.fit(X_train, y_train)

print(LogReg.predict(np.array([[20, 2, 3, 2,3, 2]]))[0])
print(LogReg.score(X_test, y_test))