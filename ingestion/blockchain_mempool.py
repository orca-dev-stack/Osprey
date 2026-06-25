import requests
import time
import redis
from feast import FeatureStore
from utils.settings import REDIS_URL
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float32, Int64

r = redis.Redis.from_url(REDIS_URL)
MEMPOOL_KEY = "osprey:mempool"

BITCOIN_MEMPOOL_API = "https://mempool.space/api/mempool/recent"

def poll_mempool():
    while True:
        try:
            resp = requests.get(BITCOIN_MEMPOOL_API, timeout=5)
            txs = resp.json()
            for tx in txs:
                r.lpush(MEMPOOL_KEY, str(tx))
        except Exception as e:
            print("[Mempool] Error:", e)
        time.sleep(10)


wallet = Entity(name="wallet_id", join_keys=["wallet_id"])

wallet_source = FileSource(
    path="data/features/wallet_features.parquet",
    timestamp_field="event_timestamp",
)

wallet_features = FeatureView(
    name="wallet_features",
    entities=[wallet],
    ttl=None,
    schema=[
        Field(name="wallet_degree", dtype=Int64),
        Field(name="wallet_in_degree", dtype=Int64),
        Field(name="wallet_out_degree", dtype=Int64),
        Field(name="risk_score", dtype=Float32),
    ],
    source=wallet_source,
)

store = FeatureStore(repo_path="feature_store/feature_repo")

features = store.get_online_features(
    features=["wallet_features:wallet_degree", "wallet_features:risk_score"],
    entity_rows=[{"wallet_id": wallet_id}],
).to_dict()