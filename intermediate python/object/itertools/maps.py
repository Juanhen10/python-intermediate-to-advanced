# map - para mapear dados
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

def aumentar_porcetagem(valor, porcetagem):
    return round(valor * porcetagem)

aumentar_dez_porcento = partial(
    aumentar_porcetagem,
    porcetagem=1.1
)

# novo_produtos = [
#     {**p, 
#      'preco': aumentar_dez_porcento(p['preco'])} 
#     for p in produtos
# ]
def muda_preco(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }
    
    
novo_produtos = map(
    muda_preco,
    produtos
)

print_inter(produtos)
print_inter(novo_produtos)