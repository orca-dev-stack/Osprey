import os
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

MODEL_DIR = "models_artifacts"
os.makedirs(MODEL_DIR, exist_ok=True)


def build_tf_model(input_dim):
    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(input_dim,)),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-3),
        loss="binary_crossentropy",
        metrics=[tf.keras.metrics.AUC(name="auc")],
    )
    return model


def train_tf(X, y, epochs: int = 10, batch_size: int = 512):
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=42
    )

    model = build_tf_model(input_dim=X.shape[1])
    history = model.fit(
        X_train.values,
        y_train.values,
        validation_data=(X_val.values, y_val.values),
        epochs=epochs,
        batch_size=batch_size,
        verbose=1,
    )

    val_preds = model.predict(X_val.values).ravel()
    auc = roc_auc_score(y_val, val_preds)
    print(f"[TensorFlow] Final AUC: {auc:.4f}")

    model.save(os.path.join(MODEL_DIR, "tf_mlp"))
    print("[TensorFlow] Saved model.")
