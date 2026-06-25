import pandas as pd
import networkx as nx

def add_blockchain_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "sender" not in df.columns or "receiver" not in df.columns:
        df["wallet_degree"] = 0
        df["wallet_in_degree"] = 0
        df["wallet_out_degree"] = 0
        return df

    G = nx.DiGraph()
    edges = df[["sender", "receiver"]].dropna().values.tolist()
    G.add_edges_from(edges)

    df["wallet_degree"] = df["sender"].apply(lambda w: G.degree(w) if w in G else 0)
    df["wallet_in_degree"] = df["receiver"].apply(lambda w: G.in_degree(w) if w in G else 0)
    df["wallet_out_degree"] = df["sender"].apply(lambda w: G.out_degree(w) if w in G else 0)

    return df
