'''
Closure e funções que retornam outras funções
'''
import os
os.system('cls')


def saudacao(msg):
    def saudar(nome):
        return f'{msg}, {nome}!'
    return saudar 

falar_bom_dia = saudacao('Bom dia')
falar_boa_noite = saudacao('boa noite')
for nome in ['Juan','Victor','Biel']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
    