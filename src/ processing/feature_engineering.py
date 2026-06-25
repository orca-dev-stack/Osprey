import pandas as pd
import numpy as np

def basic_transaction_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "TransactionDT" in df.columns:
        df["hour"] = (df["TransactionDT"] / 3600) % 24
        df["day"] = (df["TransactionDT"] / (3600 * 24)) % 7

    if "TransactionAmt" in df.columns:
        df["log_amount"] = np.log1p(df["TransactionAmt"])
        df["high_amount_flag"] = (df["TransactionAmt"] > df["TransactionAmt"].median()).astype(int)

    return df

def merge_sources(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(dfs, axis=0, ignore_index=True)
    df = df.drop_duplicates(subset=["transaction_id"], keep="last") if "transaction_id" in df.columns else df
    return df
