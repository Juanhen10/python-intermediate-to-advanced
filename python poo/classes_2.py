import os 
os.system('cls')


class Animal:
    def __init__(self, nome):
        self.nome = nome
        
        variavel = 'valor'
        print(variavel)
        
    def comendo(self, alimento):
        return (f'{self.nome} está comendo {alimento}')

    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
    
leao = Animal('leão')
print(leao.nome)
print(leao.comendo('comida'))
print(leao.executar('maça'))