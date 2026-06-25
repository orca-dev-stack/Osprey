import os
import requests
from utils.logger import get_logger

logger = get_logger("discord_alerts")

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_alert(message: str):
    """Send alert message to Discord via webhook."""
    if not DISCORD_WEBHOOK:
        logger.error("Discord webhook not configured.")
        return False

    payload = {
        "content": message
    }

    try:
        r = requests.post(DISCORD_WEBHOOK, json=payload, timeout=5)
        if r.status_code in (200, 204):
            logger.info("Discord alert sent.")
            return True
        else:
            logger.error(f"Discord error: {r.text}")
            return False

    except Exception as e:
        logger.error(f"Discord alert failed: {e}")
        return False
