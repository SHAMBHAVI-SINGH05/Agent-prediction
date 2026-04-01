# 📦 Step 1: Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 📂 Step 2: Load the Encoded Dataset
df = pd.read_csv("cleaned_encoded_delivery_dataset1.csv")

# 🧹 Step 3: Quick Preview
print("🔍 Dataset Preview:")
print(df.head())
print("\n🧾 Column Types:")
print(df.dtypes)

# 📌 Step 4: Define Input Features (X) and Target Variable (y)
X = df.drop(columns=['Agents Needed'])
y = df['Agents Needed']

# 🔀 Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ⚖️ Step 6: Scale the Features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 🧠 Step 7: Train the Linear Regression Model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 🎯 Step 8: Predict on Test Data
y_pred = model.predict(X_test_scaled)

# 📊 Step 9: Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n✅ Model Trained Successfully!\n")
print(f"📉 Mean Squared Error (MSE): {mse:.2f}")
print(f"📏 Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"📐 Mean Absolute Error (MAE): {mae:.2f}")
print(f"📈 R² Score (Test): {r2:.2f}")

# 🧪 Step 10: R² Score on Train Set (Overfitting Check)
train_pred = model.predict(X_train_scaled)
r2_train = r2_score(y_train, train_pred)
print(f"🏋️‍♀️ R² Score (Train): {r2_train:.2f}")

# 🎯 Step 11: Approximate Accuracy (just for intuition)
accuracy_approx = 100 * (1 - mae / y_test.mean())
print(f"🎯 Approximate Accuracy: {accuracy_approx:.2f}%")

# 📊 Step 12: Feature Importance (Coefficient Ranking)
importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values(by='Coefficient', key=abs, ascending=False)

print("\n📌 Top 10 Most Influential Features:")
print(importance_df.head(10))

# 📈 Step 13: Visualizations

# a. Actual vs Predicted Scatter Plot
"""plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6, color='teal')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.xlabel("Actual Agents Needed")
plt.ylabel("Predicted Agents Needed")
plt.title("📉 Actual vs Predicted Agents Needed")
plt.grid(True)
plt.tight_layout()
plt.show()"""

# b. Residual Plot (Errors)
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, color='orange')
plt.title("📊 Residual Distribution (Actual - Predicted)")
plt.xlabel("Residuals")
plt.tight_layout()
plt.show()


import pickle

with open("agent_model.pkl", 'wb') as f:
    pickle.dump(model, f)

with open("agent_scaler.pkl", 'wb') as f:
    pickle.dump(scaler, f)

print("✅ Model saved locally!")

