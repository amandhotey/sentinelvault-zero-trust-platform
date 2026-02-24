import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

DATASET = "ml-engine/data/access_dataset.csv"
MODEL_PATH = "ml-engine/models/anomaly_model.pkl"

# Load dataset
df = pd.read_csv(DATASET)

print("Dataset loaded:")
print(df.head())

# Train Isolation Forest
model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(df)

# Save trained model
joblib.dump(model, MODEL_PATH)

print("\nModel trained and saved at:", MODEL_PATH)