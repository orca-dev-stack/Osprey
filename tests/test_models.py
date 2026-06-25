import pandas as pd
from models.train_tabular import train_tabular
from models.pytorch_model import train_pytorch
from models.tensorflow_model import train_tf
from models.autoencoder import train_autoencoder
from models.anomaly_detector import train_anomaly

def sample_df():
    return pd.DataFrame({
        "amount": [10, 20, 30, 40],
        "sender": [1, 2, 3, 4],
        "receiver": [5, 6, 7, 8],
        "channel": [0, 0, 0, 0],
        "country": [1, 1, 1, 1],
        "timestamp": [0, 0, 0, 0],
        "label": [0, 1, 0, 1],
        "source": ["test"] * 4
    })

def test_tabular_training_runs():
    df = sample_df()
    X = df.drop(columns=["label"])
    y = df["label"]
    train_tabular(X, y)

def test_pytorch_training_runs():
    df = sample_df()
    X = df.drop(columns=["label"])
    y = df["label"]
    train_pytorch(X, y)

def test_tensorflow_training_runs():
    df = sample_df()
    X = df.drop(columns=["label"])
    y = df["label"]
    train_tf(X, y)

def test_autoencoder_training_runs():
    df = sample_df()
    X = df.drop(columns=["label"])
    y = df["label"]
    train_autoencoder(X, y)

def test_anomaly_training_runs():
    df = sample_df()
    X = df.drop(columns=["label"])
    y = df["label"]
    train_anomaly(X, y)
