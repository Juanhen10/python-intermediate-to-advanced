'''
Dicionarios em Python (tipo dict)
Dicionarios são estruturas de dados do tipo par de "chave" e "valor"
Chaves podem ser consideradas como o "indice"
que vimos na lista e pode ser tipos imutaveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionario
Usamos as chaves --{}-- ou a classe dict para criar dicionarios.
Imutavei: str, int, float, bool, tuple
Mutavel: dict, list
pessoa = {
    'nome': 'luiz otavio',
    'sobrenome':'Miranda',
    'idade':18
    'altura':1.8
    'endereços' [{'rua':'tal tal}]
}
'''
import os
os.system('cls')



pessoa = {
    'nome': 'Juan',
    'sobrenome': 'henrique',
    'idade': 20,
    'altura': 1.80
}
for chave in pessoa:
    print(chave, pessoa[chave])
    