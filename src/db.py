import sqlite3
from pathlib import Path

DB_PATH = Path("data/warehouse.db")
SCHEMA_PATH = Path("sql/schema.sql")

def get_connection():
    """Return a connection to the SQLite DB"""
    conn = sqlite3.connect(DB_PATH)
    return conn

def init_db():
    """Create tables in the database from sql/schema.sql"""
    # Read schema.sql
    schema_sql = SCHEMA_PATH.read_text()

    # Connect and execute the schema
    conn = get_connection()
    try:
        conn.executescript(schema_sql)
        conn.commit()
        print("Database initialized from schema.sql")
    finally:
        conn.close()

def run_query(sql: str, params: tuple | None = None):
    """
    Run SELECT query and return all rows and a list of tuples.
    For now this is a simple helper for analytics
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        rows = cur.fetchall()
        return rows
    finally:
        conn.close()

