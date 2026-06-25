from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from models.inference import stack_predict
from alerts.engine import maybe_alert
from database.db import log_score
from database.cache import cache_score
from inference.stack_predict import stack_predict
from inference.unified_score import combine_scores
from alerts.alert_manager import send_alert

app = FastAPI(title="Osprey Fraud Scoring API")

class Transaction(BaseModel):
    transaction_id: int | None = None
    amount: float
    country: str | None = None
    hour: float | None = None
    day: float | None = None

@app.post("/score")
def score_transaction_endpoint(transaction: Transaction):
    features_df = pd.DataFrame([transaction.dict()])
    score = score_transaction(features_df)
    log_score(transaction.transaction_id, score)
    cache_score(transaction.transaction_id, score)
    tabular_prob = stack_predict(features_df)[0]
    anomaly_prob = anomaly_model.predict(features_df)[0]
    gnn_prob = gnn_model.predict(features_df)[0]

    news_risk = features_df["news_risk"].iloc[0]
    market_vol = features_df["market_volatility"].iloc[0]
    mempool_pressure = features_df["mempool_pressure"].iloc[0]

    maybe_alert(transaction.transaction_id, score)
    return {"transaction_id": transaction.transaction_id, "score": score}

    unified = combine_scores(
        tabular_score=tabular_prob,
        anomaly_score=anomaly_prob,
        gnn_score=gnn_prob,
        news_risk=news_risk,
        market_volatility=market_vol,
        mempool_pressure=mempool_pressure,
    )

    return unified

if unified_score > 0.85:
    send_alert(
        message=f" HIGH-RISK FRAUD DETECTED — Score: {unified_score:.3f}",
        severity="high"
    )
elif unified_score > 0.65:
    send_alert(
        message=f" Medium risk transaction — Score: {unified_score:.3f}",
        severity="medium"
    )

@app.get("/health")
def health():
    return {"status": "ok"}



