""" Load a CSV file into a pandas DataFrame. """
import pandas as pd
def load_csv("file_path"):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None
    

"""Clean the data by removing or filling missing values."""
def clean_data(df):
    if df is not None:
        df = df.dropna()  # Example: drop rows with missing values
        # Add more cleaning steps as needed
        return df
    return None


""" Scale features in the DataFrame using StandardScaler. """
from sklearn.preprocessing import StandardScaler

def scale_features(df):
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled


""" Plot a histogram of a specified column in the DataFrame. """
import matplotlib.pyplot as plt
def plot_histogram(df, column):
    if column in df.columns:
        plt.hist(df[column], bins=30)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.title(f'Histogram of {column}')
        plt.show()

""" Load configuration settings from a JSON file. """
import json
def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            return config
    except Exception as e:
        print(f"Error loading configuration file: {e}")
        return None


""" Get the mean value of a specified column in the DataFrame. """
def get_column_mean(df, column):
    if column in df.columns:
        return df[column].mean()
    return None

