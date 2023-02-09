import os 
os.system('cls')
# abstractmethod para qualquer método já decorado
# É possivel criar @property @property.setter @classmethod 
# @staticmethod e métodos normais como abstratos, para isso use @abstractmetrodo como decorator mais interno
# Foo - Bar são palavras usasdsas como placeholder
# para palvras que podem mudar na programção.
from abc import ABC, abstractmethod

class AbstractFOO(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name):...
    
class Foo(AbstractFOO):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')
        
    # @AbstractFOO.name.setter
    def name(self, name):
        self._name = name
    

foo = Foo('Bar')
print(foo.name)