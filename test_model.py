import pickle
import pandas as pd

# Load trained model
with open("models/xgb_credit_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

# Fix column names to match training data exactly
sample_input = pd.DataFrame([{
    'Job': 'skilled',
    'Housing': 'own',
    'Purpose': 'radio/TV',
    'Sex': 'male',
    'Saving accounts': 'little',
    'Checking account': 'moderate',
    'Age': 35,
    'Credit amount': 5000,
    'Duration': 24
}])

# Make prediction
prediction = model.predict(sample_input)

# Optional: decode label
label_map = {0: 'bad', 1: 'good'}
print("Prediction:", label_map[prediction[0]])