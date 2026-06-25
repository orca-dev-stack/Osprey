import os
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.model_selection import train_test_split

MODEL_DIR = "models_artifacts"
os.makedirs(MODEL_DIR, exist_ok=True)


class FraudAutoencoder(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
        )
        self.decoder = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, input_dim),
        )

    def forward(self, x):
        z = self.encoder(x)
        x_rec = self.decoder(z)
        return x_rec


def train_autoencoder(X, y, epochs: int = 10, batch_size: int = 512):
    # Train on non-fraud only
    X_normal = X[y == 0]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    X_train, X_val = train_test_split(X_normal, test_size=0.2, random_state=42)

    X_train_t = torch.tensor(X_train.values, dtype=torch.float32)
    X_val_t = torch.tensor(X_val.values, dtype=torch.float32)

    train_ds = TensorDataset(X_train_t)
    train_dl = DataLoader(train_ds, batch_size=batch_size, shuffle=True)

    model = FraudAutoencoder(input_dim=X.shape[1]).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.MSELoss()

    for epoch in range(epochs):
        model.train()
        for (xb,) in train_dl:
            xb = xb.to(device)
            optimizer.zero_grad()
            x_rec = model(xb)
            loss = criterion(x_rec, xb)
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_rec = model(X_val_t.to(device)).cpu()
        val_loss = criterion(val_rec, X_val_t).item()
        print(f"[Autoencoder] Epoch {epoch+1}/{epochs} Val MSE: {val_loss:.6f}")

    torch.save(model.state_dict(), os.path.join(MODEL_DIR, "autoencoder.pt"))
    print("[Autoencoder] Saved model.")
