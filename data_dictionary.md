| Field                      | Type        | Description                                             | Nullable |
| -------------------------- | ----------- | ------------------------------------------------------- | -------- |
| id                         | string      | Unique identifier of the line                           | No       |
| name                       | string      | Human readable name                                     | No       |
| modeName                   | string      | Transport type (e.g: Tube)                              | No       |
| statusSeverity             | int         | Numerical severity level of the line's service status   | No       |
| statusSeverityDescriptions | string/None | Human-readable service status                           | No       |
| reason                     | string/None | Explanation of the current service status or disruption | Yes      |
| validityPeriods            | string/None | Period during which a status is valid                   | No       |
| observed_at                | string/None | EWhen our pipeline collected the data                   | No       |
