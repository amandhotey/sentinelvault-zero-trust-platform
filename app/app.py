import json
import time
import requests
from datetime import datetime, timezone

VAULT_ADDR = "http://localhost:8200"
VAULT_TOKEN = "sentinelvault-root"

APP_NAME = "sentinelvault-demo-app"
LOG_FILE = "logs/app_access.log"


def log_event(secret_path, action):
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app": APP_NAME,
        "secret_path": secret_path,
        "action": action
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(event) + "\n")


def get_secret(path, key):
    url = f"{VAULT_ADDR}/v1/{path}"
    headers = {"X-Vault-Token": VAULT_TOKEN}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Log BEFORE returning the secret
    log_event(path, "read")

    return response.json()["data"]["data"][key]


if __name__ == "__main__":
    db_password = get_secret("secret/data/app/db", "password")
    api_key = get_secret("secret/data/app/api", "api_key")


    print("Secrets fetched securely from Vault")
