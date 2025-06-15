import pandas as pd

# CSV file path, adjust if needed
df = pd.read_csv("data/german_credit_data.csv")

# Print all column names
print(df.columns.tolist())