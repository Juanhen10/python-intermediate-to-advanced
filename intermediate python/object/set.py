'''
Sets - conjunto em Python (tipo set)
Conjuntos são ensinados na matemática
representads graficamente pelo diagrama de Venn
Set em Pthon são mutáveis, po´rem aceitam apenas tipos imutáveis como valor interno

criando um set
set(interável) ou {1,2,3}

set são eficientes par remover valores duplicados da interáveis.
eles não tem índezes;
eles não garantem ordem;
eles são interáveis (for,in,not in)

Métodos úteis:
add, update, clear, discard

Operadores úteis:
união | união (union) - Une
intersecção & (interserction) - itens presentes em ambos
#diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estã o em ambos
------------------------------------------------------
Sets - set in Python (set type)
Sets are taught in mathematics
graphically represented by the Venn diagram
Set in Pthon are mutable, because they only accept immutable types as internal values

creating a set
set(interable) or {1,2,3}

set are efficient for removing duplicate values ​​from iterables.
they don't have indices;
they do not guarantee order;
they are iterable (for,in,not in)

Useful methods:
add, update, clear, discard

Useful operators:
union | union (union)
intersection & (interserction) - items present in both
#difference - Items present only in the left set
symmetric difference ^ - Items that are not in both
'''

import os
os.system('cls')

# s1 = set()
# s1 = {1,2,3,3,3,3,1}
# s1.add('luiz')
# s1.update(('olá mundo',1,2,3,4))
# # s1.clear()
# s1.discard('olá mundo')
# print(s1)

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2 # unir o sets
s3 = s1 & s2 # mostra os itens iguais
s3 = s1 - s2 # diferença dos itens em um dos set 
s3 = s2 - s1 
s3 = s2 ^ s1 #vai mostrar as diferenças dos dois


# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('digite: ')
    letras.add(letra.lower())
    
    if 'l' in letras:
        print('parabens')
        break
    print(letras)
    