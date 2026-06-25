import pandas as pd
from textblob import TextBlob

RISK_KEYWORDS = [
    "fraud", "scam", "money laundering", "ponzi",
    "hack", "breach", "illegal", "suspicious"
]

def extract_sentiment(text: str) -> float:
    if not isinstance(text, str) or not text.strip():
        return 0.0
    return TextBlob(text).sentiment.polarity

def keyword_risk_score(text: str) -> int:
    if not isinstance(text, str):
        return 0
    text_lower = text.lower()
    return sum(1 for kw in RISK_KEYWORDS if kw in text_lower)

def add_news_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "news" not in df.columns:
        df["news_sentiment"] = 0.0
        df["news_risk"] = 0
        df["news_volatility"] = 0.0
        return df

    df["news_sentiment"] = df["news"].apply(extract_sentiment)
    df["news_risk"] = df["news"].apply(keyword_risk_score)
    df["news_volatility"] = df["news_sentiment"].rolling(5).std().fillna(0)

    return df
