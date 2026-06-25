import os
import pandas as pd
from data.creditcard_loader import load_creditcard
from data.ieee_loader import load_ieee
from data.paysim_loader import load_paysim
from data.elliptic_loader import load_elliptic

DATA_DIR = "data"  # adjust to your structure

def load_all() -> pd.DataFrame:
    dfs = []

    dfs.append(load_creditcard(os.path.join(DATA_DIR, "creditcard.csv")))
    dfs.append(load_ieee(os.path.join(DATA_DIR, "ieee.csv")))
    dfs.append(load_paysim(os.path.join(DATA_DIR, "paysim.csv")))
    dfs.append(
        load_elliptic(
            os.path.join(DATA_DIR, "elliptic_txs_classes.csv"),
            os.path.join(DATA_DIR, "elliptic_txs_features.csv"),
        )
    )

    df = pd.concat(dfs, ignore_index=True)
    return df
