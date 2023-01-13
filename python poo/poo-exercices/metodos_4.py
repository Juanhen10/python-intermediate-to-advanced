import os 
os.system('cls')
# @propety - um getter no modo Pythônico 
# Getter - um metodo para obter um atributo no modo Pythonico - modo do Python fazer as coisas
# @propery é uma propriedade do objeto, ela é um metodo que se comport acomo atributo
# geralmente é usada nas seh=guintes situações:
#   - como getter
#   - p/ evitar quebra de código cliente
#   - p/ habilitar setter
#   - p/ executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        # private - protecte - public
        self.cor_tinta = cor
        
    @property
    def cor(self):
        print('PROPERTY: ')
        return self.cor_tinta
    
    @property
    def marca(self):
        return f'{self.cor_tinta} - bic'


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.marca)






# class Caneta:
#     def __init__(self, cor):
#         # private - protecte - public
#         self.cor = cor
        
#     def get_cor(self):
#         print('GET COR')
#         return self.cor
    

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

