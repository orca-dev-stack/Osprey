import pandas as pd

def load_elliptic(classes_path: str, features_path: str) -> pd.DataFrame:
    classes = pd.read_csv(classes_path)
    features = pd.read_csv(features_path, header=None)

    # txId is transaction_id, class: 1=licit, 2=illicit, 3=unknown
    df = classes.merge(features, left_on="txId", right_on=0, how="left")
    df["transaction_id"] = df["txId"]
    df["amount"] = df[1]  # example: one of the feature columns as amount proxy
    df["sender"] = None
    df["receiver"] = None
    df["channel"] = "crypto"
    df["country"] = None
    df["timestamp"] = None
    df["label"] = df["class"].apply(lambda c: 1 if c == 2 else 0)
    df["source"] = "elliptic"

    return df[[
        "transaction_id", "amount", "sender", "receiver",
        "channel", "country", "timestamp", "label", "source"
    ]]
