from src.db import init_db, run_query
from src.load_data import load_customers, load_products, load_orders, load_order_items
from src.analytics import total_revenue_per_customer, customer_revenue_details, revenue_by_country, revenue_by_products

def main():
    init_db()
    load_customers()
    load_products()
    load_orders()
    load_order_items()

    # print("Customers:", run_query("SELECT COUNT(*) FROM customers;"))
    # print("Products:", run_query("SELECT COUNT(*) FROM products;"))
    # print("Orders:", run_query("SELECT COUNT(*) FROM orders;"))
    # print("Order items:", run_query("SELECT COUNT(*) FROM order_items;"))

    rows = revenue_by_products()
    for r in rows:
        print(r)

if __name__ == "__main__":
    main()