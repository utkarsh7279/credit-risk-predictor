from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from xgboost import XGBClassifier
import pandas as pd
import pickle
import os

# ✅ Step 1: Load dataset with correct path
csv_path = os.path.join(os.path.dirname(__file__), "german_credit_data.csv")
df = pd.read_csv(csv_path)
df.columns = df.columns.str.lower().str.strip()

# ✅ Step 2: Define correct column names from your CSV
categorical = ['job', 'housing', 'purpose', 'sex', 'saving_accounts', 'checking_account']
numerical = ['age', 'credit_amount', 'duration']
target = 'risk'
print(df.columns.tolist())

X = df[categorical + numerical]
y = df[target].map({'good': 1, 'bad': 0})  # Encode target labels

# ✅ Step 3: Build preprocessing + model pipeline
preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
], remainder='passthrough')

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', XGBClassifier())
])

pipeline.fit(X, y)

# ✅ Step 4: Save pipeline to correct path
model_dir = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(model_dir, exist_ok=True)

with open(os.path.join(model_dir, "xgb_credit_pipeline.pkl"), "wb") as f:
    pickle.dump(pipeline, f)
    print("✅ Model training complete and saved to models/xgb_credit_pipeline.pkl")