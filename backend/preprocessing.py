# preprocessing.py
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(filepath):
    print(f"Reading from: {filepath}")
    df = pd.read_csv(filepath)

    print("Columns:", df.columns)
    print("Shape:", df.shape)
    print("First few rows:\n", df.head())

    if 'Risk' not in df.columns:
        raise ValueError(f"'Risk' column not found. Found columns: {df.columns}")
    

    if 'Unnamed: 0' in df.columns:
        df.drop('Unnamed: 0', axis=1, inplace=True)

    # Encode categorical variables
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop('Risk', axis=1)
    y = df['Risk'].apply(lambda x: 1 if x == 'good' else 0)

    return train_test_split(X, y, test_size=0.2, random_state=42)