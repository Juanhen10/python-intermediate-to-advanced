import contas
import pessoa


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoa.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None
    ):

        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('checando a Agencia:', True)
            return True
        print('chegando a Agencia:', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('checando o Cliente:', True)
            return True
        print('checando o Cliente:', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('checando a Conta:', True)
            return True
        print('checando a Conta:', False)
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('checando Cliente e Conta:', True)
            return True
        print('checando Conta e Cliente:', False)
        return False

    def autenticar(self, cliente: pessoa.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}) - {self.clientes}, {self.contas}'
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    c1 = pessoa.Cliente('Juan', 18)
    cc = c1.conta = contas.ContaCorrente(111, 222, 0, 0)

    c2 = pessoa.Cliente('Victor', 15)
    cpp = c2.conta = contas.ContaPoupanca(111, 222, 0)
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([c1.conta, cpp])
    banco.agencias.extend([111, 222])

    print(banco.autenticar(c1, c2.conta))

    if banco.autenticar(c1, cc):
        cc.depositar(20)
        print(c1.conta)
