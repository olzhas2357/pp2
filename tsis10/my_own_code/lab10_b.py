import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port = 5432
    )
    connection.autocommit = True
    print("Connection established successfully!")
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE SNAKE_SCORE (
            id SERIAL PRIMARY KEY,
            users varchar(50) not null,
            users_SCORE integer not null
            );"""
    )

    print("[INFO] Table created successfully")


except Exception as ex:
    print("[INFO] error occurred:", ex)

finally:
    if connection:
        connection.close()
        print("[INFO] connection closed")