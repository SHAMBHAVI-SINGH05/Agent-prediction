import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the cleaned dataset
df = pd.read_csv("cleaned_delivery_dataset.csv")

# Step 1: Check data types BEFORE encoding
print(" Data types before encoding:")
print(df.dtypes)

# Step 2: Identify object or boolean columns
non_numeric_cols = df.select_dtypes(include=['object', 'bool']).columns.tolist()
print("\nNon-numeric columns:", non_numeric_cols)

# Step 3: Apply Label Encoding
le = LabelEncoder()
for col in non_numeric_cols:
    print(f"Encoding column: {col}")
    df[col] = le.fit_transform(df[col].astype(str))  # convert everything to string, then encode

# Step 4: Confirm everything is numeric now
print("\n Data types after encoding:")
print(df.dtypes)

# Step 5: Save the encoded dataset
df.to_csv("cleaned_encoded_delivery_dataset1.csv", index=False)
print("\n Encoded dataset saved as 'cleaned_encoded_delivery_dataset1.csv'")

# Preview
print("\n Final preview:")
print(df.head())
