import os
os.system('cls')

class Pessoa:
    ano_atual = 2023
    
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
 
 
dados = {'nome': 'joao', 'idade': 35}    
p1 = Pessoa(**dados)

# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.get_ano_nascimento())
# print(p1.__dict__)
# print(p1.outra)
# print(vars(p1))
print(vars(p1))