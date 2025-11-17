from .db import run_query

def total_revenue_per_customer():
    """
    Return a list of (customer_id, total_revenue) from warehouse 
    """
    sql = """
        SELECT
            o.customer_id,
            SUM(oi.quantity * oi.unit_price) AS total_revenue
        FROM orders o
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY o.customer_id
        ORDER BY total_revenue DESC;
        """

    rows = run_query(sql)
    return rows

def customer_revenue_details():
    """
    Return a list of (customer_id, first_name, last_name, country, total_revenue)
    """
    sql = """
        SELECT
            c.customer_id,
            c.first_name,
            c.last_name,
            c.country,
            SUM(oi.quantity * oi.unit_price) AS total_revenue
        FROM customers c
        JOIN orders o
            ON c.customer_id = o.customer_id
        JOIN order_items oi
            ON o.order_id = oi.order_id
        GROUP BY c.customer_id, c.first_name, c.last_name, c.country
        ORDER BY total_revenue DESC;
        """
    return run_query(sql)

def revenue_by_country():
    sql = """
    SELECT 
        c.country,
        SUM(oi.quantity * oi.unit_price) as total_revenue
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    JOIN order_items oi
        ON o.order_id = oi.order_id
    GROUP BY c.country
    ORDER BY total_revenue DESC;
    """
    return run_query(sql)

def revenue_by_products():
    sql = """
    SELECT
        p.product_id,
        p.product_name,
        SUM(oi.quantity * oi.unit_price) as total_revenue
    FROM products p
    JOIN order_items oi
        ON p.product_id = oi.product_id
    GROUP BY p.product_id, p.product_name
    ORDER BY total_revenue DESC;
    """
    return run_query(sql)