import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 


def getLogisticRegression(X_list, X_values):
    df = pd.read_csv('./CarRentalDataCleaned.csv')
    X_train, X_test, y_train, y_test = train_test_split(df[X_list], df['recommended'])
    LogReg = LogisticRegression()
    LogReg.fit(X_train, y_train)
    
    # Run prediction, return result and score
    print(LogReg.predict(np.array([X_values]))[0])
    print(LogReg.score(X_test, y_test))