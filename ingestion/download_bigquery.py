import os
from google.cloud import bigquery

def export_bigquery_table(project: str, dataset: str, table: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    client = bigquery.Client(project=project)

    query = f"""
    SELECT *
    FROM `{project}.{dataset}.{table}`
    LIMIT 100000
    """
    job = client.query(query)
    df = job.result().to_dataframe()
    df.to_parquet(output_path)
