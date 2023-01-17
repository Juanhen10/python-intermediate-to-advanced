import os
os.system('cls')
# Encapsulamento (modificadores de acesso: public, protect private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#     (sem underline) = public
#               pode er usado em qualquer lugar
# _ (um underline) = protected 
#               não DEVE ser usado fora da classe
#               ou suas subclasses.
#__  (dois underlines) = private 
#     "name mangling" (desfiguração de nomes) em Python
#      só DEVE ser usado na classe em que foi declarado. 
#
class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protect = 'isso é protegida'
        self.__private = 'isso é privado' 
    
    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return 'metodo_protected'
        
f = Foo()
print(f.public)
print(f.metodo_publico())
print()
