import os
os.system('cls')
# Valores truthy e Falsy, tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imútaveis () "" 0 0.0 None False range(0,10)
#QUALQUER VALOR VAZIO é FALSY!!!
lista = [1]
dicionario = {2}
conjunto = set()
tupla = ()
string = ''
int = 0
float = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{int=}', falsy(int))
print(f'{float=}', falsy(float))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo}', falsy(intervalo))

