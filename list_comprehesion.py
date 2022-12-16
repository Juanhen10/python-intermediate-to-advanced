import os
os.system('cls')
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)
# list comprehension em Python
# List comprehension é uma forma rápida para criar listas a partir de interáveis
# print(list(range(10)))
lista = []
for num in range(10):
    lista.append(num)
    
# print(lista)

lista = [
    num * 2 
    for num in range(10)]
# print(lista)

#Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produtos, 'preco': produtos['preco']* 1.05}
    if produtos['preco'] > 20 else {**produtos}
    for produtos in produtos
]
# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)
# lista = [n for n in range(10) if n < 5]


#filter 
novos_produtos = [
    {**produtos, 'preco': produtos['preco']* 1.05}
    if produtos['preco'] > 20 else {**produtos}
    for produtos in produtos
    if produtos['preco'] > 10
]
# p(novos_produtos)

#for in for 
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
        
lista = [
    (x,y )
    for x in range(3)
    for y in range(3)
    
]
p(lista)