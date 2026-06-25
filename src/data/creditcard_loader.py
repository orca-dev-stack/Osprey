import pandas as pd

def load_creditcard(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.rename(columns={"Amount": "amount", "Class": "label"})
    df["transaction_id"] = df.index
    df["sender"] = None
    df["receiver"] = None
    df["channel"] = "banking"
    df["country"] = "EU"
    df["timestamp"] = None
    df["source"] = "creditcard"
    return df[[
        "transaction_id", "amount", "sender", "receiver",
        "channel", "country", "timestamp", "label", "source"
    ]]
