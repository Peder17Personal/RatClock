import sqlite3

def get_db_version(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA data_version;")
    return cursor.fetchone()[0]
