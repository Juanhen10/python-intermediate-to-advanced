# Funções decoradoras e decoradores com classes
import os 
os.system('cls')

def adicona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} - {class_dict}'
        return class_repr
    cls.__repr__ = meu_repr
    return cls

    

class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} - {class_dict}'
        return class_repr



def meu_planeta(metodo):
    def interno(self,*args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if 'Terra' in resultado:
            return f'Você esta em casa ({self.nome})'

        
        return resultado
    
    return interno


@adicona_repr
class Time:
    def __init__(self,nome):
        self.nome = nome
    
    
@adicona_repr        
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def fala_nome(self):
        return f'O planeta é {self.nome}'
    
spfc = Time('São Paulo')
psg = Time('PSG')


terra = Planeta('Terra')
marte = Planeta('Marte')

print(spfc)
print(psg)


print(terra)
print(marte)

print(terra.fala_nome())
print(marte.fala_nome())