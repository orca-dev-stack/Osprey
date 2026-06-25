import os
from twilio.rest import Client
from utils.logger import get_logger

logger = get_logger("sms_alerts")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")
TWILIO_TO = os.getenv("TWILIO_TO")

def send_sms_alert(message: str):
    if not TWILIO_SID or not TWILIO_TOKEN:
        logger.error("Twilio not configured.")
        return False

    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=TWILIO_TO
        )
        logger.info("SMS alert sent.")
        return True
    except Exception as e:
        logger.error(f"SMS alert failed: {e}")
        return False
