from sklearn.metrics import roc_auc_score, f1_score, precision_score, recall_score

def evaluate_model(y_true, y_pred):
    return {
        "auc": roc_auc_score(y_true, y_pred),
        "f1": f1_score(y_true, y_pred > 0.5),
        "precision": precision_score(y_true, y_pred > 0.5),
        "recall": recall_score(y_true, y_pred > 0.5),
    }
