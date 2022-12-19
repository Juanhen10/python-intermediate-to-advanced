'''
Manipulando chaves e valores em dicionarios
'''
import os
os.system('cls')

pessoa = {}
chave = 'nome'

pessoa[chave] = 'Juan'
pessoa['sobrenome'] = 'Henrique'

del pessoa['sobrenome']
print(pessoa[chave])
print(pessoa)

print( pessoa.get('sobrenome', None) )
