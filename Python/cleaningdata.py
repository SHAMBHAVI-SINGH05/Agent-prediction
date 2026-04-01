import pandas as pd
import numpy as np
df= pd.read_excel("final_realistic_employee_dataset_with_date.xlsx")

df['Date'] = pd.to_datetime(df['Date'],dayfirst=True,errors='coerce')
print(df.head())
print("Total length",len(df))
df.drop_duplicates(inplace=True)
print(df.head())

print("Total rows after removing duplicates:",len(df))

print("Missing values before cleaning:")

print(df[['Orders','Agents Needed','Temperature (°C)']].isnull().sum())
for col in['Orders','Agents Needed','Temperature (°C)']:
    df[col] = df[col].fillna(df[col].median())

print("\nMissing values after cleaning:")
print(df[['Orders','Agents Needed','Temperature (°C)']].isnull().sum())

print(df[['Rain','Traffic Level','Order Type','Holiday']].isnull().sum())

categorical_cols =['Rain','Traffic Level','Order Type','Holiday']
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df[categorical_cols].isnull().sum())

print("Data types before conversion:")
print(df[['Hour', 'Orders', 'Agents Needed']].dtypes)

for col in ['Hour', 'Orders', 'Agents Needed']:
    df[col] = df[col].astype(int)


print(df[['Hour', 'Orders', 'Agents Needed']].dtypes)

df.columns = df.columns.str.strip()

categorical_cols = ['Company', 'Rain', 'Traffic Level', 'Holiday']
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print(df[categorical_cols].isnull().sum())

print("Data types before conversion:")
print(df[['Hour', 'Orders', 'Agents Needed']].dtypes)

for col in ['Hour', 'Orders', 'Agents Needed']:
    df[col] = df[col].astype(int)

df.columns = df.columns.str.strip()

categorical_cols = ['Company', 'Rain', 'Traffic Level', 'Holiday', 'Offer Active', 'Area Type', 'Order Type']
for col in categorical_cols:
    if col in df.columns: 
        df[col] = df[col].astype(str).str.strip().str.title()
df = df[df['Orders'] < 1000]  
df = df[df['Agents Needed'] < 100]

print(df.isnull().sum())
print("\nFinal cleaned dataset shape:", df.shape)
print(df.head())

df.to_csv("cleaned_employee_dataset.csv", index=False)
print("\nFile saved as 'cleaned_employee_dataset.csv'")