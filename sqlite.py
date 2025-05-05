import sqlite3
import csv
import os


# connect to sqlite server
conn = sqlite3.connect("output/orders.db")
cur = conn.cursor()


# create tables
cur.executescript("""
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS stores;
DROP TABLE IF EXISTS billing;
DROP TABLE IF EXISTS shipping;
DROP TABLE IF EXISTS line_items;

                  
CREATE TABLE events (
    event_id INTEGER PRIMARY KEY,
    event_name TEXT
);

CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    event_id INTEGER,
    total REAL,
    currency TEXT,
    channel TEXT,
    customer_reference TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

CREATE TABLE stores (
    store_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    store_id TEXT,
    store_name TEXT,
    event_id INTEGER,
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

CREATE TABLE billing (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT,
    phone_number TEXT,
    address TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE shipping (
    order_id TEXT PRIMARY KEY,
    customer_name TEXT,
    phone_number TEXT,
    address TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE line_items (
    item_id TEXT PRIMARY KEY,
    order_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    total REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
                  
""")


# Load CSV files into SQL tables
def load_csv_to_table(csv_path, table_name):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames
        placeholders = ", ".join(["?"] * len(cols))
        sql = f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES ({placeholders})"
        cur.executemany(sql, [tuple(row[col] for col in cols) for row in reader])


csv_dir = "output"
for table in ["events", "orders", "stores", "billing", "shipping", "line_items"]:
    csv_path = os.path.join(csv_dir, f"{table}.csv")
    print(csv_path)
    load_csv_to_table(csv_path, table)

conn.commit()
conn.close()

print("Data loaded into orders.db SQLite database.")
