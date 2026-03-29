import numpy as np

def compute_risk_score(df):
    bpm = df["bpm"]
    spo2 = df["spo2"]

    df["risk_score"] = (
        np.abs(bpm - 80) / 20 +
        np.maximum(0, 94 - spo2) / 6
    )

    df["risk_flag"] = (
        ((bpm < 60) | (bpm > 100)) |
        (spo2 < 94)
    ).astype(int)

    return df