import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

# Load dataset
data = pd.read_csv("german_credit_data.csv")

print("🔎 Original CSV Columns:", data.columns.tolist())

# Standardize column names
data.columns = data.columns.str.strip().str.lower()

# Auto-rename to expected names
rename_map = {
    "saving_accounts": "Saving accounts",
    "saving account": "Saving accounts",
    "savingaccounts": "Saving accounts",
    "checking_account": "Checking account",
    "checkingaccount": "Checking account",
    "checking account": "Checking account",
    "credit_amount": "Credit amount",
    "amount": "Credit amount",
    "duration": "Duration",
    "purpose": "Purpose",
    "sex": "Sex",
    "job": "Job",
    "housing": "Housing",
    "age": "Age",
    "risk": "Risk"
}

# Apply renaming only if column exists
data.rename(columns={col: rename_map[col] for col in data.columns if col in rename_map}, inplace=True)

print("✅ Renamed Columns:", data.columns.tolist())

# Features & Target
X = data.drop("Risk", axis=1)
y = data["Risk"].map({"good": 1, "bad": 0})  # convert to binary

# Define categorical and numeric features
categorical_features = ["Sex", "Job", "Housing", "Saving accounts", "Checking account", "Purpose"]
numeric_features = ["Age", "Credit amount", "Duration"]

# Preprocessor
preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
    ("num", StandardScaler(), numeric_features)
])

# Model pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", XGBClassifier(use_label_encoder=False, eval_metric="logloss"))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model
pipeline.fit(X_train, y_train)

# Save pipeline
joblib.dump(pipeline, "models/xgb_credit_pipeline.pkl")

print("✅ Model trained and saved to models/xgb_credit_pipeline.pkl")