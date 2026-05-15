# Data

This project uses CMS Provider Data and resolves the current CSV URL from the
official metadata endpoint:

<https://data.cms.gov/provider-data/api/1/metastore/schemas/dataset/items/xubh-q36u>

## Folder Policy

- `raw/`: downloaded source CSVs exactly as provided by CMS.

Do not edit raw files by hand. The notebook can download the source file again
from CMS metadata whenever the local copy is missing.
