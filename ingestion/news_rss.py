import feedparser
import time
import redis
from utils.settings import REDIS_URL

r = redis.Redis.from_url(REDIS_URL)
NEWS_KEY = "osprey:news_stream"

RSS_FEEDS = [
    "https://news.google.com/rss/search?q=fraud",
    "https://news.google.com/rss/search?q=crypto+scam",
]

def poll_feeds():
    while True:
        for feed_url in RSS_FEEDS:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                item = {
                    "title": entry.get("title"),
                    "summary": entry.get("summary"),
                    "link": entry.get("link"),
                    "published": entry.get("published"),
                }
                r.lpush(NEWS_KEY, str(item))
        time.sleep(60)
