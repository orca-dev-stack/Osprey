import os
import subprocess

def download_kaggle_dataset(dataset: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cmd = [
        "kaggle", "datasets", "download",
        "-d", dataset,
        "-p", os.path.dirname(output_path),
        "--force"
    ]
    subprocess.run(cmd, check=True)

def download_kaggle_competition(competition: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    cmd = [
        "kaggle", "competitions", "download",
        "-c", competition,
        "-p", output_dir,
        "--force"
    ]
    subprocess.run(cmd, check=True)
