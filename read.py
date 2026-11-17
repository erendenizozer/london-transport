import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TFL_API_KEY")

url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"

params = {
    "app_key": API_KEY
}

response = requests.get(url, params=params, timeout=10)

response.raise_for_status()

data = response.json()

for line in data:
    print(
        line["name"],
        "Statuses:",
        len(line["lineStatuses"])
    )