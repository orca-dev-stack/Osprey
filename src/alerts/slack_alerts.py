import os
import requests
from utils.logger import get_logger

logger = get_logger("slack_alerts")

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK_URL")

def send_slack_alert(message: str):
    if not SLACK_WEBHOOK:
        logger.error("Slack webhook not configured.")
        return False

    payload = {"text": message}

    try:
        r = requests.post(SLACK_WEBHOOK, json=payload, timeout=5)
        if r.status_code == 200:
            logger.info("Slack alert sent.")
            return True
        else:
            logger.error(f"Slack error: {r.text}")
            return False
    except Exception as e:
        logger.error(f"Slack alert failed: {e}")
        return False
