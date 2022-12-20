import os
os.system('cls')
# raise - lançando exceções (erros)
def erro_divide(d):
    if d == 0:
        raise ZeroDivisionError('Você esta tentando dividir por zero')
    return True 

def deve_ser_int_float(n):
    tipo_n - type(n)
    if not isinstance(n, (float,int)):
        raise TypeError(
            f'{n} deve ser int ou float'
            
            )
    return True


def divide(n,d):
    erro_divide(d)
    deve_ser_int_float(n)
    deve_ser_int_float(d)
    return n / d
   
print(divide(8, 0))