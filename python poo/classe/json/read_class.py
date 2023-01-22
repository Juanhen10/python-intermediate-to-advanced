import os
os.system('cls')

from save_classe import CAMINHO, Car, fazer_dump
import json


fazer_dump() 

with open(CAMINHO,'r', encoding='utf8') as file:
    dados = json.load(file)
    carro1 = Car(**dados[0])
    print('-'*20)
    print(carro1.name, carro1.car_brand)
   
        
        
