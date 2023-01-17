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
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor
         
             
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
        


motor = Motor('A8')
fabricante = Fabricante('Audi')
 
car = Carro('A4')
fabricante.fabr_m(motor)


