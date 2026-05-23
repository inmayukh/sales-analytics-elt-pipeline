from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'mayukh',
}

with DAG(
    dag_id='sales_elt_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 5, 1),
    schedule='15 * * * *',
    catchup=False
) as dag:

    run_ingestion = BashOperator(
        task_id='run_ingestion',
        bash_command="""
        cd /opt/project/ingestion &&
        python load_to_snowflake.py
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

    run_ingestion >> run_dbt >> run_dbt_tests