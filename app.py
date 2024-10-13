from flask import Flask
import os
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

def check_db_connection():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT", "5432")
        )
        connection.close()
        return True
    except OperationalError:
        return False

@app.route('/')
def hello_world():
    db_connected = check_db_connection()
    if db_connected:
        return "Hello, World! Connected to the database."
    else:
        return "Hello, World! Not connected to the database."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
