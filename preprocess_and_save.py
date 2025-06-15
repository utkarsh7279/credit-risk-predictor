import pandas as pd

# Load the original raw dataset (adjust filename if needed)
df = pd.read_csv("german_credit_data.csv")

# ✅ Standardize column names to match API schema
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
df.rename(columns={
    'saving accounts': 'saving_accounts',
    'checking account': 'checking_account',
    'credit amount': 'credit_amount'
}, inplace=True)
# Optional cleaning (drop NA rows or fill)
df = df.dropna()

# ✅ Save cleaned data
df.to_csv("german_credit_cleaned.csv", index=False)

print("✅ Cleaned dataset saved as german_credit_cleaned.csv")