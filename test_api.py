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
    if not isinstance(data,list):
         raise ValueError("Expected a list of lines from TfL API")
    if not data:
         raise ValueError("TfL API returned a empty response")
except requests.JSONDecodeError as e:
     print(f"Invalid JSON response {e}")
     raise

for line in data: # Data validation, making sure we're getting the list correctly and there is no element missing.
    if "id" not in line:
          raise ValueError("A line record ID is missing")
    if "name" not in line:
          raise ValueError("A line record name is missing")
    if "lineStatuses" not in line:
        raise ValueError(f"{line['name']} is missing lineStatuses")
    if not isinstance(line["lineStatuses"], list):
        raise ValueError(f"{line['name']} lineStatuses must be a list")


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
