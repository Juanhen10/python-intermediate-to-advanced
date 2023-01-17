import os
os.system('cls')
# Exercicio com Classes
# 1 - Crie uma classe Carro (NOME)
# 2 - Crie uma classe Motor (NOME)
# 3 - Crie uma classe Fabricante (NOME)
# 4 - Faça a ligação entre Carro e Fabricante
# Obs.: Um fabricante pode fabricar varios carros
# Exiba o nome do carro, motor e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
         
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        
   
             
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
        


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1
print(f'{fusca.nome} - {fusca.fabricante.nome} - {fusca.motor.nome}')


a4 = Carro('A4')
audi = Fabricante('AUDI')
motor_2 = Motor('2.0')
a4.fabricante = audi
a4.motor = motor_2


print(f'{a4.nome} - {a4.fabricante.nome} - {a4.motor.nome}')
