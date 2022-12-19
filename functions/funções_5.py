'''
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palvra global faz uma variável do escopo externo ser a mesmo no escopo interno
--------------------------------
Function scope in Python
Scope means where that code can reach.
There is global and local scope.
The global scope is the scope where all code is reachable.
The local scope is the scope where only names from the same locale can be reached.
We don't have access to inner scope names in outer scopes.
The global word makes a variable in the outer scope the same as in the inner scope.
🇧🇷
'''

x = 1

def escopo():
    global x
    x = 10 
    
    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x,y)
        
    outra_funcao()
    print(x)
    
escopo()