import os
os.system('cls')

from bank_account import Clinte, ContaCorrente,ContaPupanca, Banco
p1 = Clinte('Juan Henrique Correia Souza', 18)
c1 = ContaPupanca()
c1.Poupanca('nubank',123,15, p1.nome) 
c1.sacar(5)
print()
p2 = Clinte('victor',18)
c2 = ContaCorrente()
c2.Corrente('inter', '45645', 1000, p2.nome, 200)
c2.sacar(500)
print()

Banco(p1.nome,c1.agencia,c2.numero)