'''
Higher order Functions
Funções de primeira classe

Termos técnicos: Higher Order Functions e First-Class Functions
Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
-----------------------------------------------------------------
Higher orderFunctions
First class functions

Technical Terms: Higher Order Functions and First-Class Functions
Academically, the terms Higher Order Functions and First-Class Functions have different meanings.

Higher Order Functions - Functions that can receive and/or return other functions

First-Class Functions - Functions that are treated like other common data types (strings, integers, etc...)

It wouldn't make much difference to your code, but I think I should let you know.

Note: These terms may be different and still reflect the same meaning.
'''
import os
os.system('cls')



def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)



v = executa(saudacao,'bom dia','juan')
print(v)