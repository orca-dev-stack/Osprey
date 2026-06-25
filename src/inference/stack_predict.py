import os
import numpy as np
import pandas as pd
import lightgbm as lgb
import xgboost as xgb
from catboost import CatBoostClassifier
from utils.settings import MODEL_DIR
from utils.logger import get_logger

logger = get_logger("stack_predict")


def load_models():
    """Load all tabular models from disk."""
    try:
        lgbm = lgb.Booster(model_file=os.path.join(MODEL_DIR, "lgbm_fraud.txt"))

        xgb_model = xgb.XGBClassifier()
        xgb_model.load_model(os.path.join(MODEL_DIR, "xgb_fraud.json"))

        cat = CatBoostClassifier()
        cat.load_model(os.path.join(MODEL_DIR, "catboost_fraud.cbm"))

        logger.info("Loaded LGBM, XGB, CatBoost models successfully.")
        return lgbm, xgb_model, cat

    except Exception as e:
        logger.error(f"Model loading failed: {e}")
        raise


def stack_predict(df: pd.DataFrame) -> np.ndarray:
    """Run predictions using all three models and return an ensemble score."""
    if df.empty:
        logger.error("Input DataFrame is empty.")
        raise ValueError("Input DataFrame is empty.")

    lgbm, xgb_model, cat = load_models()

    
    X = df.values.astype(float)

    p_lgbm = lgbm.predict(X)
    p_xgb = xgb_model.predict_proba(X)[:, 1]
    p_cat = cat.predict_proba(X)[:, 1]

    ensemble = (p_lgbm + p_xgb + p_cat) / 3.0
    logger.info(f"Stacked prediction generated for {len(ensemble)} samples.")

    return ensemble
