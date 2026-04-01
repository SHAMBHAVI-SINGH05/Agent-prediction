# USER INPUT PREDICTION SECTION
import joblib

# Save models
joblib.dump(ridge, "ridge_model.pkl")
joblib.dump(lasso, "lasso_model.pkl")

# Load any one model for prediction
loaded_model = joblib.load("ridge_model.pkl")  # Change to "lasso_model.pkl" to use Lasso

print("\n🔮 Predict Agent Needed Using Your Input")
print("⚠️ Enter values in the same order as the training features.")

# Get the column names used in training
feature_names = list(X.columns)

# Take input for each feature from user
user_input = []
for col in feature_names:
    val = input(f"Enter value for {col}: ")
    try:
        user_input.append(float(val))  # Convert to float (you can change this if some are categorical)
    except ValueError:
        print(f"Invalid input for {col}, expected a number.")
        exit()

# Convert to DataFrame for prediction
user_df = pd.DataFrame([user_input], columns=feature_names)

# Predict using the loaded model
predicted_agents = loaded_model.predict(user_df)[0]
print(f"\n🎯 Predicted Number of Agents Needed: {round(predicted_agents)}")
