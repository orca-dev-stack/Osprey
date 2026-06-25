import asyncio
import websockets
import json
import redis
from utils.settings import REDIS_URL

r = redis.Redis.from_url(REDIS_URL)
MARKET_KEY = "osprey:market_stream"

CRYPTO_WS = "wss://stream.binance.com:9443/ws/btcusdt@trade"

async def stream_market():
    async with websockets.connect(CRYPTO_WS) as ws:
        async for msg in ws:
            data = json.loads(msg)
            price = float(data["p"])
            r.set(f"{MARKET_KEY}:btc_price", price)

if __name__ == "__main__":
    asyncio.run(stream_market())
