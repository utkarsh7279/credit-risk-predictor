from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np
import os
import shap
import xgboost as xgb
import pandas as pd

# Initialize FastAPI app
app = FastAPI(title="Credit Risk Prediction API")

# Enable CORS for all origins (for local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Define input schema
class CreditInput(BaseModel):
    Age: int
    Job: str
    Housing: str
    Purpose: str
    Credit_amount: int
    Duration: int
    Sex: str
    Saving_accounts: str
    Checking_account: str

# ✅ Load model
USE_PIPELINE = True

model_path = os.path.join(
    os.path.dirname(__file__),
    "models/xgb_credit_pipeline.pkl" if USE_PIPELINE else "models/xgb_credit_model.pkl"
)

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model. Error: {e}")

# ✅ Column name mapping: snake_case → model’s expected format
column_map = {
    'age': 'Age',
    'job': 'Job',
    'housing': 'Housing',
    'purpose': 'Purpose',
    'credit_amount': 'Credit amount',
    'duration': 'Duration',
    'sex': 'Sex',
    'saving_accounts': 'Saving accounts',
    'checking_account': 'Checking account'
}

# ✅ SHAP explainer
shap_model = model.named_steps['classifier'] if USE_PIPELINE else model
explainer = shap.Explainer(shap_model)

# 🛠️ Option 2: Manual preprocessing (used if not pipeline)
def manual_preprocess(data: CreditInput):
    df = pd.DataFrame([data.dict()])
    df['Job'] = df['Job'].map({
        'unemployed': 0,
        'unskilled': 1,
        'skilled': 2,
        'highly_skilled': 3
    })
    df['Housing'] = df['Housing'].map({
        'own': 0,
        'rent': 1,
        'free': 2
    })
    df['Purpose'] = df['Purpose'].map({
        'car': 0,
        'furniture': 1,
        'radio_tv': 2,
        'education': 3,
        'business': 4,
        'domestic_appliance': 5,
        'repairs': 6,
        'vacation': 7,
        'retraining': 8,
        'other': 9
    })
    return df.values

# ✅ Prediction Endpoint
@app.post("/predict/")
async def predict(data: CreditInput):
    try:
        if USE_PIPELINE:
            input_df = pd.DataFrame([data.dict()])
            input_df = input_df.rename(columns=column_map)  # ✅ Rename to match model's columns
            prediction = model.predict(input_df)[0]
            shap_values = explainer(input_df)
        else:
            processed_input = manual_preprocess(data)
            prediction = model.predict(processed_input)[0]
            shap_values = explainer(processed_input)

        return {
            "prediction": int(prediction),
            "shap_values": shap_values.values[0].tolist()
        }
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}