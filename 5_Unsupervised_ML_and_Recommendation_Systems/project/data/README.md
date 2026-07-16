# Data

This directory contains the interaction dataset supplied with the Udacity IBM
Community recommendation-system project. The project does not require an
external download.

## File

`user-item-interactions.csv` contains 45,993 logical user-article interaction
records and four source columns:

| Column | Description |
|---|---|
| `Unnamed: 0` | Source row identifier retained from the provided dataset |
| `article_id` | Article identifier, stored as a decimal value in the CSV and loaded as an integer by the notebook |
| `title` | Article title and the only supplied article text |
| `email` | Hashed user identifier; missing for 17 interaction records |

Verified aggregates:

- 45,993 interaction records
- 714 unique article IDs
- 714 unique article titles
- 5,148 non-null user identifiers
- 17 records with a missing user identifier

The notebook maps all missing identifiers to one `unknown_user`, resulting in
5,149 modeled users. Multiple rows may represent repeated interactions between
the same user and article. Those rows are counted separately for popularity and
exploratory statistics but collapsed to a binary value in the user-item matrix.

## Integrity

SHA-256 for the provided CSV:

```text
07df24977199e629339723b644a93b8a6452d3a5c70868f7b0a143b14ab59bc6
```

Some quoted article titles contain embedded newline characters. As a result, a
physical line count from tools such as `wc -l` is not the number of CSV records;
use a CSV-aware reader such as `pandas.read_csv`.

## Folder Policy

- Treat `user-item-interactions.csv` as immutable source data.
- Do not edit identifiers, titles, or missing values directly in the CSV.
- Keep cleaning, type conversion, and user mapping reproducible in the notebook.
- Do not replace the file without updating the aggregate checks and checksum in
  this README.
- Treat hashed identifiers as pseudonymous user data and avoid exposing
  row-level records in documentation or generated reports.

The dataset is course-provided. No independent license statement or external
source URL is asserted by this repository.
