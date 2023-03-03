import os
import sys

os.system('cls')

# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code


argumentos = sys.argv
qtd_Argumentos = len(argumentos)

if qtd_Argumentos <= 1:
    print('Você não passou argumentos')
else:
    print(f'Você passou os argumentos {argumentos[1:]}')
