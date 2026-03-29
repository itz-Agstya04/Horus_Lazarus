import pandas as pd
import numpy as np

def caesar(text, shift):
    res = ""
    for c in text:
        if c.isalpha():
            start = ord('A') if c.isupper() else ord('a')
            res += chr((ord(c) - start - shift) % 26 + start)
        else: res += c
    return res

# Load
p, t, r = pd.read_csv("patient_demographics.csv"), pd.read_csv("telemetry_logs.csv"), pd.read_csv("prescription_audit.csv")

# Process
t["bpm"] = t["heart_rate_hex"].apply(lambda x: int(str(x), 16) if pd.notnull(x) else 0)
t["spo2"] = t["spO2"].interpolate().ffill().bfill()
t["parity_group"] = t["bpm"] % 2

# Merge & Decode
df = t.merge(p, on=["ghost_id", "parity_group"], how="left")
rx = r.merge(p, on="ghost_id")
rx["med"] = rx.apply(lambda x: caesar(str(x["scrambled_med"]), int(x["age"]) % 26), axis=1)
meds = rx.groupby(['ghost_id', 'parity_group'])['med'].apply(lambda x: ", ".join(set(x))).to_dict()
df['medications'] = df.set_index(['ghost_id', 'parity_group']).index.map(meds)

# Score
df["risk_score"] = (np.abs(df["bpm"] - 80) / 20 + np.maximum(0, 94 - df["spo2"]) / 6)
df["status"] = df["risk_score"].apply(lambda x: "Emergency" if x > 2.0 else "Critical" if x > 1.2 else "Warning" if x > 0.5 else "Stable")

# Export
df.head(100).to_json("dashboard_data.json", orient="records")
print("Done! dashboard_data.json created.")