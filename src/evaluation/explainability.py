import shap
from utils.settings import DATA_DIR, MODEL_DIR, DB_DSN

model_path = os.path.join(MODEL_DIR, "lgbm_fraud.txt")

def explain_model(model, X_sample):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_sample)
    shap.summary_plot(shap_values, X_sample)
