import os 
os.system('cls')
# Classe decoradora (Decorator Classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
        
        
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado *self._multiplicador
        return interna
        

@Multiplicar(1)
def soma(x, y):
    return x + y

soma = soma(2,4)
print(soma)