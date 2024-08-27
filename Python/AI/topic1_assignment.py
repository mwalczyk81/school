"""
AI Introduction Assignment - Practical Tasks

This assignment is designed to give you hands-on experience with some of the Python libraries commonly used in AI.
You will implement functions that demonstrate basic usage of these libraries.

Please make sure to install the necessary libraries before you start implementing the functions:
- numpy
- pandas
- scikit-learn

You can install them using pip:
pip install numpy pandas scikit-learn
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

def perform_linear_regression(X, y):
    """
    Perform a simple linear regression.

    Parameters:
    X (numpy.ndarray): 2D array where each row represents a sample and each column represents a feature.
    y (numpy.ndarray): 1D array of targets associated with each sample in X.

    Returns:
    coefficients (numpy.ndarray): Coefficients of the linear regression model.
    intercept (float): Intercept of the linear regression model.
    """
    model = LinearRegression()
    
    model.fit(X, y)
    
    return model.coef_, model.intercept_

def calculate_statistics(data):
    """
    Calculate mean, median, and standard deviation of a dataset.

    Parameters:
    data (numpy.ndarray): 1D array containing numerical data.

    Returns:
    statistics (dict): A dictionary containing the mean, median, and standard deviation of the data,
                        with keys 'mean', 'median', and 'std'.
    """
        
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data)
    }

def preprocess_dataframe(df):
    """
    Preprocess a pandas dataframe: impute missing values, encode categorical variables (if any), and normalize numerical features.

    Parameters:
    df (pandas.DataFrame): DataFrame to preprocess.

    Returns:
    processed_df (pandas.DataFrame): The preprocessed DataFrame.
    """

    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])    
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_columns),
            ('cat', categorical_transformer, categorical_columns)
        ])
    
    preprocessor.fit(df)
    
    processed_array = preprocessor.transform(df)
    
    # This will throw the AttributeError below if there are no categorical columns, so catch the exception and make it an empty list
    # Error occurred: This OneHotEncoder instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.
    try:
        encoded_categorical_columns = preprocessor.named_transformers_['cat']['encoder'].get_feature_names_out(categorical_columns)
    except AttributeError:
        encoded_categorical_columns = []

    all_columns = list(numerical_columns) + list(encoded_categorical_columns)
    
    processed_df = pd.DataFrame(processed_array, columns=all_columns)
    
    return processed_df