# Sales Analytics ELT Pipeline

## Project Overview

This project is an end-to-end modern ELT (Extract, Load, Transform) data pipeline built using:

* Python
* Snowflake
* dbt
* Apache Airflow
* Docker

The pipeline ingests sales data from CSV files into Snowflake, performs transformations using dbt, validates data quality using dbt tests, and orchestrates the complete workflow using Airflow.

---

# Architecture

```text
CSV Files
    ↓
Python Ingestion
    ↓
Snowflake RAW Tables
    ↓
dbt Staging Models
    ↓
dbt Mart Models (Dimensions + Facts)
    ↓
dbt Tests & Freshness Checks
    ↓
Airflow Orchestration
```

---

# Architecture Diagram

Detailed architecture is available here:

[View Architecture Diagram](docs/architecture.md)

---

# Tech Stack

| Tool           | Purpose                       |
| -------------- | ----------------------------- |
| Python         | Data ingestion                |
| Snowflake      | Cloud data warehouse          |
| dbt            | Data transformation & testing |
| Apache Airflow | Workflow orchestration        |
| Docker         | Containerized Airflow setup   |
| Git/GitHub     | Version control               |

---

# Project Features

## Data Ingestion

* CSV-based batch ingestion
* Dynamic table loading using Python
* Logging and observability added

## Data Warehouse Modeling

* Staging layer
* Star schema design
* Dimension tables
* Fact tables

## dbt Transformations

* Modular SQL transformations
* Incremental model implementation
* Dependency management using ref()

## Data Quality Checks

Implemented:

* not_null
* unique
* relationships
* accepted_values
* custom business-rule tests

## Orchestration

* Automated DAG execution using Airflow
* Custom cron scheduling
* Dockerized Airflow deployment

## Security Improvements

* Environment variable-based credential management
* .env protection using .gitignore

---

# Project Structure

```text
Sales Analytics ELT Pipeline
│
├── airflow
│   ├── dags
│   ├── config
│   └── docker-compose.yaml
│
├── data
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── dbt_project
│   ├── models
│   ├── tests
│   └── dbt_project.yml
│
├── ingestion
│   └── load_to_snowflake.py
│
├── screenshots
├── docs
├── .env
├── .gitignore
└── README.md
```
---

# How to Run

## 1. Activate Virtual Environment

.\venv\Scripts\Activate.ps1


## 2. Run Ingestion

python ingestion/load_to_snowflake.py


## 3. Run dbt Models

cd dbt_project

dbt run


## 4. Run dbt Tests

dbt test


## 5. Start Airflow

docker compose up


---

# Future Improvements

* S3 integration
* Real-time API ingestion
* Slack/email alerting
* Advanced Airflow monitoring
* Slowly Changing Dimensions (SCD)
* CI/CD integration

---

# Key Learning Outcomes

* ELT pipeline design
* Data warehouse modeling
* dbt transformations and testing
* Workflow orchestration
* Incremental data processing
* Data observability
* Secure configuration management

---

# Author

Mayukh Chowdhury
