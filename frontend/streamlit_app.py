import streamlit as st
import requests
from requests.auth import HTTPBasicAuth
import matplotlib.pyplot as plt

st.title("Credit Risk Prediction")

# User input form
job = st.selectbox("Job", ["unskilled", "skilled", "highly skilled"])
housing = st.selectbox("Housing", ["own", "free", "rent"])
purpose = st.selectbox("Purpose", ["car", "radio/TV", "education", "furniture/equipment", "business", "domestic appliances"])
sex = st.selectbox("Sex", ["male", "female"])
saving_accounts = st.selectbox("Saving Accounts", ["little", "moderate", "quite rich", "rich", "no_info"])
checking_account = st.selectbox("Checking Account", ["little", "moderate", "rich", "no_info"])
age = st.number_input("Age", min_value=18, max_value=100, value=30)
credit_amount = st.number_input("Credit Amount", min_value=0, max_value=100000, value=5000)
duration = st.number_input("Duration (in months)", min_value=1, max_value=72, value=24)

if st.button("Predict"):
    payload = {
        "job": job,
        "housing": housing,
        "purpose": purpose,
        "sex": sex,
        "saving_accounts": saving_accounts,
        "checking_account": checking_account,
        "age": age,
        "credit_amount": credit_amount,
        "duration": duration
    }

    try:
        auth = HTTPBasicAuth("admin", "password")  # Adjust/remove if not needed
        response = requests.post("http://127.0.0.1:8000/predict", auth=auth, json=payload)
        result = response.json()

        st.write("API response:", result)

        if "prediction" in result:
            st.success(f"Prediction: {'Good' if result['prediction'] == 1 else 'Bad'} Credit Risk")
            st.write("🔢 Probability of Risk:", round(result["probability_of_risk"], 4))

            # SHAP Values as JSON (optional raw display)
            st.subheader("📊 SHAP Values (Raw)")
            st.json(result["shap_values"])

            # 🎯 NEW: SHAP Feature Importance Bar Plot
            st.subheader("📊 SHAP Feature Impact (Top 10)")
            shap_vals = result["shap_values"]
            feature_names = result.get("feature_names", [f"feature_{i}" for i in range(len(shap_vals))])
            shap_data = list(zip(feature_names, shap_vals))
            shap_data.sort(key=lambda x: abs(x[1]), reverse=True)
            top_features = shap_data[:10]
            labels = [f[0] for f in top_features]
            values = [f[1] for f in top_features]
            fig, ax = plt.subplots(figsize=(8, 5))
            colors = ['green' if val > 0 else 'red' for val in values]
            ax.barh(labels[::-1], values[::-1], color=colors[::-1])
            ax.set_xlabel("SHAP Value")
            ax.set_ylabel("Feature")
            ax.set_title("Top 10 Feature Impacts on Prediction")
            st.pyplot(fig)
        else:
            st.error(f"⚠️ API Error: {result.get('error', 'No prediction returned.')}")
    except Exception as e:
        st.error(f"Connection Error: {e}")