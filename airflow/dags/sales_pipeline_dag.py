from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="sales_elt_pipeline",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule="15 * * * *",
    catchup=False,
) as dag:

    run_ingestion = BashOperator(
        task_id='run_ingestion',
        bash_command="""
        cd /opt/project/ingestion &&
        python load_s3_to_snowflake.py
        """
    )

    check_source_freshness = BashOperator(
    task_id="check_source_freshness",
    bash_command="""
    cd /opt/project/dbt_project &&
    dbt source freshness
    """
    )

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command="""
        cd /opt/project/dbt_project &&
        dbt run
        """
    )

    run_dbt_tests = BashOperator(
        task_id='run_dbt_tests',
        bash_command="""
        cd /opt/project/dbt_project &&
        dbt test
        """
    )

    run_ingestion >> check_source_freshness >> run_dbt >> run_dbt_tests