'''
args - argumentos não nomeados 
* - *args Eempacotamento e desempacotamento)

 Lembre-te de desempacotamento
'''
import os
os.system('cls')


# x, y, *resto = 1,2,3,4
# print(x,y,resto)

def soma(*args):
    #args = list(args)
    total = 0
    for numero in args:
        total += numero
    return total
    
    
soma1 = soma(1,2,3)
print(soma1)    

soma2 = soma(4,5,6)
print(soma2)
