import pandas as pd
import numpy as np

from features.categorical_encoders import encode_categoricals
from features.time_features import add_time_features
from features.news_features import add_news_features
from features.market_features import add_market_features
from features.blockchain_features import add_blockchain_features
from features.imputation_pipeline import impute_missing


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # 1. Imputation
    df = impute_missing(df)

    # 2. Time features
    df = add_time_features(df)

    # 3. Categorical encodings
    df = encode_categoricals(df)

    # 4. Amount features
    if "amount" in df.columns:
        df["log_amount"] = np.log1p(df["amount"])
        df["high_amount_flag"] = (df["amount"] > df["amount"].median()).astype(int)

    # 5. News features
    df = add_news_features(df)

    # 6. Market features
    df = add_market_features(df)

    # 7. Blockchain features
    df = add_blockchain_features(df)

    return df
