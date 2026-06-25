import yaml
from ingestion.download_kaggle import download_kaggle_dataset, download_kaggle_competition
from ingestion.download_http import download_http_file
from ingestion.download_bigquery import export_bigquery_table

def load_config(path="config/data_sources.yaml"):
    with open(path) as f:
        return yaml.safe_load(f)

def run_kaggle(cfg):
    for src in cfg.get("kaggle", []):
        if "dataset" in src:
            download_kaggle_dataset(src["dataset"], src["output"])
        elif "competition" in src:
            download_kaggle_competition(src["competition"], src["output"])

def run_http(cfg):
    for src in cfg.get("http", []):
        download_http_file(src["url"], src["output"])

def run_bigquery(cfg):
    for src in cfg.get("bigquery", []):
        export_bigquery_table(
            src["project"],
            src["dataset"],
            src["table"],
            src["output"],
        )

def main():
    cfg = load_config()
    run_kaggle(cfg)
    run_http(cfg)
    run_bigquery(cfg)

if __name__ == "__main__":
    main()
