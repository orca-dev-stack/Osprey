import json
import pika
from utils.logger import get_logger
from alerts.alert_manager import send_alert

logger = get_logger("rabbit_worker")

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="osprey.alerts.queue", durable=True)


def callback(ch, method, properties, body):
    alert = json.loads(body.decode())
    logger.info(f"Processing alert from RabbitMQ: {alert}")
    send_alert(alert["message"], alert["severity"])
    ch.basic_ack(delivery_tag=method.delivery_tag)


def run_worker():
    logger.info("RabbitMQ worker started.")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue="osprey.alerts.queue",
        on_message_callback=callback,
    )
    channel.start_consuming()
