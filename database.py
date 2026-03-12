import psycopg2

def database_connection():
    try:
        connection = psycopg2.connect(
            user = 'postgres',
            password = '1234',
            host = 'localhost',
            port = '5432',
            database = 'calculator_data'
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