import os
from sklearn.ensemble import IsolationForest
from sklearn.metrics import roc_auc_score

MODEL_DIR = "models_artifacts"
os.makedirs(MODEL_DIR, exist_ok=True)


def train_anomaly(X, y):
    iso = IsolationForest(
        n_estimators=200,
        contamination=0.02,
        random_state=42,
        n_jobs=-1,
    )
    iso.fit(X)

    scores = -iso.score_samples(X)  # higher = more anomalous
    auc = roc_auc_score(y, scores)
    print(f"[IsolationForest] AUC: {auc:.4f}")

    import joblib

    joblib.dump(iso, os.path.join(MODEL_DIR, "isoforest.pkl"))
    print("[IsolationForest] Saved model.")
