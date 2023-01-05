# Problema dos parâmetros  mutaveis em funções Python
import os 
os.system('cls')
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista



cliente1 = adiciona_clientes('juan')
adiciona_clientes('joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1)

cliente2 = adiciona_clientes('helena')
adiciona_clientes('Maria', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Pedro')
adiciona_clientes('Leo', cliente3)
print(cliente3)
