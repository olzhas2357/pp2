import psycopg2
from config import host, user, password, db_name

print("1 - CREAT TABLE or TABLE NAME:\n2 - INSERT TABLE\n3 - UPDATE TABLE\n4 - DELETE COLUMN")
a = input()
c = int(input())

def create():
    with connection.cursor() as cursor:
        cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {a}(
                id SERIAL PRIMARY KEY,
                first_name varchar(50) not null,
                last_name varchar(50) not null,
                phone int not null
            )"""
        )
        print("[INFO] Table created successfully")

def insert(f, l , p):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO {a} (first_name, last_name, phone) VALUES
            {f, l , p};"""
        )
        print("[INFO] DATA WAS SUCCESSFULLY INSERTED")

def update(n, f, l, p):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE {a} SET first_name = '{f}', last_name = '{l}', phone = {p} WHERE id = {n}"""
        )
        print("[INFO] UPDATED")

def delete_column(n):
    with connection.cursor() as cursor:
        cursor.execute(
           f"""DELETE FROM {a} WHERE first_name = '{n}';"""
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
    if c == 1:
        create()
    elif c == 2:
        f, l, p = input("first name: "), input("last name: "), int(input("phone :"))
        insert(f, l , p)
    elif c == 3:
        n = int(input("ID: "))
        q, w, e = input("first name: "), input("last name: "), int(input("phone :"))
        update(n, q, w, e)
    elif c == 4:
        n = input("first name: ")
        delete_column(n)
except Exception as ex:
    print("[INFO] error occurred:", ex)

finally:
    if connection:
        connection.close()
        print("[INFO] connection closed")