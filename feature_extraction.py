# src/feature_extraction.py
import pandas as pd
import numpy as np

def extract_features(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    # Example: compute rolling mean and std
    df["sensor_mean"] = df["sensor_value"].rolling(window=5).mean()
    df["sensor_std"] = df["sensor_value"].rolling(window=5).std()
    df = df.dropna()
    return df
