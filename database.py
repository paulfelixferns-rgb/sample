import sqlite3
import os

DB_NAME = "dc.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    return conn

def create_table():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dc_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dc_date TEXT,
            distributor TEXT,
            amount REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()

    print("✅ Table created successfully")
