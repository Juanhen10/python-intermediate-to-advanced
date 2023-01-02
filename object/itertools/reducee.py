# reduce - faz a redução de um iteravel em um valor
import os
from functools import reduce
os.system('cls')
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# def funcao_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('prduto', produto)
#     print()
#     return acumulador + produto['preco']



total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('total', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)
