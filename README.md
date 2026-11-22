# london-transport

Polls the [TfL Unified API](https://api.tfl.gov.uk/) for the current status of every London Underground line, builds one record per line with the time it was observed, and appends those records to a CSV file so you build up a history over time.

## Setup

Requires Python 3.9+.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root with your TfL API key (get one at https://api-portal.tfl.gov.uk/):

```
TFL_API_KEY=your_key_here
```

## Usage

```bash
python fetch_status.py
```

This prints one line per tube line:

```
<observed_at UTC> | <line_id> | <line_name> | <severity> | <status>
```

and appends the same records (plus the disruption `reason`, if any) to `data/tube_status.csv`. The file and the `data/` folder are created on the first run; each later run adds new rows at the bottom. Run the script from the project folder so the file lands in `data/` there. The `data/` folder is in `.gitignore`, so your collected data stays on your computer and is not committed.

You can open the CSV in Excel, Numbers, or Google Sheets.

## Files

- `fetch_status.py`: fetches line statuses, validates the response, builds the records, and saves them to `data/tube_status.csv`.
- `data_dictionary.md`: what each field means.
