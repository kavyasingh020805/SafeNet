import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",         # PostgreSQL is running locally
        database="safenetdb",     # The database you created in pgAdmin
        user="postgres",          # Default user is usually 'postgres'
        password="abcd@1234"  # The password you set while installing PostgreSQL
    )
