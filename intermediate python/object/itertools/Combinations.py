import os
os.system('cls')
# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools  import combinations, permutations, product

def print_inter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm','g'],
    ['masc', 'fem'],
    ['algodão', 'poliéster'],
]

# print_inter(combinations(pessoas,2))
# print_inter(permutations(pessoas,2))
print_inter(product(*camisetas))


