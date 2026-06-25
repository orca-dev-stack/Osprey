import pandas as pd
from processing.feature_engineering import basic_transaction_features

def run_mobile_money_pipeline(df: pd.DataFrame):
    df = df.copy()
    df = basic_transaction_features(df)
    df["mobile_fee"] = df["amount"] * 0.015
    df["source"] = "mobile_money"
    return df
