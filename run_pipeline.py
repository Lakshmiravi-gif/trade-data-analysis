from pathlib import Path
import os
import pandas as pd

from src.cleaning.clean_base import clean_base
from src.parsing.parse_goods_description import parse_goods_description
from src.feature_engineering.features import add_features
from src.db.load_to_db import save_to_db

RAW_FILE_XLSX = Path("data/raw/trade_data_2017_2025.xlsx")
PROCESSED_DIR = Path("data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_CSV = PROCESSED_DIR / "trade_cleaned.csv"


def load_raw():
    """Load Excel file only."""
    if RAW_FILE_XLSX.exists():
        print("Loading Excel file:", RAW_FILE_XLSX)
        return pd.read_excel(RAW_FILE_XLSX)

    raise FileNotFoundError("Expected Excel file (.xlsx) in data/raw/")


def main():
    print("1) Loading raw data...")
    df = load_raw()

    print("2) Cleaning data...")
    df = clean_base(df)

    print("3) Parsing goods description...")
    df = parse_goods_description(df)

    print("4) Adding engineered features...")
    df = add_features(df)

    print("5) Preparing data types...")
    # Convert parsed_keywords list → string (SQLite requires this)
    if "parsed_keywords" in df.columns:
        df["parsed_keywords"] = df["parsed_keywords"].astype(str)

    print("6) Saving cleaned CSV...")

    # If old CSV exists → delete safely
    if OUTPUT_CSV.exists():
        try:
            OUTPUT_CSV.unlink()  # delete old file
        except PermissionError:
            print("\n❌ ERROR: Please close 'trade_cleaned.csv' in Excel and run again.")
            return

    df.to_csv(OUTPUT_CSV, index=False)
    print("   ✔ Saved:", OUTPUT_CSV)

    db_url = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{PROCESSED_DIR / 'trade_analysis.db'}"
    )

    print("7) Saving data to database:", db_url)
    save_to_db(df, db_url)

    print("\n🎉 Pipeline completed successfully!")


if __name__ == "__main__":
    main()