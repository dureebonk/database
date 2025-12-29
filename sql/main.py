import psycopg
from psycopg import connect, cursor

def get_database_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    try:
        conn = connect(
            dbname="dvdrental",
            user="postgres",
            password="db1234",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None 

conn = get_database_connection()

sql_query = "SELECT first_name, last_name FROM customer;"

if conn:
    try:
        with conn.cursor() as cur:
            cur.execute(sql_query)
            rows = cur.fetchall()
            print(f'{cur.description[0].name}, {cur.description[1].name}')
            for row in rows[:1]:
                print(f"{row[0]}, {row[1]}")
    except Exception as e:
        print(f"Error executing query: {e}")
    finally:
        conn.close()