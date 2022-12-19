'''
Eswcopo de funções em Python
Eswcopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
Não temos acesso a nomes de escopos internos nos escopos externos.
A palvra global faz uma variável do escopo externo ser a mesmo no escopo interno
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