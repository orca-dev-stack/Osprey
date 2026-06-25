import pandas as pd

def load_paysim(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.rename(columns={"amount": "amount", "isFraud": "label"})
    df["transaction_id"] = df.index
    df["sender"] = df["nameOrig"]
    df["receiver"] = df["nameDest"]
    df["channel"] = "mobile_money"
    df["country"] = "KE"
    df["timestamp"] = None
    df["source"] = "paysim"
    return df[[
        "transaction_id", "amount", "sender", "receiver",
        "channel", "country", "timestamp", "label", "source"
    ]]
