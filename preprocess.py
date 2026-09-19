# src/preprocess
import pandas as pd

def load_and_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.dropna()
    return df
