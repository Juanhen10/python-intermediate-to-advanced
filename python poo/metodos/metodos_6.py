import os
os.system('cls')
# super() é a super classe na sub classe
# Classe principal (Pessoa)]
#      -> Super class, base class, parent class
# Classes filhas (Cliente)
#      -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno
    
# string= MinhaString('Juan')
# print(string.upper())


class A:
    atributo_a = 'A'
    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'B'
    def metodo(self):
        print('B')
        
class C(B):
    atributo_c = 'C'
    def metodo(self):
        super().metodo()
        print('C')
        
c = C()