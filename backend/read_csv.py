import pandas as pd

print("STARTED")

# read CSV
df = pd.read_csv("train.csv")

print("Original rows:", len(df))

# -----------------------------
# CLEAN + SELECT DATA
# -----------------------------

# rename columns
df = df.rename(columns={
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Product Name": "product_name",
    "Category": "category",
    "Region": "region",
    "Sales": "total_amount"
})

# keep only needed columns
df = df[[
    "order_id",
    "order_date",
    "product_name",
    "category",
    "region",
    "total_amount"
]]

# add quantity (since missing)
df["quantity"] = 1

# price = total_amount (simple assumption)
df["price"] = df["total_amount"]

# convert date
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

# remove bad rows
df = df.dropna()

print("\nCleaned rows:", len(df))
print("\nPreview:")
print(df.head())