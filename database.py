import sqlite3

def get_db():
    return sqlite3.connect("db.sqlite3")

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aplicacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE NOT NULL,
            token TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
