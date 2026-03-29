# 🩺 Project Lazarus: Forensic Clinical Surveillance

Project Lazarus is a high-fidelity data science pipeline and interactive dashboard designed to monitor 1,000 patients across a distributed hospital network. This project specializes in **Forensic Data Recovery**, using mathematical patterns to reconnect scrambled telemetry and encrypted medical records.

## 🔍 Forensic Decoding Logic
The raw data was provided in a "scrambled" state to simulate a compromised or legacy medical system. This project implements three core recovery techniques:

1.  **Hex-to-Decimal Telemetry**: Decodes `heart_rate_hex` from hexadecimal to standard BPM (0x51 → 81 BPM).
2.  **Vital-Parity Disambiguation**: Two distinct patients share the same `ghost_id`. The system correctly maps telemetry to the right patient by matching the **BPM Parity** (Even/Odd) to the assigned `parity_group`.
3.  **Age-Relative Caesar Cipher**: Medication names were encrypted using a Caesar Cipher. The system dynamically decrypts them using a shift based on the patient's age (`Age % 26`).

## 📊 Scoring Architecture
The triage system uses a **Weighted Composite Score** ($0.35/0.25/0.20/0.20$) to categorize patients into four levels: **Stable, Warning, Critical, and Emergency.**

| Component | Weight | Logic |
| :--- | :--- | :--- |
| **Risk Score** | 35% | Evaluates BPM (target 80) and SpO2 (target 94-100%). |
| **Anomaly Score** | 25% | Identifies outliers using a **1.5σ (Sigma)** Z-Score threshold. |
| **Integrity Score** | 20% | Tracks data quality, penalizing missing or interpolated SpO2 values. |
| **Confidence Score** | 20% | Measures system trust based on successful medication decryption. |

## 🛠️ Installation & Execution

### Prerequisites
* Python 3.8+
* Pandas, NumPy

### Quick Start
1.  Place `run_lazarus.py`, `index.html`, and the three CSV data files in the same directory.
2.  Run the master script:
    ```bash
    python run.py
    ```
3.  The script will automatically:
    * Process and score all 1,000 patients.
    * Generate `dashboard_data.json`.
    * Launch a local web server at `http://localhost:8000`.
    * Open your default browser to the interactive dashboard.

## 🖥️ Dashboard Features
* **Live Triage Table**: Real-time sorting by the composite Final Score.
* **Risk Distribution**: Doughnut chart showing the global health status of the ward.
* **Patient Focus**: Interactive sidebar that breaks down the individual score components for any selected patient.
* **Integrity Tracking**: Visual indicators of telemetry data quality and confidence levels.
