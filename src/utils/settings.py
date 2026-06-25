import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# -----------------------------
# PATHS
# -----------------------------
DATA_DIR = os.getenv("DATA_DIR", os.path.join(BASE_DIR, "data"))
MODEL_DIR = os.getenv("MODEL_DIR", os.path.join(BASE_DIR, "models_artifacts"))
LOG_DIR = os.getenv("LOG_DIR", os.path.join(BASE_DIR, "logs"))

# -----------------------------
# KAGGLE / DATA SOURCES
# -----------------------------
KAGGLE_DATASET = os.getenv("KAGGLE_DATASET", "ieee-fraud-detection")

BIGQUERY_PROJECT = os.getenv("BIGQUERY_PROJECT", "your-gcp-project")
BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET", "crypto_chain")
BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE", "transactions")

# -----------------------------
# DATABASES / CACHING
# -----------------------------
DB_DSN = os.getenv("DB_DSN", "postgresql://osprey:osprey@localhost:5432/osprey")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# -----------------------------
# Ensure directories exist
# -----------------------------
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
