TRAIN_CONFIG = {
    "tabular": {
        "test_size": 0.2,
        "random_state": 42,
        "lgbm": {
            "learning_rate": 0.05,
            "num_leaves": 64,
            "feature_fraction": 0.8,
            "bagging_fraction": 0.8,
            "bagging_freq": 5,
            "num_boost_round": 500,
            "early_stopping_rounds": 50,
        },
        "xgb": {
            "n_estimators": 500,
            "max_depth": 8,
            "learning_rate": 0.05,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
        },
        "catboost": {
            "iterations": 500,
            "depth": 8,
            "learning_rate": 0.05,
        },
    },
    "pytorch": {
        "epochs": 10,
        "batch_size": 512,
        "lr": 1e-3,
    },
    "tensorflow": {
        "epochs": 10,
        "batch_size": 512,
        "lr": 1e-3,
    },
    "autoencoder": {
        "epochs": 10,
        "batch_size": 512,
        "lr": 1e-3,
    },
    "anomaly": {
        "n_estimators": 200,
        "contamination": 0.02,
    },
    "gnn": {
        "epochs": 20,
        "lr": 1e-3,
    },
}
