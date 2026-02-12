from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd
import shap
import os

app = FastAPI(title="Credit Risk Predictor API", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model with error handling
try:
    model_path = os.path.join(os.path.dirname(__file__), "models", "xgb_credit_pipeline.pkl")
    model = joblib.load(model_path)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {model_path}. Please ensure the model is trained and committed to the repository.")

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy", "service": "credit-risk-backend"}

@app.get("/")
def root():
    return {"message": "Credit Risk Predictor API", "docs": "/docs"}

# Pydantic schema (frontend se lowercase keys aayengi)
class CreditInput(BaseModel):
    age: int
    sex: str
    job: str
    housing: str
    saving_accounts: str
    checking_account: str
    credit_amount: float
    duration: int
    purpose: str

@app.post("/predict")
def predict(data: CreditInput):
    try:
        # Mapping frontend -> training columns
        input_dict = {
            "Age": data.age,
            "Sex": data.sex,
            "Job": data.job,
            "Housing": data.housing,
            "Saving accounts": data.saving_accounts,
            "Checking account": data.checking_account,
            "Credit amount": data.credit_amount,
            "Duration": data.duration,
            "Purpose": data.purpose
        }

        df = pd.DataFrame([input_dict])

        # Prediction
        prediction = int(model.predict(df)[0])

        # SHAP explainability (wrapped in try–except)
        shap_values = None
        try:
            explainer = shap.Explainer(model.named_steps["classifier"])
            X_transformed = model.named_steps["preprocessor"].transform(df)
            shap_values = explainer(X_transformed)
            shap_values = shap_values.values.tolist()
        except Exception as e:
            shap_values = None   # fail gracefully

        return {
            "success": True,
            "prediction": prediction,
            "features": input_dict,
            "shap_values": shap_values
        }

    except Exception as e:
        return {
            "success": False,
            "prediction": None,
            "shap_values": None,
            "error": str(e)
        }