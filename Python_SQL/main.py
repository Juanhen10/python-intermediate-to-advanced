'''
import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read  Update Delete
# SQL -  INSERT SELECT UPDATE DELETE

# CUIDADO: Fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name = "{TABLE_NAME}"'
)
connection.commit()


# SQL - cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores mas colunas da tabela
# Cuidado: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight)'
    'VALUES'
    '(:name, :weight)'

)
# cursor.execute(sql, ['juan', 4])
# cursor.executemany(
#     sql,
#     (
#         ('juan', 4), ('Suzana', 5)
#     )
#     )

cursor.execute(sql, {'name': 'juan', 'weight': 4})
cursor.executemany(sql, (
    {'name': 'juan', 'weight': 4},
    {'name': 'victor', 'weight': 64},
    {'name': 'Isa', 'weight': 14},
    {'name': 'Caio', 'weight': 24},
)
)
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    connection.commit()

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "1"'
    )
    connection.commit()

    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER", weight=67.89 '
        'WHERE id = "2"'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
'''
import os

import dotenv
# PyMySQL - um cliente MySQL feito em Python puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: htpps://github.com/PyMySQL
import pymysql
import pymysql.cursors

os.system('cls')
TABLE_NAME = 'custormer'

dotenv.load_dotenv()

connection = pymysql.Connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=pymysql.cursors.SSDictCursor,
    # cursorclass=pymysql.cursors.DictCursor,
)

########################################################################
#                     ### CRIANDO VALORES ###                     C    #
########################################################################
with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # TRUNCATE: LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
########################################################################
#       Inserindo um valor usando placeholder e um iterável #
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('juan', 23)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()
#####################################################################
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = (
            {"name": "Victor", "age": 27, }
        )
        result = cursor.execute(sql, data2)
        # print(sql, data)
        # print(result)
    connection.commit()
#####################################################################
#   Inserindo varios valores usando placeholder e uma tupla de dicionarios #
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Leandri", "age": 28, },
            {"name": "Julia", "age": 26, },
            {"name": "Alisson", "age": 13, },
        )
        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()
#########################################################################    #
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s)'
        )
        data4 = (
            ("Sulivan", 60, ),
            ("Kovalsk", 50, ),
        )
        result = cursor.executemany(sql, data4)
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()
########################################################################
#                   ### LENDO VALORES COM SELECT ###               R    #
########################################################################
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id: '))
        # maior_id = int(input('Digite o maior id: '))
        menor_id = 1
        maior_id = 2
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))

        # data5 = cursor.fetchall()
        # for row in data5:
        #     print(row)
########################################################################
#                        ### UPDATE ###                           U    #
########################################################################
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name=%s, age=%s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('paulin', 15, 4))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # data6 = cursor.fetchall_unbuffered()

        for row in cursor.fetchall_unbuffered():
            print(
                f'\033[32mid:{row["id"]}\033[m - \033[31mName: {row["name"]} \033[m- \033[35mAge:{row["age"]}\033[m]')
            if row['id'] >= 5:
                break
        print()
        # cursor.scroll(1, 'absolute')
        for row in cursor.fetchall_unbuffered():
            print(row)

        # for row in cursor.fetchall():
        #     _id, name, age = row
        #     print(_id, name, age)
#######################################################################
#                        ### DELETANDO ###                           D #
########################################################################
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )

        cursor.execute(sql, (2))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        # print(row)
