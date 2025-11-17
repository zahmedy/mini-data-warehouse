import pandas as pd
from pathlib import Path
from .db import get_connection

RAW_DATA_DIR = Path("data/raw")

def load_customers(csv_name: str = "customers.csv"):
    """
    Load customers from CSV into customers table
    """
    csv_path = RAW_DATA_DIR / csv_name
    print(f"Loading customers from {csv_path}")

    df = pd.read_csv(csv_path)

    conn = get_connection()

    try:
        # if_exists='append' so we can load multiple times (or switch to 'replace' while testing)
        df.to_sql("customers", conn, if_exists="append", index=False)
        print("Inserted", len(df), "customers into the database.")
    finally:
        conn.close()

def load_products(csv_name: str = "products.csv"):
    """
    Load Products from CSV into the products table
    """
    csv_path = RAW_DATA_DIR / csv_name
    print(f"Loading products from {csv_name}")

    df = pd.read_csv(csv_path)

    conn = get_connection()

    try:
        df.to_sql("products", conn, if_exists="append", index=False)
        print(f"Inserted {len(df)} products into products table")
    finally:
        conn.close()

    