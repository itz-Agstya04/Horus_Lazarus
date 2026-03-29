import numpy as np

def compute_confidence_score(df):
    confidence = (
        0.4 * df["drug_decoded"] +
        0.3 * df["parity_consistent"] +
        0.3 * df["telemetry_consistent"]
    )

    df["confidence_score"] = np.clip(confidence, 0, 1)

    return df