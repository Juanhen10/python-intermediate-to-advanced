import os 
os.system('cls')
# __new__ e __init__ em classes Python
# __new__ é o método responsavel por criar e retornar o novo onjeto.
# Por isso, new recebe cls.
# __new__ DEVE retornar o novo objeto
# __init__ é o método responsavel por inicializar a instância. Por isso, init recebe self.
# __init__ Não dever retornar nada (NOne)
# object é super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        print('Antes de criar a inst')
        instancia = super().__new__(cls)
        print('Depois da inst')
        instancia.x = 213
        return instancia
    
    def __init__(self, x):
        self.x = x
        print('Sou init')

    def __repr__(self):
        return 'A()'
    

# a = object.__new__(A)
# a.__init__()
# print(a)

a = A(123)
print(a.x)