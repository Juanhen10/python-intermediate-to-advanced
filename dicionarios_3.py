'''
Metodos úteis dos dicionarios em python
len -quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iteravel com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaaga um item com a chave especificada (del)
popitem - Apaga o último item adiconado
update - Atualiza um dicionário com outro
'''
import os
os.system('cls')

pessoa = {
    'nome': 'juan',
    'sobrenome': 2,
    #'idade': 19,
} 

#print(len(pessoa))
#############################################################
#print(list(pessoa.key()))
# for chave in pessoa.keys():
#     print(chave)
#############################################################
# print(list(pessoa.values()))
# for valor in pessoa.values():
#     print(valor)
#############################################################
# print(list(pessoa.items()))
# for chave, valor in pessoa.items():
#     print(chave, valor)
#############################################################
# pessoa.setdefault('idade', None)
# print(pessoa['idade'])
#############################################################
# import copy
# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
#     #'idade': 19,
# } 

# d2 = copy.deepcopy(d1)
# d2['c1'] = 1000
# d2['l1'][1] = 1000
# print(d1)
# print(d2)
##########################################################
p1 = {
    'nome': 'juan',
    'sobrenome':'henrique',
}
# print(p1.get('nome '))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
############################################################
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
#############################################################
# p1.update({
#     'nome':'novo valor',
#     'idade': 20,
# })
# print(p1)
# p1.update(nome='novo valor',idade = 30)
# print(p1)
tupla = ('nome','novo_valor'),
p1.update(tupla)
print(p1)