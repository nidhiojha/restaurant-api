import requests
import pandas as pd
import time
from datetime import datetime
from app.config import CSV_URL, CSV_PATH, UPDATE_INTERVAL

def download_csv():
    response = requests.get(CSV_URL)
    if response.status_code == 200:
        with open(CSV_PATH, "wb") as file:
            file.write(response.content)
        print(f"CSV updated at {datetime.now()}")

def load_data():
    return pd.read_csv(CSV_PATH)

def update_data_periodically():
    while True:
        download_csv()
        time.sleep(UPDATE_INTERVAL)
