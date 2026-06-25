import os
import requests

def download_http_file(url: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    resp = requests.get(url, stream=True)
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
