import pandas as pd
import sqlite3
df = pd.read_csv("sales_data_cleaned.csv")  
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
