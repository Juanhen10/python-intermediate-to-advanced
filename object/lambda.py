'''
Função lambda em Python
A função lambda é uam função como qualquer outra em Python. 
porém, são funções anônimas que contém apenas uma linha. 
Ou seja, tudo deve ser contido dentro de uma expressão.
lista = [
    {'nome': 'Luiz','sobrenome':'miranda'},
    {'nome': 'Juan','sobrenome':'henrique'},
    {'nome': 'Victor','sobrenome':'Hugo'},
    {'nome': 'Maria','sobrenome':'Oliveira'},
    {'nome': 'Aline','sobrenome':'Souza'},
]
lambda function in python
The lambda function is a function like any other in Python.
however, they are anonymous functions that contain only one line.
That is, everything must be contained within an expression.
list = [
    {'name': 'Luiz','last name':'miranda'},
    {'firstname': 'Juan','lastname':'henrique'},
    {'firstname': 'Victor','lastname':'Hugo'},
    {'name': 'Maria','last name':'Oliveira'},
    {'name': 'Aline','last name':'Souza'},
'''
import os
os.system('cls')

# lista = [4,32,1,33,5]
# lista.sort()
# lista.sort(reverse=True)
#sorted(lista)

lista = [
    {'nome': 'Luiz','sobrenome':'miranda'},
    {'nome': 'Juan','sobrenome':'henrique'},
    {'nome': 'Victor','sobrenome':'Hugo'},
    {'nome': 'Maria','sobrenome':'Oliveira'},
    {'nome': 'Aline','sobrenome':'Souza'},
]
def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 =sorted(lista,key=lambda item: item['nome'])
l2 =sorted(lista,key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)


##################################################################
'''
funções lambda complexas

'''
def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n*m,
    2
)
print(duplica(2))

print(
    executa(
        lambda x,y: x + y,
        2,3
    ),
    executa(soma,2,3),
    soma(2,3)
)

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5,6,7
    )
)