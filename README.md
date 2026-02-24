# 🔐 SentinelVault — AI-Driven DevSecOps Security Platform

SentinelVault is an end-to-end DevSecOps security system that secures,
monitors, detects, and automatically responds to abnormal secret access
using Machine Learning.

---

## 🚨 Problem

Organizations store API keys and credentials securely but lack:

- Visibility into secret usage
- Behavioral monitoring
- Intelligent threat detection
- Automated remediation

---

## ✅ Solution

SentinelVault implements a **complete security lifecycle**:

Secure → Monitor → Detect → Respond

---

## 🏗️ Architecture


Application
↓
HashiCorp Vault (Secrets Control Plane)
↓
Audit + Access Logs
↓
ML Anomaly Detection (Isolation Forest)
↓
Auto-Remediation Engine


---

## ⚙️ Features

- 🔐 Centralized Secret Management (Vault)
- 🔎 Secret Discovery using Gitleaks
- 📊 Audit & Telemetry Logging
- 🧠 ML-Based Anomaly Detection
- 🛡️ Automated Security Response
- 🚀 DevSecOps CI/CD Integration

---

## 🧰 Tech Stack

| Category | Tools |
|---|---|
| DevOps | Docker, GitHub Actions |
| Security | HashiCorp Vault, Gitleaks |
| Backend | Python |
| ML | Scikit-learn (Isolation Forest) |
| Monitoring | Structured Logging |

---

## ▶️ Demo Workflow

```bash
# Start Vault
docker compose up -d

# Fetch secrets securely
python app/app.py

# Prepare ML dataset
python ml-engine/scripts/prepare_dataset.py

# Train model
python ml-engine/scripts/train_model.py

# Detect anomalies
python ml-engine/scripts/detect_anomalies.py

# Auto remediation
python ml-engine/scripts/auto_remediate.py
🧠 Key Learning Outcomes

DevSecOps architecture design

Secure secret lifecycle management

Behavioral security analytics

ML-based anomaly detection

Automated incident response

👨‍💻 Author

Aman Dhotey
Cloud | DevSecOps | Security Engineering

LinkedIn: https://www.linkedin.com/in/aman-dhotey-2723a520


---