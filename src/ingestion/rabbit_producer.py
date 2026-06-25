import json
import pika
from utils.logger import get_logger

logger = get_logger("rabbit_producer")

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="osprey.alerts.queue", durable=True)


def queue_alert(message: str, severity: str = "medium"):
    payload = {"message": message, "severity": severity}
    channel.basic_publish(
        exchange="",
        routing_key="osprey.alerts.queue",
        body=json.dumps(payload),
        properties=pika.BasicProperties(delivery_mode=2),  # persistent
    )
    logger.info(f"Queued alert in RabbitMQ: {payload}")
