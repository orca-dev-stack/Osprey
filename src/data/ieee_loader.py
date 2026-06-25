import pandas as pd

def load_ieee(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.rename(columns={"TransactionAmt": "amount", "isFraud": "label"})
    df["transaction_id"] = df["TransactionID"]
    df["sender"] = df.get("card1", None)
    df["receiver"] = df.get("merchant_id", None)
    df["channel"] = "banking"
    df["country"] = df.get("card_country", None)
    df["timestamp"] = df.get("TransactionDT", None)
    df["source"] = "ieee"
    return df[[
        "transaction_id", "amount", "sender", "receiver",
        "channel", "country", "timestamp", "label", "source"
    ]]
