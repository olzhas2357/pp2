import psycopg2
import re
import csv


def main():
    connection = psycopg2.connect(
        host="localhost",
        database="python",
        user="postgres",
        password="kbtu2023"
    )
    on = True
    mode = 'ASC'
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook3(
          id SERIAL PRIMARY KEY,
          first_name VARCHAR(50) NOT NULL,
          last_name VARCHAR(50) NOT NULL,
          phone_number VARCHAR(12) NOT NULL,
          CHECK (LENGTH(phone_number) = 12 AND phone_number LIKE '+7%')
        );""")
    while on:
        a = int(input("type:\n 1-add,\n2-delete,\n3-edit,\n4-look,\n5-clear book,\n6-resort,\n7-import from csv,\n8-select with limit and offset \n:"))
        if a == 1:
            try:
                name_to_insert = input("enter name: ")
                last_name = input("last name: ")
                number_to_insert = input("enter phonebook number: ")
                with connection.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO phonebook3(first_name,last_name, phone_number)
                    VALUES ('{name_to_insert}', '{last_name}', '{number_to_insert}')""")
            except Exception as ex:
                print("You stupid nigga write your phone number correct ")
        elif a == 4:
            with connection.cursor() as cursor:
                if mode == 'ASC':
                    cursor.execute(f"""SELECT * FROM phonebook3 ORDER BY first_name ASC""")
                if mode == 'DESC':
                    cursor.execute(f"""SELECT * FROM phonebook3 ORDER BY first_name DESC""")
                all = cursor.fetchall()
                for _, name, last_name, phone in all:
                    print("|" + name + " " + last_name + "---" + phone + "|")
        elif a == 2:

            name_to_delete = input("enter to delete: ")
            with connection.cursor() as cursor:
                cursor.execute(f"DELETE FROM phonebook3 WHERE first_name = '{name_to_delete}' OR phone_number='{name_to_delete}'")
        elif a == 3:
            editing_name = input("what contact you will edit?: ")
            new_name = input("new name: ")
            new_last_name = input("new last name: ")
            new_number = input("new phonebook number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE phonebook3 SET first_name='{new_name}' WHERE first_name='{editing_name}'")
                cursor.execute(f"UPDATE phonebook3 SET last_name='{new_last_name}' WHERE first_name='{new_name}'")
                cursor.execute(f"UPDATE phonebook3 SET phone_number='{new_number}' WHERE first_name='{new_name}'")
        elif a == 5:
            with connection.cursor() as cursor:
                cursor.execute("TRUNCATE TABLE phonebook3;")
        elif a == 6:
            mode_change = input("1-by alphabetical,2-by inverse alphabetical ")
            if mode_change == 1:
                mode = 'ASC'
            else:
                mode = 'DESC'
        elif a == 7:
            # read from a file and insert its contents into a database table
            path=input("give path,NOT RELATIVE ")
            with open(f"{path}", 'r') as file:
                patt = '\n'
                content = file.read()
                for cont in list(re.split(patt, content)):
                    conte = list(re.split(";", cont))
                    if conte[0] == ' ':
                        continue
                    print(conte)
                    with connection.cursor() as cursor:
                        cursor.execute(f"""INSERT INTO phonebook3(first_name,last_name, phone_number)
                        VALUES ('{conte[0]}','{conte[1]}','{conte[2]}')""")

        elif a == 8:
            limit = input("Enter the limit")
            offset = input("Enter the offset")
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM phonebook3 LIMIT '{int(limit)}' OFFSET '{int(offset)}'""")
                all = cursor.fetchall()
                for _, name, last_name, phone in all:
                    print("|" + name + " " + last_name + "---" + phone + "|")
    connection.close()


if __name__ == "__main__":
    main()