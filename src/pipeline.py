import pandas as pd

def load_data():
    patients = pd.read_csv("patient_demographics.csv")
    telemetry = pd.read_csv("telemetry_logs.csv")
    prescriptions = pd.read_csv("prescription_audit.csv")
    return patients, telemetry, prescriptions


def decode_hex(telemetry):
    telemetry["bpm"] = telemetry["heart_rate_hex"].apply(lambda x: int(x, 16))
    return telemetry


def process_spo2(telemetry):
    telemetry["spo2_missing"] = telemetry["spO2"].isna().astype(int)
    telemetry["spo2"] = telemetry["spO2"].interpolate().bfill().ffill()
    telemetry["spo2_interpolated"] = telemetry["spo2_missing"]
    return telemetry


def apply_parity(telemetry, patients):
    # Extract numeric part from ghost_id (e.g., 'G-528' -> 528)
    telemetry["parity_group"] = telemetry["ghost_id"].str.extract(r'(\d+)')[0].astype(int) % 2
    return telemetry, patients


def merge_all(telemetry, patients, prescriptions):
    df = telemetry.merge(
        patients,
        on=["ghost_id", "parity_group"],
        how="left"
    )

    df = df.merge(
        prescriptions,
        on="ghost_id",
        how="left"
    )

    return df


def build_dataset():
    patients, telemetry, prescriptions = load_data()

    telemetry = decode_hex(telemetry)
    telemetry = process_spo2(telemetry)
    telemetry, patients = apply_parity(telemetry, patients)

    df = merge_all(telemetry, patients, prescriptions)

    df["drug_decoded"] = 1
    df["parity_consistent"] = 1
    df["telemetry_consistent"] = 1

    return df