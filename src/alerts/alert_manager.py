from alerts.slack_alerts import send_slack_alert
from alerts.email_alerts import send_email_alert
from alerts.sms_alerts import send_sms_alert
from alerts.discord_alerts import send_discord_alert
from utils.logger import get_logger
import time
import redis
from utils.settings import REDIS_URL

logger = get_logger("alert_manager")
r = redis.Redis.from_url(REDIS_URL)
ALERT_STREAM = "osprey:alerts"


def send_alert(message: str, severity: str = "medium"):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")

    # Push into Redis Stream for dashboard + case system
    r.xadd(ALERT_STREAM, {
        "message": message,
        "severity": severity,
        "timestamp": ts,
    })

    logger.info(f"Alert queued: {message} ({severity})")

    # Always send Slack + Discord
    send_slack_alert(message)
    send_discord_alert(message)

    # Medium → Email
    if severity == "medium":
        send_email_alert("OSPREY ALERT", message)

    # High → Email + SMS
    if severity == "high":
        send_email_alert("OSPREY FRAUD ALERT", message)
        send_sms_alert(message)
