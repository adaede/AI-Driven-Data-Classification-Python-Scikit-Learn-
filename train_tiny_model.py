# src/train_tiny_model.py
from feature_extraction import extract_features
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

DATA_PATH = "data/sensor_data.csv"
MODEL_PATH = "models/tiny_model.pkl"

def main():
    df = extract_features(DATA_PATH)

    # Adjust 'label' to your actual target column
    X = df[["sensor_mean", "sensor_std"]]
    y = df["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Tiny model accuracy: {acc:.4f}")

    joblib.dump(model, MODEL_PATH)
    print(f"Tiny model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
