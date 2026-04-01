import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Read and preprocess
df = pd.read_excel("finaltwo_delivery_dataset_with_promised_actual_and_nulls.xlsx")
df.columns = df.columns.str.strip()

print(df.head())
print(df.info())


plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='magma')
plt.title("Missing Values Heatmap")
plt.show()

#MISSING VALUE CLEANING
numeric_cols = ['Orders', 'Agents Needed', 'Temperature (°C)', 'Actual Time (min)']
print("\nMissing Numeric BEFORE Cleaning:\n", df[numeric_cols].isnull().sum())

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing Numeric AFTER Cleaning:\n", df[numeric_cols].isnull().sum())

cat_cols = ['Rain', 'Traffic Level', 'Holiday']
print("\nMissing Categorical BEFORE Cleaning:\n", df[cat_cols].isnull().sum())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Categorical AFTER Cleaning:\n", df[cat_cols].isnull().sum())

# DATE + DTYPE CLEANING 
print("\nDtypes BEFORE conversion:")
print(df[['Hour', 'Orders', 'Agents Needed', 'Actual Time (min)', 'Date']].dtypes)

for col in ['Hour', 'Orders', 'Agents Needed', 'Actual Time (min)']:
    df[col] = df[col].astype(int)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print("\nDtypes AFTER conversion:")
print(df[['Hour', 'Orders', 'Agents Needed', 'Actual Time (min)', 'Date']].dtypes)

# DEVIATION / COST CALCULATION (Moved here)
PROMISED_TIME = 10

df['Early By (min)'] = np.where(df['Actual Time (min)'] < PROMISED_TIME,
                                PROMISED_TIME - df['Actual Time (min)'], 0)
df['Delay By (min)'] = np.where(df['Actual Time (min)'] > PROMISED_TIME,
                                df['Actual Time (min)'] - PROMISED_TIME, 0)
df['Timing Deviation Cost'] = (df['Actual Time (min)'] - PROMISED_TIME) ** 2

print("\n Timing Deviation Columns:")
print(df[['Actual Time (min)', 'Early By (min)', 'Delay By (min)', 'Timing Deviation Cost']].head())

# ENCODING 
le = LabelEncoder()
binary_cols = ['Rain', 'Holiday', 'Offer Active', 'Competitor']

print("\nBinary BEFORE Label Encoding:")
print(df[binary_cols].head())

for col in binary_cols:
    df[col] = le.fit_transform(df[col].astype(str))

print("\nBinary AFTER Label Encoding:")
print(df[binary_cols].head())

print("\nShape BEFORE One-Hot Encoding:", df.shape)
df = pd.get_dummies(df, columns=['Company', 'Traffic Level', 'Order Type', 'Area Type'], drop_first=True)
print("Shape AFTER One-Hot Encoding:", df.shape)



Q1 = df['Orders'].quantile(0.25)
Q3 = df['Orders'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['Orders'] >= lower) & (df['Orders'] <= upper)]


# FINAL CHECKS & STATS 
print("\nFinal Null Check:\n", df.isnull().sum().sort_values(ascending=False))
print("\nTiming Deviation Cost Stats:\n", df['Timing Deviation Cost'].describe())



# Save cleaned data
df.to_csv("cleaned_delivery_dataset.csv", index=False)
print("\n Cleaned dataset saved as 'cleaned_delivery_dataset.csv'")
