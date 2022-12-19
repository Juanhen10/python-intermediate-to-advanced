"""
Escopo de funções em Python
Escopo significa o local onde aquele codigo pode atingit.
Existe o escpo global e local
O escopoglobal é o escopo onde todo o código é alcançavel.
O escpo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""
import os
os.system('cls')


x = 1

def escopo():
    x = 10
    def escopo2():
        y = 2
        print(x, y)
        
    escopo2()
    print(x)
    
escopo()

