from database import get_connection

try:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT version();")  # This checks PostgreSQL version
    db_version = cur.fetchone()
    print("✅ Connected to PostgreSQL!")
    print("PostgreSQL version:", db_version)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Failed to connect to the database.")
    print(e)
