| Field                      | Type        | Description                                             | Nullable |
| -------------------------- | ----------- | ------------------------------------------------------- | -------- |
| id                         | string      | Unique identifier of the line                           | No       |
| name                       | string      | Human readable name                                     | No       |
| modeName                   | string      | Transport type (e.g: Tube)                              | No       |
| statusSeverity             | int         | Numerical severity level of the line's service status   | No       |
| statusSeverityDescriptions | string/None | Human-readable service status                           | No       |
| reason                     | string/None | Explanation of the current service status or disruption | Yes      |
| validityPeriods            | string/None | Period during which a status is valid                   | No       |
| observed_at                | string/None | When our pipeline collected the data                   | No       |

## Saved CSV (`data/tube_status.csv`)

`fetch_status.py` saves one row per line per run with these columns:

| Column      | Comes from (API field)                    | Example                                  |
| ----------- | ----------------------------------------- | ---------------------------------------- |
| observed_at | set by our script (UTC, ISO 8601)         | 2026-11-22T22:30:00.123456+00:00         |
| line_id     | id                                        | central                                  |
| line_name   | name                                      | Central                                  |
| severity    | lineStatuses[0].statusSeverity            | 6                                        |
| status      | lineStatuses[0].statusSeverityDescription | Severe Delays                            |
| reason      | lineStatuses[0].reason                    | Central Line: Severe delays due to ...   |

`reason` is empty when the line has a good service, because TfL only sends it during a disruption. `modeName` and `validityPeriods` are not saved yet.
