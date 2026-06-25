import os
import torch
from torch import nn
from torch_geometric.data import Data
from torch_geometric.nn import GCNConv

MODEL_DIR = "models_artifacts"
os.makedirs(MODEL_DIR, exist_ok=True)


class WalletGNN(nn.Module):
    def __init__(self, in_channels, hidden_channels=64, out_channels=2):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        self.lin = nn.Linear(hidden_channels, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index)
        x = torch.relu(x)
        x = self.conv2(x, edge_index)
        x = torch.relu(x)
        x = self.lin(x)
        return x


def build_crypto_graph(df_crypto):
    # Example: treat sender/receiver as nodes, edges as transactions
    wallets = pd.unique(df_crypto[["sender", "receiver"]].values.ravel("K"))
    wallets = [w for w in wallets if w is not None]
    wallet_to_idx = {w: i for i, w in enumerate(wallets)}

    edges = []
    for _, row in df_crypto.iterrows():
        s, r = row["sender"], row["receiver"]
        if s in wallet_to_idx and r in wallet_to_idx:
            edges.append([wallet_to_idx[s], wallet_to_idx[r]])

    if not edges:
        raise ValueError("No edges for crypto graph.")

    edge_index = torch.tensor(edges, dtype=torch.long).t().contiguous()

    # Simple features: degree or amount; here just ones
    x = torch.ones((len(wallets), 8), dtype=torch.float32)  # dummy 8-dim features

    # Labels: wallet-level label from transaction labels (simplified)
    y = torch.zeros(len(wallets), dtype=torch.long)
    #  can aggregate tx labels per wallet here

    return Data(x=x, edge_index=edge_index, y=y)


def train_gnn(df_crypto, epochs: int = 20):
    import pandas as pd  # ensure imported

    data = build_crypto_graph(df_crypto)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = WalletGNN(in_channels=data.num_node_features).to(device)
    data = data.to(device)

    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        model.train()
        optimizer.zero_grad()
        out = model(data.x, data.edge_index)
        loss = criterion(out, data.y)
        loss.backward()
        optimizer.step()
        print(f"[GNN] Epoch {epoch+1}/{epochs} Loss: {loss.item():.4f}")

    torch.save(model.state_dict(), os.path.join(MODEL_DIR, "gnn_wallets.pt"))
    print("[GNN] Saved model.")
