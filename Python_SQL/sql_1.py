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
