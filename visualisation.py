
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
csv_file = "sales_data_cleaned.csv"
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"{csv_file} not found! Run data_cleaning.py first.")
df = pd.read_csv(csv_file)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly_revenue = df.groupby('Month')['TotalSales'].sum().reset_index()
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_revenue, x='Month', y='TotalSales', marker='o')
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Revenue")
plt.tight_layout()
plt.show()
