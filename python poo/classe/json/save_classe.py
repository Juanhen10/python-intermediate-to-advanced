import json
import os 
os.system('cls')
        
CAMINHO = 'car.json'


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
        print('-'*30)
        
        
    def not_sold(self):
        if not self.solding:
            print(f"{self.name} isn't was solding")
            print('-'*30)
        
            return
        
        print(f'CAR: {self.name} was solding...')
        self.solding = True
        print('-'*30)
        
    
        
   
        
car_1 = Car('Golf GTI', '1998', 'GOLF', 'MK4')


car_1.not_sold()

car_2 = Car('Civic', '1998', 'HONDA')
car_2.sold()

car_3 = Car('Lancer', '2020', 'Mitsubishi', 'Mitsubishi Lancer HL')
car_3.not_sold()

car_4 = Car('A4', '2021', 'AUDI', 'Prestige')
car_4.sold()


car_5 = Car('BMW M3', '2020', 'BMW', 'M4')
car_5.sold()

dados = [vars(car_1),vars(car_2),vars(car_3),vars(car_4),vars(car_5)]



def fazer_dump():
    with open(CAMINHO, 'w', encoding='utf8') as file:
        json.dump(dados, file, ensure_ascii=False, indent=2)
        
        
if __name__ == '__main__':
    print('#' * 40)
    fazer_dump()
          




