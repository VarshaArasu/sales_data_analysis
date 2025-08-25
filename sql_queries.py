import pandas as pd
import sqlite3
import os
csv_file = "sales_data_cleaned.csv"
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"{csv_file} not found! Run data_cleaning.py first.")
df = pd.read_csv(csv_file)
print("CSV loaded successfully. Columns:", df.columns.tolist())
conn = sqlite3.connect("sales_data.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
print("Data loaded into SQL table 'sales'")
query = """
SELECT Product, SUM(TotalSales) as Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5
"""
top_products = pd.read_sql(query, conn)
print("Top 5 products by revenue:\n", top_products)
conn.close()
