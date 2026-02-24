import pandas as pd
import joblib

DATASET = "ml-engine/data/access_dataset.csv"
MODEL_PATH = "ml-engine/models/anomaly_model.pkl"
OUTPUT_FILE = "ml-engine/data/anomaly_results.csv"

# Load dataset
df = pd.read_csv(DATASET)

# Load trained model
model = joblib.load(MODEL_PATH)

print("Model loaded successfully")

# Predict anomalies
predictions = model.predict(df)
scores = model.decision_function(df)

df["anomaly"] = predictions
df["risk_score"] = scores

# Save results
df.to_csv(OUTPUT_FILE, index=False)

print("\nDetection complete.")
print("Results saved to:", OUTPUT_FILE)

# Show anomalies
print("\n⚠️ Detected Anomalies:")
print(df[df["anomaly"] == -1])