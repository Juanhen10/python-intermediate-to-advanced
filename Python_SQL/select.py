# import sqlite3

# from sql_1 import DB_FILE, TABLE_NAME

# connection = sqlite3.connect(DB_FILE)
# cursor = connection.cursor()

# cursor.execute(f'SELECT * FROM {TABLE_NAME}')

# row = cursor.fetchall()
# print(row)

# print()
# cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = "3"')
# row = cursor.fetchone()
# print(row)

# # if __name__ == '__main__':
# #     for row in cursor.fetchall():
# #         _id, name, weight = row
# #         print(_id, name, weight)

# cursor.close()
# connection.close()
