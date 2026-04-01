import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib


# 1. Load and prepare dataset

df = pd.read_csv('cleaned_encoded_delivery_dataset1.csv')
X = df.drop(columns=['Agents Needed'])
y = df['Agents Needed']


# 2. Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 3. Initialize and Train Models

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)

# 4. Save Models

joblib.dump(ridge, 'ridge_model.pkl')
joblib.dump(lasso, 'lasso_model.pkl')

# 5. Evaluation Function

def evaluate_model(model, X_test, y_test):
    pred = model.predict(X_test)
    mse = mean_squared_error(y_test, pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    return {"MSE": mse, "RMSE": rmse, "MAE": mae, "R2 Score": r2}

ridge_metrics = evaluate_model(ridge, X_test, y_test)
lasso_metrics = evaluate_model(lasso, X_test, y_test)

print("Ridge Evaluation:", ridge_metrics)
print("Lasso Evaluation:", lasso_metrics)



# Use trained model (Ridge in this case)
model = joblib.load("ridge_model.pkl")

# Take feature names from dataset
feature_names = list(X.columns)

# Take user input for prediction
print("\n Enter values to predict Agent Needed:")
user_input = {}
for feature in feature_names:
    try:
        value = float(input(f"{feature}: "))
    except ValueError:
        value = int(input(f"{feature} (0 or 1): "))
    user_input[feature] = value


input_df = pd.DataFrame([user_input])
prediction = model.predict(input_df)

print(f"\n Predicted Agent Needed: {prediction[0]:.2f}")
