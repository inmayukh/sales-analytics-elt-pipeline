import logging
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Snowflake connection
conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse=os.getenv('SNOWFLAKE_WAREHOUSE'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

cursor = conn.cursor()

# Clear existing data
tables = ["customers", "products", "orders"]

for table in tables:
    cursor.execute(f"DELETE FROM {table}")

print("Old data deleted.")

# File mappings
files = {
    "customers": "../data/customers.csv",
    "products": "../data/products.csv",
    "orders": "../data/orders.csv"
}

# Load fresh data
for table, path in files.items():

    logging.info(f"Starting load for {table.upper()} from {path}")

    df = pd.read_csv(path)

    for _, row in df.iterrows():

        values = tuple(row)

        placeholders = ", ".join(["%s"] * len(values))

        query = f"""
        INSERT INTO {table}
        VALUES ({placeholders})
        """

        cursor.execute(query, values)

    logging.info(f"Loaded {len(df)} rows into {table.upper()} table")
cursor.close()
conn.close()

print("All data loaded successfully!")