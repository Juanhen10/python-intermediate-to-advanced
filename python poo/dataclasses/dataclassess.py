
import os
from dataclasses import asdict, astuple, dataclass, field, fields

os.system('cls')
# Dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__, __eq__ (entre outros) em classes definidas pelo usuario
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do python
# doc: https://docs.python.org/3/libary/dataclasses.html


@dataclass(frozen=True, repr=True, order=True)
class Pessoa:
    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 0
    enderecos: list[str] = field(default_factory=list)

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completp = f'{self.nome} {self.sobrenome}'
    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = sobrenome


if __name__ == '__main__':
    p1 = Pessoa('juan', 'henrique')
    print(p1)
    # print(asdict(p1).keys())
    # print(asdict(p1).values())
    # print(asdict(p1).items())
    # print(astuple(p1)[0])
