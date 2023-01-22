import os 
os.system('cls')
# herança simples - Relações entre classes
# associação - usa, agregação - tem compisição - É dono de, Herença - É um
#
# Herança ou composição
#
# Classe pricipal (Pessoa)
# ->super class, base class, parent class
# Classes filhas (clientes)
# -> sub class, chilf class, derived class
# object
class Pessoa:
    cpf = '1234'
    
    
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome,self.__class__.__name__)
        
class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('teste')
        print(self.nome, self.sobrenome,self.__class__.__name__)
    
class Aluno(Pessoa):
    ...
    


c1 = Cliente('Juan', 'henrique')
c1.falar_nome_classe()
a1 = Aluno('Maria','Helena')
a1.falar_nome_classe()