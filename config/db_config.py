import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="college_db",
        user="postgres",
        password="newpassword123"  # your password
    )
    return conn
