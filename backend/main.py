from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import shap

# Load the model
with open("models/xgb_credit_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

# Define input schema
class CreditInput(BaseModel):
    job: str
    housing: str
    purpose: str
    sex: str
    saving_accounts: str
    checking_account: str
    age: float
    credit_amount: float
    duration: float

@app.post("/predict")
def predict(data: CreditInput):
    try:
        input_dict = data.dict()

        # Make a DataFrame with correct column names
        input_df = pd.DataFrame([input_dict])

        # Prediction
        prediction = model.predict(input_df)[0]
        prob = model.predict_proba(input_df)[0][1]

        # SHAP Explanation
        explainer = shap.Explainer(model.named_steps["classifier"])
        transformed_input = model.named_steps["preprocessor"].transform(input_df)
        shap_values = explainer(transformed_input)

        return {
            "prediction": int(prediction),
            "probability_of_risk": float(prob),
            "shap_values": shap_values.values.tolist()[0]
        }

    except Exception as e:
        print("❌ Error in prediction route:", str(e))
        return {"error": str(e)}
    