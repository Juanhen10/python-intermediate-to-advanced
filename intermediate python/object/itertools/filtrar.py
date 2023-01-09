# filter - é um filtro funcional
import os 
os.system('cls')
from functools import partial



def print_inter(iterator):
    print(*list(iterator), sep = '\n')
    print()
    
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def filtrar_preco(produto):
    return produto['preco'] > 100


# novo_produtos = [
#     p for p in produtos
#     if p['preco'] > 0
# ]
novo_produtos = filter(
    # lambda p: p['preco'] > 100,
    filtrar_preco,
    produtos
)

print_inter(produtos)
print_inter(novo_produtos)