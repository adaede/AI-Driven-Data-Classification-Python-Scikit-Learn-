# preprocess.py
import csv

def load_and_clean(path):
    with open(path, newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    return [row for row in rows if all(value not in (None, "") for value in row.values())]

# train_model.py
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = load_and_clean("data/dataset.csv")
X = [[float(value) for key, value in row.items() if key != "target"] for row in df]
y = [row["target"] for row in df]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "models/model.pkl")