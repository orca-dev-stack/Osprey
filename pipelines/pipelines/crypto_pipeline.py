import pandas as pd
from processing.graph_embeddings import build_transaction_graph, simple_degree_embeddings

def run_crypto_pipeline(df: pd.DataFrame):
    df = df.copy()

    # Build graph
    G = build_transaction_graph(df)
    emb = simple_degree_embeddings(G)

    # Merge embeddings back
    df = df.merge(emb, left_on="sender_wallet", right_on="node", how="left")
    df["source"] = "crypto"
    return df
