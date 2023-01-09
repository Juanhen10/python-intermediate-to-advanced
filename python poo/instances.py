import os 
os.system('cls')
# metodos em intancias de classes python
# Hard coded - Codigo ecrito diretamente
# Clases - Molde (geralmente sem dados ) 
# insta^ncia da class (objetos) - 
# Tem os dados Uma classe pode gerar varias instancias. 
# na Classe o self é a propria instancia
class Carro:
    def __init__(self, nome='no name car'):
        self.nome = nome
        
    def acelara(self):
        print(f'{self.nome} está acelerando... ')
        
        
celta = Carro('celta').acelara()
Carro.acelara()
fusca = Carro('fusca').acelara()
