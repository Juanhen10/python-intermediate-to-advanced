import os
os.system('cls')
# Metodos de Classe + factories(fabricas)
# São metodos onde "self" será "cls", ou seja,
# ao inves de receber a instancia no primeiro párametro, receberemos a propria classe
class Pessoa:
    ano = 2023
    
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade  
        
    @classmethod    
    def metodo_de_classe(cls):
        print('hey')
        
    @classmethod    
    def cria_com_50_ano(cls, nome):
        return cls(nome, 50)
        
    @classmethod    
    def cria_sem_nome(cls, idade):
        return cls('Anonima', idade)
        
        
        
        
p1 = Pessoa('João', 34)
p2 = Pessoa.cria_com_50_ano('Helna')
p3 = Pessoa.cria_sem_nome(20)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(Pessoa.ano)
Pessoa.metodo_de_classe()