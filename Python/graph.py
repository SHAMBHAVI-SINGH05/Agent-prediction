import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import os

# Ensure output folder exists
output_dir = "graphs"
os.makedirs(output_dir, exist_ok=True)

# Read and clean column names
df = pd.read_excel("finaltwo_delivery_dataset_with_promised_actual_and_nulls.xlsx")
df.columns = df.columns.str.strip()

"""#  VISUAL: MISSING VALUES (Before Filling)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='magma')
plt.title("Missing Values Heatmap (Before Filling)")
plt.tight_layout()
plt.savefig(f"{output_dir}/missing_values_before.png")
plt.close()

#  FILLING MISSING VALUES
numeric_cols = ['Orders', 'Agents Needed', 'Temperature (°C)', 'Actual Time (min)']
cat_cols = ['Rain', 'Traffic Level', 'Holiday']

# Save plot of nulls before filling
nulls_before = df[numeric_cols + cat_cols].isnull().sum()

# Fill numeric columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Save plot of nulls after filling
nulls_after = df[numeric_cols + cat_cols].isnull().sum()

# Barplot of before vs after filling nulls
plt.figure(figsize=(10, 6))
width = 0.35
x = np.arange(len(nulls_before))
plt.bar(x - width/2, nulls_before, width, label='Before Filling')
plt.bar(x + width/2, nulls_after, width, label='After Filling')
plt.xticks(ticks=x, labels=nulls_before.index, rotation=45)
plt.ylabel('Missing Values Count')
plt.title('Before vs After Filling Missing Values')
plt.legend()
plt.tight_layout()
plt.savefig(f"{output_dir}/missing_values_comparison.png")
plt.close()

# DTYPE CONVERSION 
for col in ['Hour', 'Orders', 'Agents Needed', 'Actual Time (min)']:
    df[col] = df[col].astype(int)

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

#  PROMISED TIME CALCULATION 
PROMISED_TIME = 10
df['Early By (min)'] = np.where(df['Actual Time (min)'] < PROMISED_TIME, PROMISED_TIME - df['Actual Time (min)'], 0)
df['Delay By (min)'] = np.where(df['Actual Time (min)'] > PROMISED_TIME, df['Actual Time (min)'] - PROMISED_TIME, 0)
df['Timing Deviation Cost'] = (df['Actual Time (min)'] - PROMISED_TIME) ** 2

# Histogram of Deviation Cost
plt.figure(figsize=(8, 6))
sns.histplot(df['Timing Deviation Cost'], kde=True)
plt.title('Timing Deviation Cost Distribution')
plt.tight_layout()
plt.savefig(f"{output_dir}/timing_deviation_cost.png")
plt.close()

# ENCODING 
le = LabelEncoder()
binary_cols = ['Rain', 'Holiday', 'Offer Active', 'Competitor']
for col in binary_cols:
    df[col] = le.fit_transform(df[col].astype(str))

df = pd.get_dummies(df, columns=['Company', 'Traffic Level', 'Order Type', 'Area Type'], drop_first=True)"""

#  OUTLIER REMOVAL (Before & After)
plt.figure()
sns.boxplot(df['Orders'])
plt.title("Orders Before Removing Outliers")
plt.tight_layout()
plt.savefig(f"{output_dir}/orders_before_outliers.png")
plt.close()

Q1 = df['Orders'].quantile(0.25)
Q3 = df['Orders'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
df = df[(df['Orders'] >= lower) & (df['Orders'] <= upper)]

plt.figure()
sns.boxplot(df['Orders'])
plt.title("Orders After Removing Outliers")
plt.tight_layout()
plt.savefig(f"{output_dir}/orders_after_outliers.png")
plt.close()

"""# CORRELATION HEATMAP (Final) 
plt.figure(figsize=(14, 8))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), cmap='coolwarm', annot=False)
plt.title("Final Cleaned Dataset Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{output_dir}/final_correlation_heatmap.png")
plt.close()"""

# Save cleaned dataset
df.to_csv("cleaned_delivery_dataset.csv", index=False)
print(" All graphs saved in 'graphs/' folder and cleaned CSV saved.")
