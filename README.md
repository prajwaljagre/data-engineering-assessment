# Data Engineering Partner Ingestion Pipeline

## Overview
This project implements a simple, config-driven data ingestion pipeline that standardizes eligibility data from multiple partner files into a single unified output schema.

Each partner may provide data in different formats (file type, delimiter, column names). These differences are handled through configuration rather than hard-coded logic, allowing the pipeline to scale easily as new partners are added.

## How to Run the Pipeline

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add partner files

Place partner input files in the data/ directory.
Example:
data/acme.txt
data/bettercare.csv

### 3. Run the ingestion script

From the project root directory:
```bash
python src/ingest.py
```

### 4. Output
A unified, standardized CSV file will be generated at:
```bash
output/unified_output.csv
```

## Output Schema

All partner data is standardized to the following schema:
```
external_id
first_name
last_name
dob(YYYY-MM-DD)
email(lowercase)
phone(XXX-XXX-XXXX)
partner_code
```
## How to Add a New Partner
To add a new partner, no changes to the ingestion logic are required.
Steps:

1. Open src/partner_config.py

2. Add a new entry to the PARTNER_CONFIG dictionary specifying:
- File delimiter
- Partner code
- Column mappings (partner column → standard column)

##Example:
```python
"newpartner": {
    "delimiter": "\t",
    "partner_code": "NEWPARTNER",
    "column_mapping": {
        "member_id": "external_id",
        "given_name": "first_name",
        "family_name": "last_name",
        "birth_date": "dob",
        "email_address": "email",
        "phone_number": "phone"
    }
}
```

3. Place the new partner file in the data/ directory.

4. Call the ingestion function with the new partner key.

The pipeline will automatically process the new partner using the provided configuration.



