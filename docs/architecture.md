```mermaid
flowchart TD

    A[CSV Source Files<br/>customers, products, orders] --> B[Amazon S3 Bucket<br/>raw/customers<br/>raw/products<br/>raw/orders]

    B --> C[Snowflake External Stage<br/>sales_s3_stage]

    C --> D[Snowflake COPY INTO<br/>Bulk Load from S3]

    D --> E[Snowflake RAW Layer<br/>raw.customers<br/>raw.products<br/>raw.orders]

    E --> F[dbt Staging Layer<br/>stg_customers<br/>stg_products<br/>stg_orders]

    F --> G[dbt Mart Layer<br/>dim_customers<br/>dim_products<br/>fact_orders<br/>fct_sales]

    G --> H[dbt Tests<br/>not_null<br/>unique<br/>relationships<br/>accepted_values<br/>custom tests]

    I[Airflow DAG] --> D
    I --> J[dbt run]
    J --> K[dbt test]

    K --> L[Validated Analytics Tables<br/>Ready for BI / Reporting]

    M[Docker] --> I

    N[.env Credentials] --> D
    N --> J