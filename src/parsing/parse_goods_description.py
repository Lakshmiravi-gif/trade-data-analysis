import pandas as pd
import regex as re

def parse_goods_description(df: pd.DataFrame) -> pd.DataFrame:
    if "Goods Description" not in df.columns:
        print("Warning: 'Goods Description' column not found.")
        df["Goods Description"] = ""

    df["parsed_keywords"] = (
        df["Goods Description"]
        .astype(str)
        .str.lower()
        .apply(lambda x: re.findall(r"[a-zA-Z]+", x))
    )

    return df