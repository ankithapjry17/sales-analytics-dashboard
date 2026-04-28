from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analytics import (
    get_total_revenue,
    get_total_orders,
    get_top_products,
    get_sales_by_region,
    get_monthly_sales
)

app = FastAPI()

# Allow React frontend to call this API later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Sales API is running"}

@app.get("/revenue")
def revenue():
    return {"total_revenue": get_total_revenue()}

@app.get("/orders")
def orders():
    return {"total_orders": get_total_orders()}

@app.get("/top-products")
def top_products():
    data = get_top_products()
    return [{"product": p, "revenue": r} for p, r in data]

@app.get("/region-sales")
def region_sales():
    data = get_sales_by_region()
    return [{"region": r, "revenue": s} for r, s in data]

@app.get("/monthly-sales")
def monthly_sales():
    data = get_monthly_sales()
    return [{"month": m, "revenue": s} for m, s in data]