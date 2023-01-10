import copy
import os
os.system('cls')

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Relogio  3', 'preco': 10.00},
    {'nome': 'controle 4', 'preco': 22.32},
    {'nome': 'Livros   2', 'preco': 10.11},
    {'nome': 'Celular  1', 'preco': 105.87},
    {'nome': 'teclado  5', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
novos_produtos = produtos.copy()
for p in produtos:
    print(f'os produtos: {p["nome"]}  -  R${p["preco"]}')
print('-----------------------------------------------')
print('os produtos acima tiveram alteração de 10% cada.')
print('-----------------------------------------------')

for i in novos_produtos:
    aumento = i['preco'] * 1.10
    print(f'os produtos: {i["nome"]} - R${aumento:.1f}')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produtos: produtos['nome'],
    reverse= True

)
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produtos: produtos['preco'],

)
print()
print(*produtos_ordenados_por_preco, sep='\n')
