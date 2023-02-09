import os

import account
import people


os.system('cls')

"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""


# class Pessoa:
#     def __init__(self, nome: str, idade: int) -> None:
#         self.nome = nome
#         self.idade = idade

#     @property
#     def nome(self):
#         return self._nome

#     @nome.setter
#     def nome(self, nome: str):
#         self._nome = nome

#     @property
#     def idade(self):
#         return self._idade

#     @idade.setter
#     def idade(self, idade: int):
#         self._idade = idade

#     def __repr__(self):
#         class_name = type(self).__name__
#         attrs = f'({self.nome!r}, {self.idade!r})'
#         return f'{class_name}{attrs}'


# class Cliente(Pessoa):
#     def __init__(self, nome: str, idade: int) -> None:
#         super().__init__(nome, idade)
#         self.conta: Conta | None = None


class Bank():
    def __init__(self, client: list[people.People] | None = None, agencies: list[str] | None = None, accounts: list[account.Account] | None = None):
        self.client = client or []
        self.agencies = agencies or []
        self.accounts = accounts or []

        def check_agency(self, account):
            if account.agency in self.agencies:
