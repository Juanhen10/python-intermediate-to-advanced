import os
os.system('cls')
# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta azul',
    'precp': 2.5,
    'categoria': 'Escritorio',
}




dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave, valor 
    in produto.items()
    if chave == 'categoria'
    
}


lista = [
    ('a','valor a'),
    ('b','valor a'),
    ('c','valor a'),
]

dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)