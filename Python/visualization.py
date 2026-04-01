import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("cleaned_employee_dataset.xlsx")

sns.set_theme(style="whitegrid")
orders_by_date = df.groupby('Date')['Orders'].sum().reset_index()

"""plt.figure(figsize=(12, 5))
sns.lineplot(data=orders_by_date, x='Date', y='Orders', marker='o')
plt.title("Total Orders Per Day")
plt.xlabel("Date")
plt.ylabel("Total Orders")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()"""

"""avg_agents = df.groupby('Company')['Agents Needed'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=avg_agents, x='Company', y='Agents Needed', palette='Set2')
plt.title("Average Agents Needed by Company")
plt.ylabel("Average Agents")
plt.xlabel("Company")
plt.show()"""

"""heatmap_data = df.pivot_table(index='Hour', columns='Date', values='Orders', aggfunc='sum')

plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlOrRd", annot=False)
plt.title("Order Volume Heatmap (Hour vs Date)")
plt.xlabel("Date")
plt.ylabel("Hour of Day")
plt.show()"""

"""plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Orders', y='Agents Needed', hue='Company', alpha=0.7)
plt.title("Orders vs Agents Needed")
plt.xlabel("Orders")
plt.ylabel("Agents Needed")
plt.legend(title='Company')
plt.show()"""

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Company', y='Temperature (°C)')
plt.title("Temperature Distribution by Company")
plt.show()


