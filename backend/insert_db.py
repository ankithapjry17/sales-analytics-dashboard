import pandas as pd
import psycopg2

# connect to database
conn = psycopg2.connect(
    dbname="sales_db",
    user="postgres",
    password="postgre@ise",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# read and clean data (same as before)
df = pd.read_csv("train.csv")

df = df.rename(columns={
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Product Name": "product_name",
    "Category": "category",
    "Region": "region",
    "Sales": "total_amount"
})

df = df[[
    "order_id",
    "order_date",
    "product_name",
    "category",
    "region",
    "total_amount"
]]

df["quantity"] = 1
df["price"] = df["total_amount"]

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df = df.dropna()

print("Inserting rows:", len(df))

# insert into database
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO sales (order_id, order_date, product_name, category, region, quantity, price, total_amount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["order_id"],
        row["order_date"],
        row["product_name"],
        row["category"],
        row["region"],
        int(row["quantity"]),
        float(row["price"]),
        float(row["total_amount"])
    ))

conn.commit()
cursor.close()
conn.close()

print("DONE ✅ Data inserted")