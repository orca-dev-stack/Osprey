import smtplib
from email.message import EmailMessage

def classify_risk(prob: float) -> str:
    if prob > 0.9:
        return "CRITICAL"
    if prob > 0.7:
        return "HIGH"
    if prob > 0.4:
        return "MEDIUM"
    return "LOW"

def send_email_alert(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "alerts@osprey.local"
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("user", "password")
        server.send_message(msg)

def maybe_alert(transaction_id: int, prob: float, to_email: str):
    risk = classify_risk(prob)
    if risk in {"HIGH", "CRITICAL"}:
        subject = f"[Osprey] {risk} fraud risk for transaction {transaction_id}"
        body = f"Transaction {transaction_id} scored {prob:.3f} ({risk})."
        send_email_alert(to_email, subject, body)
    return risk
