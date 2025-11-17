from src.db import init_db, run_query
from src.load_data import load_customers, load_products

def main():
    # 1) Initialize schema (only needed once / when you reset)
    init_db()

    # 2) Load customers CSV into the warehouse
    load_customers()

    # 3) load produtcs CSV into warehouse
    load_products()

    print(run_query("SELECT * FROM customers;"))
    print(run_query("SELECT * FROM products;"))

if __name__ == "__main__":
    main()