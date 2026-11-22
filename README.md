# london-transport

Polls the [TfL Unified API](https://api.tfl.gov.uk/) for the current status of every London Underground line and builds one record per line with the time it was observed.

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

## Files

- `fetch_status.py`: fetches line statuses, validates the response, and builds the records.
- `data_dictionary.md`: what each field means.
