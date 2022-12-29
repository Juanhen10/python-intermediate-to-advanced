import os
os. system('cls')

def fabrica_de_funcoes(func):
    print('decoradora 1')
    
    def alinhada(*args, **kwargs):
        print('Alihada')
        res = func(*args, **kwargs)
        return res
    return alinhada


def fabrica_de_decoradores(a=None,b=None,c=None):
    return fabrica_de_funcoes





@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    return x + y

decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x,y: x * y)

s = soma(10,5)
m = multiplica(10,5)
print(s)
print(m)