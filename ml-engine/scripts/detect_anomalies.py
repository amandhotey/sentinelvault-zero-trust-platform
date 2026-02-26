# ============================================
# SentinelVault ML Anomaly Detection Engine
# ============================================

import os
import pandas as pd
import requests
from sklearn.ensemble import IsolationForest

# ============================================
# PATH SETUP (WORKS FROM ANY DIRECTORY)
# ============================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATASET = os.path.join(BASE_DIR, "data", "access_dataset.csv")
OUTPUT = os.path.join(BASE_DIR, "data", "anomaly_results.csv")

# API endpoint (app.py)
ANOMALY_API = "http://localhost:5000/anomaly"

# ============================================
# LOAD DATASET
# ============================================

print("📂 Loading dataset...")

df = pd.read_csv(DATASET)

# ============================================
# FEATURE SELECTION
# ============================================

features = df[["hour", "minute", "secret", "action"]]

# ============================================
# TRAIN MODEL
# ============================================

print("🤖 Training Isolation Forest model...")

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(features)

print("✅ Model loaded successfully")

# ============================================
# DETECT ANOMALIES
# ============================================

df["anomaly"] = model.predict(features)
df["risk_score"] = model.decision_function(features)

# anomaly = -1 means suspicious
anomalies = df[df["anomaly"] == -1]

# ============================================
# SAVE RESULTS
# ============================================

df.to_csv(OUTPUT, index=False)

print("\nDetection complete.")
print(f"Results saved to: {OUTPUT}")

# ============================================
# SEND ALERTS TO MONITORING APP
# ============================================

if not anomalies.empty:
    print("\n⚠️ Detected Anomalies:")

    print(anomalies[["hour", "minute", "secret",
                     "action", "anomaly", "risk_score"]])

    print("\n🚨 Sending anomalies to SentinelVault monitoring...")

    for _, row in anomalies.iterrows():
        try:
            requests.post(ANOMALY_API, timeout=2)
            print("✅ Alert sent")
        except Exception as e:
            print("❌ Failed to notify app:", e)

else:
    print("\n✅ No anomalies detected.")