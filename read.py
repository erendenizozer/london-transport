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

# print(json.dumps(data[0], indent=4))

for line in data:
    print(f"\nLine: {line['name']}")

    print(f"Number of statuses: {len(line['lineStatuses'])}")

    for status in line["lineStatuses"]:
        print(
            status["statusSeverityDescription"],
            "|",
            status.get("reason")
        )

    print(f"Number of disruptions: {len(line['disruptions'])}")