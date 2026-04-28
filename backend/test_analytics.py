from analytics import (
    get_total_revenue,
    get_total_orders,
    get_top_products,
    get_sales_by_region,
    get_monthly_sales
)

print("Total Revenue:", get_total_revenue())
print("Total Orders:", get_total_orders())
print("\nTop Products:", get_top_products())
print("\nSales by Region:", get_sales_by_region())
print("\nMonthly Sales:", get_monthly_sales())