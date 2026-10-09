import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TFL_API_KEY")

url = f"https://api.tfl.gov.uk/Line/Mode/tube/Status?app_key={API_KEY}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
     print(f"Request failed: {e}")
     raise

try:
    data = response.json()
except requests.JSONDecodeError as e:
     print(f"Invalid JSON response {e}")
     raise



def output():
    records = []

    observe_date = datetime.now(timezone.utc)

    for line in data:
            line_id = line["id"]
            line_name = line["name"]
            if line["lineStatuses"]:
                severity = line["lineStatuses"][0]["statusSeverity"]
                status = line["lineStatuses"][0]["statusSeverityDescription"]
            else:
                 severity = None
                 status = None
            print(f"{observe_date} | {line_id} | {line_name} | {severity} | {status}")

            records.append({
                  "observed_at": observe_date,
                  "line_id": line_id,
                  "line_name": line_name,
                  "severity": severity,
                  "status": status
            })
    return records

records = output() #records contain the original data, not the human readable version