import os
import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
r = redis.Redis.from_url(REDIS_URL)

def cache_score(transaction_id: int, prob: float, risk: str):
    r.hset(f"tx:{transaction_id}", mapping={"prob": prob, "risk": risk})
