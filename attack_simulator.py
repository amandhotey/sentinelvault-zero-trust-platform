import requests
import time
import random

VAULT_ADDR = "http://localhost:8200"
VAULT_TOKEN = "sentinelvault-root"

headers = {
    "X-Vault-Token": VAULT_TOKEN
}

print("🔥 ATTACK SIMULATION STARTED")

while True:
    try:
        # attacker repeatedly steals secrets
        requests.get(
            f"{VAULT_ADDR}/v1/secret/data/app/db",
            headers=headers,
            timeout=2
        )

        print("⚠️ Secret accessed")

        # very fast requests (abnormal behaviour)
        time.sleep(random.uniform(0.05, 0.2))

    except Exception as e:
        print("Error:", e)