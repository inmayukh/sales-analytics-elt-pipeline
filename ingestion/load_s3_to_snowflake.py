import os
import logging
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

tables = ["customers", "products", "orders"]

copy_commands = {
    "customers": """
        COPY INTO customers
        FROM @sales_s3_stage/customers/customers.csv
        FILE_FORMAT = csv_format
    """,
    "products": """
        COPY INTO products
        FROM @sales_s3_stage/products/products.csv
        FILE_FORMAT = csv_format
    """,
    "orders": """
        COPY INTO orders
        FROM @sales_s3_stage/orders/orders.csv
        FILE_FORMAT = csv_format
    """
}

try:
    logging.info("Connecting to Snowflake")

    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE"),
    )

    cursor = conn.cursor()

    logging.info("Connected to Snowflake successfully")

    for table in tables:
        logging.info(f"Truncating RAW.{table.upper()} table")
        cursor.execute(f"TRUNCATE TABLE {table}")

        logging.info(f"Loading {table.upper()} from S3 stage")
        cursor.execute(copy_commands[table])

        results = cursor.fetchall()
        logging.info(f"COPY INTO result for {table.upper()}: {results}")

    logging.info("S3 to Snowflake load completed successfully")

    cursor.close()
    conn.close()

except Exception as e:
    logging.error(f"S3 to Snowflake load failed: {str(e)}")
    raise