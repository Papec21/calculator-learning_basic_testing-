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

if __name__ == '__main__':
    database_connection()


def save_equation(result, operation, num1, num2):
    try:
        with database_connection() as conn:
            with conn.cursor() as cur:

                sql = "INSERT INTO equations (result, operation, num1, num2) VALUES (%s, %s, %s, %s)"
                data = (result, operation, num1, num2)
                cur.execute(sql, data)
                conn.commit()
                return True
    
    except Exception as e:
        print(f'Error occurred: {e}')
        return None