import sqlite3

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS twisters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            title TEXT,
            description TEXT,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            place TEXT
        )
    """)
    conn.execute("""
        twister events (
            title of twister,
            deaths from twister
        )
    """)
    conn.commit()
    conn.close()