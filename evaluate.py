# src/evaluate.py
import joblib
import pandas as pd
from sklearn.metrics import classification_report
from preprocess import load_and_clean

DATA_PATH = "data/dataset.csv"
MODEL_PATH = "models/model.pkl"

def main():
    df = load_and_clean(DATA_PATH)
    X = df.drop("target", axis=1)
    y = df["target"]

    model = joblib.load(MODEL_PATH)
    y_pred = model.predict(X)

    print("Classification Report:")
    print(classification_report(y, y_pred))

if __name__ == "__main__":
    main()
