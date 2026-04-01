import pandas as pd
import numpy as np
import joblib

#  Load the saved model and scaler
model = joblib.load("agent_prediction_model.pkl")
scaler = joblib.load("agent_scaler.pkl")

#  Load your dataset to get the feature column structure
df = pd.read_csv("cleaned_encoded_delivery_dataset1.csv")
X = df.drop(columns=['Agents Needed'])  # These were your input features

#  Create a new input sample in the SAME structure
# Example: Modify values according to your scenario
sample_input = pd.DataFrame([[
    14,     # Hour
    50,     # Orders
    30,     # Temperature (°C)
    0,      # Rain (No)
    1,      # Holiday (Yes)
    1,      # Offer Active
    0,      # Competitor
    0, 0, 0, 1, 0,   # Company encoding (e.g., Swiggy = 1)
    0, 0, 1,         # Traffic Level encoding (e.g., High = 1)
    0, 1,            # Order Type encoding
    1, 0             # Area Type encoding
]], columns=X.columns)  # Ensures column names and order match exactly

#  Scale the input using the same scaler
scaled_input = scaler.transform(sample_input)

# Predict Agents Needed
predicted_agents = model.predict(scaled_input)
print(f"\n Predicted Agents Needed: {round(predicted_agents[0])}")
