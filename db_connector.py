import sqlite3

def execute_sql_query(query):
    conn = sqlite3.connect("db/ecommerce.db")
    try:
        result = conn.execute(query).fetchall()
        return result
    except Exception as e:
        return str(e)
    finally:
        conn.close()
