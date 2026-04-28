import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="sales_db",
        user="postgres",
        password="postgres123",
        host="localhost",
        port="5432"
    )

# -------------------------
# TOTAL REVENUE
# -------------------------
def get_total_revenue():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT SUM(total_amount) FROM sales;")
    result = cur.fetchone()[0]

    cur.close()
    conn.close()

    return result

# -------------------------
# TOTAL ORDERS
# -------------------------
def get_total_orders():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(DISTINCT order_id) FROM sales;")
    result = cur.fetchone()[0]

    cur.close()
    conn.close()

    return result

# -------------------------
# TOP 5 PRODUCTS
# -------------------------
def get_top_products():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT product_name, SUM(total_amount) AS revenue
        FROM sales
        GROUP BY product_name
        ORDER BY revenue DESC
        LIMIT 5;
    """)

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result

# -------------------------
# SALES BY REGION
# -------------------------
def get_sales_by_region():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT region, SUM(total_amount)
        FROM sales
        GROUP BY region;
    """)

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result

# -------------------------
# MONTHLY SALES (CLEAN FORMAT)
# -------------------------
def get_monthly_sales():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT TO_CHAR(order_date, 'YYYY-MM') AS month,
               SUM(total_amount)
        FROM sales
        GROUP BY month
        ORDER BY month;
    """)

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result