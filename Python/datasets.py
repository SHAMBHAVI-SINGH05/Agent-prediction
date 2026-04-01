import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import math

# Step 1: Generate the base dataset
start_date = datetime(2024, 6, 1)
companies = ['Zepto', 'Blinkit', 'Swiggy', 'JioMart']
data = []

for day in range(7):
    date = start_date + timedelta(days=day)
    day_name = date.strftime('%A')
    is_holiday = day_name in ['Saturday', 'Sunday']

    for company in companies:
        for hour in range(9, 22):  # 9 AM to 9 PM
            traffic = random.choices(['Low', 'Medium', 'High'], weights=[0.2, 0.5, 0.3])[0]
            temp = random.randint(28, 42)
            rain = random.choice(['Yes', 'No'])
            offer = random.choice(['Yes', 'No'])
            area = random.choice(['Urban', 'Suburban'])
            order_type = random.choice(['Food', 'Grocery', 'Electronics'])
            competitor = random.choice(['Yes', 'No'])

            base_orders = random.randint(120, 300)
            if traffic == 'High':
                base_orders += random.randint(30, 60)
            if offer == 'Yes':
                base_orders += random.randint(20, 50)
            if rain == 'Yes':
                base_orders = int(base_orders * 1.15)
            if is_holiday:
                base_orders = int(base_orders * 1.25)
            if hour in [12, 13, 14, 19, 20, 21]:
                base_orders += random.randint(40, 100)

            agents_needed = max(1, math.ceil(base_orders / random.randint(10, 15)))

            data.append({
                "Company": company,
                "Date": date.strftime('%Y-%m-%d'),
                "Day": day_name,
                "Hour": hour,
                "Traffic Level": traffic,
                "Temperature (°C)": temp,
                "Rain": rain,
                "Holiday": "Yes" if is_holiday else "No",
                "Offer Active": offer,
                "Area Type": area,
                "Order Type": order_type,
                "Competitor": competitor,
                "Orders": base_orders,
                "Agents Needed": agents_needed
            })

# Step 2: Create DataFrame
df = pd.DataFrame(data)

# Step 3: Add Actual Delivery Time (min)
np.random.seed(42)
df['Actual Delivery Time (min)'] = np.random.randint(7, 13, size=len(df))

# Step 4: Add Early Delivery Impact
def compute_impact(time):
    if time < 9:
        return 'High'
    elif time == 9:
        return 'Medium'
    else:
        return 'Low'

df['Early Delivery Impact'] = df['Actual Delivery Time (min)'].apply(compute_impact)

# Step 5: Randomly introduce nulls (~5%) into selected columns
columns_to_null = [
    'Traffic Level', 'Temperature (°C)', 'Rain',
    'Holiday', 'Orders', 'Actual Delivery Time (min)'
]

for col in columns_to_null:
    null_indices = df.sample(frac=0.05, random_state=42).index
    df.loc[null_indices, col] = np.nan

# Step 6: Save to Excel
df.to_excel("updated_employee_dataset_with_impact_and_nulls1.xlsx", index=False)
print("Final dataset saved as 'updated_employee_dataset_with_impact_and_nulls.xlsx'")
