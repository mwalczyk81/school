"""
Python Essentials for AI Assignment

This assignment covers key Python essentials for AI, including a refresher on Python for AI applications,
data handling and preprocessing, and implementing basic AI algorithms.

Before starting, ensure you have the following libraries installed:
- numpy
- pandas

You can install them using pip:
pip install numpy pandas
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from scipy.stats import zscore

def filter_outliers(data):
    """
    Filter outliers from a dataset. An outlier is defined as a value that is more than 2 standard deviations from the mean.

    Parameters:
    data (numpy.ndarray): 1D array containing numerical data.

    Returns:
    filtered_data (numpy.ndarray): The dataset with outliers removed.
    """
    
    # Your code here
    # Need to account for zero variance otherwise a test fails
    if np.std(data) == 0:
        return data
    
    # Filter out values that are more than 2 standard deviations from the mean
    return data[abs(data - np.mean(data)) < 2 * np.std(data)]


def normalize_features(X):
    """
    Normalize the features in a dataset to have zero mean and unit variance.

    Parameters:
    X (numpy.ndarray): 2D array where each row represents a sample and each column represents a feature.

    Returns:
    normalized_X (numpy.ndarray): The dataset with normalized features.
    """
        
    # Your code here
    return (X - X.mean(axis=0)) / X.std(axis=0)


def implement_knn(X_train, y_train, X_test, k):
    """
    Implement the k-Nearest Neighbors (kNN) algorithm from scratch. Use Euclidean distance to find the k nearest neighbors.

    Parameters:
    X_train (numpy.ndarray): 2D array of training data samples.
    y_train (numpy.ndarray): 1D array of labels corresponding to the training samples.
    X_test (numpy.ndarray): 2D array of test data samples.
    k (int): The number of nearest neighbors to consider for making predictions.

    Returns:
    predictions (numpy.ndarray): Predicted labels for the test data.
    """
    # Your code here
    predictions = []

    for test_sample in X_test:
        # Calculate distances...Euclidean is the square root of the summed distance squared
        distances = np.array([np.sqrt(np.sum((test_sample - train_sample) ** 2)) for train_sample in X_train])
        
        # Use argsort to get the indices of the sorted distances
        k_indices = np.argsort(distances)[:k]
        
        k_nearest_labels = y_train[k_indices]
        
        label_counts = {}
        
        # Not sure if adding other libraries is allowed for assignments so I did this manually instead of using Counter
        # Loop through the labels to get how often each occurs
        for label in k_nearest_labels:
            if label in label_counts:
                label_counts[label] += 1
            else:
                label_counts[label] = 1        
        
        most_common_label = max(label_counts, key=label_counts.get)
        
        predictions.append(most_common_label)
    
    return np.array(predictions)