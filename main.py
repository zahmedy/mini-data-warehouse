from src.db import init_db, run_query
from src.load_data import load_customers, load_products, load_orders, load_order_items

def main():
    init_db()
    load_customers()
    load_products()
    load_orders()
    load_order_items()

    print("Customers:", run_query("SELECT COUNT(*) FROM customers;"))
    print("Products:", run_query("SELECT COUNT(*) FROM products;"))
    print("Orders:", run_query("SELECT COUNT(*) FROM orders;"))
    print("Order items:", run_query("SELECT COUNT(*) FROM order_items;"))

if __name__ == "__main__":
    main()