import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split 


def getLogisticRegression(X_list, X_values):
    """
    Function to train a logistic regression model.  
    Used to predict if passed in values would result in 5-star rating.  

    Returns formatted string with yes/no result & model accuracy.  
    """
    df = pd.read_csv('./CarRentalDataCleaned.csv')
    X_train, X_test, y_train, y_test = train_test_split(df[X_list], df['recommended'])
    LogReg = LogisticRegression()
    LogReg.fit(X_train, y_train)
    
    # Run prediction and gets accuracy score
    result = LogReg.predict(np.array([X_values]))[0]
    accuracy = LogReg.score(X_test, y_test)
    
    # Returns the result as formatted string
    if result == 1:
        return f"Vehicle is predicted to be recommended!  The model is {(accuracy*100):.2f}% confident in it's accuracy."
    else: 
        return f"Vehicle is predicted to be not recommended.  The model is {(accuracy*100):.2f}% confident in it's accuracy."



def getKMeansGraph(x_axis, y_axis, cluster_count):
    """
    Function to determin clusters using K-means
    
    Saves created graph as an image to be used by `KMeansTab.py`
    """

    # Read in data
    df = pd.read_csv('./CarRentalDataCleaned.csv')

    # Run K-Mean Clustering Model
    kmeans = KMeans(n_clusters=cluster_count)
    kmeans = kmeans.fit(df[[x_axis, y_axis]])
    clusters = []
    clusters = kmeans.labels_

    # create graph
    plot = sns.scatterplot(x=x_axis, y=y_axis, hue=clusters, data=df)
    plt.savefig('output.png')
    print(len(kmeans.labels_))
    
    # Delete dataframe from memory.
    del df
    del clusters
    del kmeans
    del plot

