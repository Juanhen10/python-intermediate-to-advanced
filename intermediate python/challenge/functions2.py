'''
Exercícios
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro
'''
import os
os.system('cls')

def multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


    
duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)

