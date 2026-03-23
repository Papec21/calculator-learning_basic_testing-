import psycopg2
import os
from dotenv import load_dotenv

def database_connection():
    try:
        load_dotenv()
        connection = psycopg2.connect(
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            database = os.getenv("DB_DATABASE")
        )

        return connection
    
    except Exception as error:
        print(f'Connection error: {error}')

def save_equation(scramble, solve_time):
    try:
        with database_connection() as conn:
            with conn.cursor() as cur:

                sql = "INSERT INTO solves (scramble, solve_time) VALUES (%s, %s)"
                data = (scramble, solve_time)
                cur.execute(sql, data)
                conn.commit()
                return True
    
    # sprawdzanie czy występują błędy (przydaje się :3)
    except Exception as e:
        print(f'Error occurred: {e}')
        return None