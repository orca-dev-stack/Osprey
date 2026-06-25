import pandas as pd
from processing.feature_engineering import basic_transaction_features
from processing.aml_indicators import aml_rules

def run_banking_pipeline(df: pd.DataFrame):
    df = df.copy()
    df = basic_transaction_features(df)
    df = aml_rules(df)
    df["source"] = "banking"
    return df
