# os.walk
# os.walk é uma funçãoque permite percorrer uma estrutura de diretorios de  maneira recursiva
# Elas gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretorio atual (root), uma lista de subdiretótios (dirs) e uma lista dos arquivos do diretorio atual (files )
import os
from itertools import count

os.system('cls')

caminho = os.path.join('\\Users', 'Juan Henrique', 'Desktop', 'Nova Pasta')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(f'{the_counter}-Pasta atual:', root)

    for dir_ in dirs:
        print(f'  {the_counter}- Dir atual {dir_}')

    for file_ in files:
        # print(f'   {the_counter} - FILE: {file_}')
        caminho_completo_arquivo = os.path.join(root, file_)
        print(f'   {the_counter} - FILE: {caminho_completo_arquivo}')
        # APAGA ARQUIVOS ↓
        #               os.unlink(caminho_completo_arquivo)
