import pandas as pd

# Read CSV file
df = pd.read_csv("/data/customers.csv")

# Print dataframe
print(df)

# Show basic information
print("\nDataset Info:")
print(df.info())

# Show total records
print("\nTotal Records:")
print(len(df))