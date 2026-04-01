import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("agent_model_rf_tuned.pkl")

# Define feature names in correct order (replace these with your actual column names used in training)
feature_names = ['Date', 'Day', 'Hour', 'Temperature (°C)', 'Rain', 'Holiday', 'Offer Active', 'Competitor',
 'Orders', 'Promised Time (min)', 'Actual Time (min)', 'Delivered On Time', 'Early By (min)', 
 'Delay By (min)', 'Timing Deviation Cost', 'Company_JioMart', 'Company_Swiggy', 'Company_Zepto', 
 'Traffic Level_Low', 'Traffic Level_Medium', 'Order Type_Food', 'Order Type_Grocery', 'Area Type_Urban']


# Take input from user
print(" Enter values for prediction (based on your feature set):")

user_data = {}

for feature in feature_names:
    value = float(input(f"{feature}: "))
    user_data[feature] = value

# Create DataFrame from input
input_df = pd.DataFrame([user_data])

# Predict
prediction = model.predict(input_df)[0]

print(f"\nPredicted Agents Needed: {round(prediction)}")
