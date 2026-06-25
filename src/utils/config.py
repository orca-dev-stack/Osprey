import json
import os

CONFIG_PATH = "config/train_config.json"

def load_config(path: str = CONFIG_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file not found: {path}")
    with open(path, "r") as f:
        return json.load(f)
