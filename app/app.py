from prometheus_client import start_http_server, Counter
from flask import Flask, jsonify
import json
import requests
from datetime import datetime, timezone

# ==============================
# PROMETHEUS METRICS
# ==============================

secret_requests = Counter(
    "secret_requests_total",
    "Total secret fetch requests"
)

anomaly_events = Counter(
    "anomaly_events_total",
    "Detected anomaly events"
)

# ==============================
# FLASK APP (API SERVER)
# ==============================

app = Flask(__name__)

# ==============================
# CONFIG
# ==============================

VAULT_ADDR = "http://localhost:8200"
VAULT_TOKEN = "sentinelvault-root"

APP_NAME = "sentinelvault-demo-app"
LOG_FILE = "logs/app_access.log"


# ==============================
# LOGGING FUNCTION
# ==============================

def log_event(secret_path, action):
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app": APP_NAME,
        "secret_path": secret_path,
        "action": action
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")


# ==============================
# VAULT SECRET FETCH
# ==============================

def get_secret(path, key):
    url = f"{VAULT_ADDR}/v1/{path}"
    headers = {"X-Vault-Token": VAULT_TOKEN}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # increment metric
    secret_requests.inc()

    # log access
    log_event(path, "read")

    return response.json()["data"]["data"][key]


# ==============================
# ANOMALY API (ML ENGINE CALLS THIS)
# ==============================

@app.route("/anomaly", methods=["POST"])
def register_anomaly():
    anomaly_events.inc()
    print("🚨 Anomaly event received!")
    return jsonify({"status": "anomaly recorded"})


# ==============================
# HEALTH CHECK (OPTIONAL)
# ==============================

@app.route("/")
def health():
    return jsonify({"status": "SentinelVault running"})


# ==============================
# MAIN STARTUP
# ==============================

if __name__ == "__main__":

    # Start Prometheus metrics server
    start_http_server(8000)
    print("📊 Metrics available at http://localhost:8000/metrics")

    # Fetch secrets once (demo activity)
    try:
        db_password = get_secret("secret/data/app/db", "password")
        api_key = get_secret("secret/data/app/api", "api_key")
        print("✅ Secrets fetched securely from Vault")
    except Exception as e:
        print("Vault connection issue:", e)

    # Start Flask API server
    print("🚀 SentinelVault API running on http://localhost:5000")
    app.run(host="0.0.0.0", port=5000)