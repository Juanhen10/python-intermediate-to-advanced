import sys
import os
os.system('cls')

# Generator expression, Interables e Interators em Python
interable = ['Eu', 'Tenho', '__iter__']
iterator = iter(interable) # tem __iter__ e __next__
lista = [(n for n in range(10))]
generator = (n for n in range(10))
print(lista)
print(generator)


print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


for n in generator:
    print(n) 