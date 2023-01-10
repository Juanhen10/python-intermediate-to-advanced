import os 
os.system('cls')
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
######################################################################
# Exercise - Merge lists
# Create a zipper function (like clothes zipper)
# The job of this function will be to join two
# lists in order.
# Use all values ​​from the smaller list.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Result
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


# def zipper(l1, l2):
#     mine = min(len(l1), len(l2))
#     return [ 
#       (l1[i],l2[i]) for i in range(mine)  
#     ]
        
    

    

# regiao = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# lugar =  ['BA', 'SP', 'MG', 'RJ']
# a = zipper(lugar, regiao)
# print(a)
from itertools import zip_longest


regiao = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lugar =  ['BA', 'SP', 'MG', 'RJ']
print(list(zip(regiao,lugar)))
print()
print(list(zip_longest(regiao,lugar)))

