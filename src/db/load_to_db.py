import pandas as pd
from sqlalchemy import create_engine

def save_to_db(df: pd.DataFrame, db_url: str):
    engine = create_engine(db_url)
    df.to_sql("trade_data", engine, if_exists="replace", index=False)
    print("Saved to DB successfully.")