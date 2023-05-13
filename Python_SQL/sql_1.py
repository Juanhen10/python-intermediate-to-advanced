import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: Fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

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
# Cuidado: sqç injection
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
print(sql)


cursor.close()
connection.close()
