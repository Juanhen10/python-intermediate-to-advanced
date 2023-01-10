import json
import os 
os.system('cls')


class Car:
    def __init__(self, name='', year=0 ,car_brand='no brand', type='no type', solding = False):
        self.name = name
        self.year = year
        self.car_brand = car_brand
        self.type = type
        self.solding = solding
        
        
        print( f'CAR: {name} \nBRAND: {car_brand}\nYEAR: {year}\nTYPE: {type} ')
        print()
        
    def sold(self):
        if self.solding:
            print(f'CAR:{self.name} was solding!!')
        print(f'CAR:{self.name} was sold!!!!')
        self.solding = True
        
        
    def not_sold(self):
        if not self.solding:
            print(f"{self.name} isn't was solding")
            return
        
        print(f'CAR: {self.name} was solding...')
        self.solding = True
        
    
        
   
        
        
CAMINHO = 'car.json'
car_1 = Car('Golf GTI', '1998', 'GOLF', 'MK4')




car_2 = Car('Civic', '1998', 'HONDA')
car_3 = Car('Lancer', '2020', 'Mitsubishi', 'Mitsubishi Lancer HL')
car_4 = Car('A4', '2021', 'AUDI', 'Prestige')
car_4 = Car('BMW M3', '2020', 'BMW', 'M4')



car_1.not_sold()
car_1.sold()
car_1.not_sold()


