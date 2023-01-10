import os
os.system('cls')
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetps (instâncias) que  podem ter seus proprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados internos para reaçizar varias ações.
# Por convenção, usamos PescalCase para nome de classes.
# string = 'Juan' #str
# print(string.upper())
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('juan','Henrique')
# p1.nome = 'juan'
# p1.sobrenome = 'henrique'

p2 = Pessoa('Maria','Joana')
# p1.nome = 'Maria'
# p1.sobrenome = 'Joana'


print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)


