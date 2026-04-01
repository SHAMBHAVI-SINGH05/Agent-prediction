import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

# Load cleaned data
df = pd.read_csv("cleaned_encoded_delivery_dataset1.csv")

# Features and target
X = df.drop("Agents Needed", axis=1)
y = df["Agents Needed"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

# Predict & evaluate
y_pred = dt.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print(f" Mean Absolute Error: {mae:.2f}")

accuracy_approx = 100 * (1 - mae / y_test.mean())
print(f" Approximate Accuracy: {accuracy_approx:.2f}%")


# Save the model
with open("agent_model_dt.pkl", "wb") as f:
    pickle.dump(dt, f)

print(" Decision Tree model saved as agent_model_dt.pkl")
