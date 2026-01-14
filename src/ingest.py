import pandas as pd
import re
from pathlib import Path
from partner_config import PARTNER_CONFIG

OUTPUT_COLUMNS = [
    "external_id",
    "first_name",
    "last_name",
    "dob",
    "email",
    "phone",
    "partner_code"
]

def format_phone(phone):
    digits = re.sub(r"\D", "", str(phone))
    return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}" if len(digits) == 10 else None

def ingest_file(file_path, partner):
    cfg = PARTNER_CONFIG[partner]
    df = pd.read_csv(file_path, sep=cfg["delimiter"], dtype=str)

    df = df.rename(columns=cfg["column_mapping"])

    df["first_name"] = df["first_name"].str.title()
    df["last_name"] = df["last_name"].str.title()
    df["email"] = df["email"].str.lower()
    df["dob"] = pd.to_datetime(df["dob"], errors="coerce").dt.strftime("%Y-%m-%d")
    df["phone"] = df["phone"].apply(format_phone)
    df["partner_code"] = cfg["partner_code"]

    return df[OUTPUT_COLUMNS]

def main():
    root = Path(__file__).resolve().parents[1]

    acme_df = ingest_file(root / "data" / "acme.txt", "acme")
    bettercare_df = ingest_file(root / "data" / "bettercare.csv", "bettercare")

    final_df = pd.concat([acme_df, bettercare_df], ignore_index=True)

    output_path = root / "output" / "unified_output.csv"
    output_path.parent.mkdir(exist_ok=True)

    final_df.to_csv(output_path, index=False)
    print("Unified file is saved to:", output_path)

if __name__ == "__main__":
    main()
