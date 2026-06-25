import numpy as np
from utils.logger import get_logger

logger = get_logger("unified_score")


def combine_scores(
    tabular_score: float,
    anomaly_score: float,
    gnn_score: float,
    news_risk: float,
    market_volatility: float,
    mempool_pressure: float,
) -> float:
    """Weighted ensemble of all fraud intelligence signals."""

    weights = {
        "tabular": 0.40,
        "anomaly": 0.20,
        "gnn": 0.20,
        "news": 0.10,
        "market": 0.05,
        "mempool": 0.05,
    }

    score = (
        weights["tabular"] * tabular_score +
        weights["anomaly"] * anomaly_score +
        weights["gnn"] * gnn_score +
        weights["news"] * news_risk +
        weights["market"] * market_volatility +
        weights["mempool"] * mempool_pressure
    )

    score = float(np.clip(score, 0.0, 1.0))
    logger.info(f"Unified fraud score: {score:.4f}")

    return score
