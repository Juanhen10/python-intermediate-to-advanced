'''
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel

crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
'''

import os 
os.system('cls')

def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total
    
mult1 = mult(1,5) 
mult2 = mult(5,6)
print(mult1)
print(mult2)

def im_par(*args):
    for num in args:
        if num % 2 == 0:
            return print('esse número é par')
        return print('esse número é impar')
        
num1 = im_par(2)
num = im_par(3)