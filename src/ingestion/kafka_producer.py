import json
from kafka import KafkaProducer
from utils.logger import get_logger

logger = get_logger("kafka_producer")

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)


def publish_transaction(tx: dict, topic: str = "osprey.transactions.raw"):
    """Send a transaction event into Kafka."""
    producer.send(topic, tx)
    logger.info(f"Published transaction to {topic}: {tx}")
