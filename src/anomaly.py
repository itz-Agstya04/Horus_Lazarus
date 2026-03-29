import numpy as np

def z_score(series):
    return (series - series.mean()) / series.std()

def compute_anomaly_score(df):
    df["z_bpm"] = z_score(df["bpm"])
    df["z_spo2"] = z_score(df["spo2"])

    df["anomaly_score"] = (
        np.abs(df["z_bpm"]) +
        np.abs(df["z_spo2"])
    )

    df["anomaly_flag"] = (
        (np.abs(df["z_bpm"]) > 1.5) |
        (np.abs(df["z_spo2"]) > 1.5)
    ).astype(int)

    return df