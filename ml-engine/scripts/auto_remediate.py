import pandas as pd
from datetime import datetime
import json

INPUT_FILE = "ml-engine/data/anomaly_results.csv"
ALERT_LOG = "ml-engine/data/security_alerts.log"


def calculate_risk(score):
    if score < -0.20:
        return "HIGH"
    elif score < -0.10:
        return "MEDIUM"
    else:
        return "LOW"


def simulate_secret_rotation(secret_id):
    print(f"🔐 Rotating secret automatically: {secret_id}")


df = pd.read_csv(INPUT_FILE)

alerts = []

for _, row in df.iterrows():
    if row["anomaly"] == -1:

        risk = calculate_risk(row["risk_score"])

        alert = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "secret_id": int(row["secret"]),
            "risk_level": risk,
            "risk_score": float(row["risk_score"]),
            "action": "rotation_triggered" if risk == "HIGH" else "monitor"
        }

        if risk == "HIGH":
            simulate_secret_rotation(row["secret"])

        alerts.append(alert)

# Save alerts
with open(ALERT_LOG, "a") as f:
    for alert in alerts:
        f.write(json.dumps(alert) + "\n")

print("\n✅ Auto-remediation completed.")
print(f"Alerts generated: {len(alerts)}")