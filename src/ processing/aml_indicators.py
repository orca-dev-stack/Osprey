import pandas as pd

def aml_rules(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "amount" in df.columns:
        df["aml_large_tx"] = (df["amount"] > 10_000).astype(int)
    if "country" in df.columns:
        high_risk = {"IR", "KP", "SY"}
        df["aml_high_risk_country"] = df["country"].isin(high_risk).astype(int)
    return df
