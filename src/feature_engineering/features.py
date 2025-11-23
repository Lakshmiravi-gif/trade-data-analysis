import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "value" in df.columns:
        df["value_log"] = df["value"].apply(
            lambda x: None if x <= 0 else __import__("math").log(x)
        )
    else:
        df["value_log"] = None

    return df