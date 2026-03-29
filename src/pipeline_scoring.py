from src.risk import compute_risk_score
from src.anomaly import compute_anomaly_score
from src.integrity import compute_integrity_score
from src.confidence import compute_confidence_score
from src.scoring import compute_final_score, classify

def run_scoring(df):
    df = compute_risk_score(df)
    df = compute_anomaly_score(df)
    df = compute_integrity_score(df)
    df = compute_confidence_score(df)
    df = compute_final_score(df)
    df = classify(df)
    return df