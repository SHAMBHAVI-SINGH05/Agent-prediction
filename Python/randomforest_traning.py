import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import numpy as np

# Load dataset
df = pd.read_csv("cleaned_encoded_delivery_dataset1.csv")

# Define features (X) and target (y)
X = df.drop("Agents Needed", axis=1)
y = df["Agents Needed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest with GridSearchCV
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

rf = RandomForestRegressor(random_state=42)
grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5, n_jobs=-1, verbose=1)

# Fit the model
grid_search.fit(X_train, y_train)

# Best model
best_rf = grid_search.best_estimator_

# Predict
y_pred = best_rf.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
r2_train = r2_score(y_train, best_rf.predict(X_train))

print(f"Best Parameters: {grid_search.best_params_}")
print(f" Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R² Score (Test): {r2:.2f}")
print(f"R² Score (Train): {r2_train:.2f}")
print(f"Approximate Accuracy: {r2 * 100:.2f}%")

# Save the model
joblib.dump(best_rf, "agent_model_rf_tuned.pkl")
print(" Tuned Random Forest model saved as agent_model_rf_tuned.pkl")
