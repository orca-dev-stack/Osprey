import os
import numpy as np
import pandas as pd
from config.settings import DATA_DIR

def generate_synthetic_transactions(n: int = 100_000):
    os.makedirs(DATA_DIR, exist_ok=True)
    amounts = np.random.lognormal(mean=3, sigma=1, size=n)
    is_fraud = np.random.binomial(1, 0.02, size=n)
    df = pd.DataFrame({
        "transaction_id": np.arange(n),
        "amount": amounts,
        "is_fraud": is_fraud,
    })
    path = os.path.join(DATA_DIR, "synthetic_transactions.csv")
    df.to_csv(path, index=False)
    print(f"[Synthetic] Generated {n} rows at {path}")
    return df

if __name__ == "__main__":
    generate_synthetic_transactions()
