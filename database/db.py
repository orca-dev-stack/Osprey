import os
import psycopg2

DB_DSN = os.getenv("DB_DSN", "postgresql://osprey:osprey@postgres:5432/osprey")

def get_conn():
    return psycopg2.connect(DB_DSN)

def log_score(transaction_id: int, prob: float, risk: str):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO fraud_scores (transaction_id, probability, risk_label)
        VALUES (%s, %s, %s)
        """,
        (transaction_id, prob, risk),
    )
    conn.commit()
    cur.close()
    conn.close()
