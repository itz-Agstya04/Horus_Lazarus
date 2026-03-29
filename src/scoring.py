def compute_final_score(df):
    df["final_score"] = (
        0.35 * df["risk_score"] +
        0.25 * df["anomaly_score"] +
        0.20 * (1 - df["integrity_score"]) +
        0.20 * (1 - df["confidence_score"])
    )
    return df


def classify(df):
    def label(x):
        if x < 0.5:
            return "Stable"
        elif x < 1.2:
            return "Warning"
        elif x < 2:
            return "Critical"
        else:
            return "Emergency"

    df["status"] = df["final_score"].apply(label)
    return df