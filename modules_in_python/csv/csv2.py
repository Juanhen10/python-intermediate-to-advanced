# csv.reader e csv.DictReader
# csv.reader lê o cvs em formato de lista
# csv.DictReader lê o CSV em formato de dicionario
import csv
import os
from pathlib import Path

os.system('cls')


CAMINGO_CSV = Path(__file__).parent / 'csv2.csv'

with open(CAMINGO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha)


# with open(CAMINGO_CSV, 'r', encoding='utf8') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)
