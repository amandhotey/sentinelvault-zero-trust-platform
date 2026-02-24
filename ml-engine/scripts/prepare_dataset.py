import json
import pandas as pd
from datetime import datetime

LOG_FILE = "logs/app_access.log"
OUTPUT_FILE = "ml-engine/data/access_dataset.csv"

records = []

with open(LOG_FILE, "r") as f:
    for line in f:
        event = json.loads(line)

        ts = datetime.fromisoformat(event["timestamp"].replace("Z", ""))

        records.append({
            "hour": ts.hour,
            "minute": ts.minute,
            "secret": event["secret_path"],
            "action": event["action"]
        })

df = pd.DataFrame(records)

# Convert categorical columns
df["secret"] = df["secret"].astype("category").cat.codes
df["action"] = df["action"].astype("category").cat.codes

df.to_csv(OUTPUT_FILE, index=False)

print("Dataset created:", OUTPUT_FILE)