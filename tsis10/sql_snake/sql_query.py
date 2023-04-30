sql_insert = """INSERT INTO score(nickname, score, x, y) VALUES(%s, %s, %s, %s)"""
sql_update = """UPDATE score SET score = %s, x = %s, y = %s WHERE nickname = %s"""
sql_check_of_exist = """SELECT COUNT(*) FROM score WHERE nickname = %s"""
sql_clear = """DELETE FROM score WHERE nickname = %s"""