import pandas as pd
from features.build_features import build_features

def test_build_features_adds_columns():
    df = pd.DataFrame({
        "transaction_id": [1],
        "amount": [100],
        "sender": ["A"],
        "receiver": ["B"],
        "channel": ["banking"],
        "country": ["US"],
        "timestamp": ["2024-01-01"],
        "label": [0],
        "source": ["test"]
    })

    df2 = build_features(df)

    assert "log_amount" in df2.columns
    assert "high_amount_flag" in df2.columns
