import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TFL_API_KEY")

url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"

params = {
    "app_key": API_KEY
}

response = requests.get(url, params=params)

data = response.json()

for line in data:
        line_id = line["id"]
        line_name = line["name"]
        severity = line["lineStatuses"][0]["statusSeverity"]
        status = line["lineStatuses"][0]["statusSeverityDescription"]
        print(f"{line_id} | {line_name} | {severity} | {status}")
