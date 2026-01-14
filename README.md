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
Place partner files in ```data/``` directory



