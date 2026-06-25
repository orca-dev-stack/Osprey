from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "osprey",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "osprey_fraud_pipeline",
    default_args=default_args,
    description="Osprey end-to-end fraud pipeline",
    schedule_interval="0 3 * * *",  # daily at 03:00
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    ingestion = BashOperator(
        task_id="ingestion",
        bash_command="cd /opt/osprey && python train_all.py --stage ingestion",
    )

    processing = BashOperator(
        task_id="processing",
        bash_command="cd /opt/osprey && python train_all.py --stage processing",
    )

    training = BashOperator(
        task_id="training",
        bash_command="cd /opt/osprey && python train_all.py --stage training",
    )

    ingestion >> processing >> training
