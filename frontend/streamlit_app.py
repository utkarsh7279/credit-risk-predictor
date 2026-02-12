import streamlit as st
import requests
import joblib
import os

# -------------------------------
# Config
# -------------------------------
# Use environment variable for deployed backend, fallback to local
# Try Streamlit secrets first (for Streamlit Cloud), then env var, then local
try:
    BACKEND_URL = st.secrets.get("BACKEND_URL", os.getenv("BACKEND_URL", "http://127.0.0.1:8000/predict"))
except:
    BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000/predict")

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config(page_title="Credit Risk Predictor", layout="wide")
st.title("💳 AI-Powered Credit Risk Prediction")

# -------------------------------
# Input Form
# -------------------------------
with st.form("credit_form"):
    st.subheader("Enter Applicant Details")

    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    sex = st.selectbox("Sex", ["male", "female"])
    job = st.selectbox("Job", ["unskilled", "skilled", "highly skilled", "management"])
    housing = st.selectbox("Housing", ["own", "rent", "free"])
    saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "rich", "quite rich"])
    checking_account = st.selectbox("Checking account", ["little", "moderate", "rich", "quite rich"])
    credit_amount = st.number_input("Credit amount", min_value=100, max_value=20000, value=5000)
    duration = st.slider("Duration (months)", 4, 72, 24)
    purpose = st.selectbox("Purpose", ["car", "furniture", "radio/TV", "education", "business", "domestic appliance", "repairs"])

    submitted = st.form_submit_button("🔍 Predict Risk")

# -------------------------------
# Handle Form Submit
# -------------------------------
if submitted:
    with st.spinner("Making prediction... ⏳"):
        try:
            payload = {
                "age": age,
                "sex": sex,
                "job": job,
                "housing": housing,
                "saving_accounts": saving_accounts,
                "checking_account": checking_account,
                "credit_amount": credit_amount,
                "duration": duration,
                "purpose": purpose
            }

            response = requests.post(BACKEND_URL, json=payload)

            if response.status_code == 200:
                result = response.json()

                if result.get("success"):
                    # ✅ Prediction
                    prediction = "Good Credit Risk" if result["prediction"] == 1 else "Bad Credit Risk"
                    st.success(f"✅ Prediction: {prediction}")

                    # 🔎 SHAP values
                    if result.get("shap_values"):
                        st.subheader("🔎 SHAP Feature Contributions")
                        st.json(result["shap_values"])
                    else:
                        st.warning("⚠️ SHAP explanation not available for this prediction.")
                else:
                    st.error(f"❌ Prediction failed: {result.get('error')}")

            else:
                st.error(f"🚨 API Error: {response.status_code}\n\n{response.text}")

        except Exception as e:
            st.error(f"🚨 API call failed or SHAP error:\n\n{str(e)}")