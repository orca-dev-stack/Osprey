import pandas as pd
from data.unified_loader import load_all

def test_load_all_returns_dataframe():
    df = load_all()
    assert isinstance(df, pd.DataFrame)

def test_unified_schema():
    df = load_all()
    expected_cols = {
        "transaction_id", "amount", "sender", "receiver",
        "channel", "country", "timestamp", "label", "source"
    }
    assert expected_cols.issubset(df.columns)
