import numpy as np

def compute_integrity_score(df):
    total = len(df)

    missing_spo2 = df["spo2_missing"].sum() / total
    interpolation = df["spo2_interpolated"].sum() / total

    parity_mismatch = df.get("parity_mismatch", 0)
    if isinstance(parity_mismatch, int):
        parity_mismatch = 0
    else:
        parity_mismatch = parity_mismatch.sum() / total

    integrity = 1.0
    integrity -= missing_spo2
    integrity -= 0.5 * interpolation
    integrity -= 0.3 * parity_mismatch

    df["integrity_score"] = np.clip(integrity, 0, 1)

    return df