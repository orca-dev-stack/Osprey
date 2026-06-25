import pandas as pd
import yfinance as yf

def get_market_price(ticker: str) -> float:
    try:
        data = yf.download(ticker, period="1d", interval="1h")
        return float(data["Close"].iloc[-1])
    except:
        return 0.0

def add_market_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["btc_price"] = get_market_price("BTC-USD")
    df["eth_price"] = get_market_price("ETH-USD")
    df["sp500"] = get_market_price("^GSPC")

    df["market_volatility"] = df[["btc_price", "eth_price"]].std(axis=1)

    return df
