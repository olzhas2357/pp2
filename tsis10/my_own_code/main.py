import psycopg2
from config import host, user, password, db_name

def create():
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phonebook(
                id SERIAL PRIMARY KEY,
                first_name varchar(50) not null,
                last_name varchar(50) not null,
            )"""
        )
        print("[INFO] Table created successfully")

def insert():
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO phonebook(first_name, last_name) VALUES
            ('NURZHAMAL', 'KOSHKARBAEVA'), ('ZHANEL', 'TLEPBERGENOVA');"""
        )
        print("[INFO] DATA WAS SUCCESSFULLY INSERTED")

def update():
    with connection.cursor() as cursor:
        cursor.execute(
            """UPDATE phonebook SET first_name = 'Alikhan', last_name='Hauryz' WHERE id = 3; """
        )
        print("[INFO] UPDATED")

def get_data_select():
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT last_name FROM phonebook WHERE first_name = 'OLZHAS';"""
        )
        print(cursor.fetchone())

def delete_table():
    with connection.cursor() as cursor:
        cursor.execute(
            """DROP TABLE player cascade ;"""
        )
        print("[INFO] Table was deleted")

def delete_column():
    with connection.cursor() as cursor:
        cursor.execute(
            """DELETE FROM phonebook WHERE first_name = 'RAMAZAN';"""
        )
        print("[INFO] Column was deleted")

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

    # # create a new table
    # create()

    # # insert data into a table
    # insert()

    # # get data from a table
    # get_data_select()

    # # delete a table
    # # if you need delete table but cannot you can use cascade
    delete_table()

    # # delete column
    # delete_column()

    # update column
    # update()



except Exception as ex:
    print("[INFO] error occurred:", ex)

finally:
    if connection:
        connection.close()
        print("[INFO] connection closed")