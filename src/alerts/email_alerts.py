import os
import smtplib
from email.mime.text import MIMEText
from utils.logger import get_logger

logger = get_logger("email_alerts")

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
ALERT_EMAIL_TO = os.getenv("ALERT_EMAIL_TO")

def send_email_alert(subject: str, body: str):
    if not SMTP_USER or not SMTP_PASS or not ALERT_EMAIL_TO:
        logger.error("Email settings not configured.")
        return False

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = ALERT_EMAIL_TO

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, ALERT_EMAIL_TO, msg.as_string())
        server.quit()
        logger.info("Email alert sent.")
        return True
    except Exception as e:
        logger.error(f"Email alert failed: {e}")
        return False
