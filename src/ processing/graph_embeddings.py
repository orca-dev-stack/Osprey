import pandas as pd
import networkx as nx

def build_transaction_graph(df: pd.DataFrame) -> nx.Graph:
    G = nx.Graph()
    for _, row in df.iterrows():
        src = row.get("sender_wallet") or row.get("card_id")
        dst = row.get("receiver_wallet") or row.get("merchant_id")
        if src and dst:
            G.add_edge(src, dst, amount=row.get("amount", 0.0))
    return G

def simple_degree_embeddings(G: nx.Graph) -> pd.DataFrame:
    nodes = list(G.nodes())
    degrees = dict(G.degree())
    df = pd.DataFrame({
        "node": nodes,
        "degree": [degrees[n] for n in nodes],
    })
    return df
