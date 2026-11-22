import csv
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("TFL_API_KEY")

CSV_PATH = "data/tube_status.csv"  # where every run's records get saved
CSV_COLUMNS = ["observed_at", "line_id", "line_name", "severity", "status", "reason"]

url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"
params = {"app_key": API_KEY}  # passed as params so the key isn't baked into the URL string

try:
    response = requests.get(url, params=params, timeout=10)
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
                reason = line["lineStatuses"][0].get("reason")  # only present when there's a disruption
            else:
                 severity = None
                 status = None
                 reason = None
            print(f"{observe_date} | {line_id} | {line_name} | {severity} | {status}")

            records.append({
                  "observed_at": observe_date,
                  "line_id": line_id,
                  "line_name": line_name,
                  "severity": severity,
                  "status": status,
                  "reason": reason
            })
    return records


def save_records(records):
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)  # create the data/ folder if it doesn't exist yet
    file_is_new = not os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:  # "a" = append, so old runs are kept
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        if file_is_new:
            writer.writeheader()  # column names go on the first line, only once
        for record in records:
            row = dict(record)
            row["observed_at"] = record["observed_at"].isoformat()  # e.g. 2026-11-22T22:30:00+00:00
            writer.writerow(row)

    print(f"Saved {len(records)} records to {CSV_PATH}")


records = output() #records contain the original data, not the human readable version
save_records(records)
