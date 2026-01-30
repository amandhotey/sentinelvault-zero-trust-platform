import os
import requests

VAULT_ADDR = "http://localhost:8200"
VAULT_TOKEN = "sentinelvault-root"

def get_secret(path, key):
    url = f"{VAULT_ADDR}/v1/{path}"
    headers = {"X-Vault-Token": VAULT_TOKEN}
    response = requests.get(url, headers=headers)
    return response.json()["data"]["data"][key]

db_password = get_secret("secret/app/db", "password")
api_key = get_secret("secret/app/api", "api_key")

print("Secrets fetched securely from Vault")
