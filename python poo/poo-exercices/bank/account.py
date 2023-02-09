from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency, account, balance):
        self.agency = agency
        self.account = account
        self.balance = balance

    @abstractmethod
    def withdraw(self, value): ...

    def to_deposit(self, value):
        self.balance += value
        self.detail(f'(deposit) value: ${value}')

    def detail(self, msg=''):
        print(f'your balance is R${self.balance:.2f} {msg}')
        print()

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r} - {self.account!r} - {self.balance!r})'
        return f'{class_name}{attrs}'


class accountPupanca(Account):
    def withdraw(self, value):
        value_saque = self.balance - value

        if value_saque > 0:
            self.balance -= value
            self.detail(f'(WITHDRAW) R${value} ')
            return self.balance

        print('it was not possibel to withdraw the money')
        self.detail(f'withdrawal danied R${value}')


class accountCorrente(Account):
    def __init__(self, agency: int, account: int, balance: float = 0, limite: float = 0):
        super().__init__(agency, account, balance)
        self.limite = limite

    def withdraw(self, value: float) -> float:
        value_pos_saque = self.balance - value
        limite_maximo = -self.limite

        if value_pos_saque >= limite_maximo:
            self.balance -= value
            self.detail(f'(WITHDRAW) R${value}')
            self.detail(f'Your limit is: {limite_maximo}')
            return self.balance

        print(' it is was not withdraw the value')
        self.detail(f'(withdraw danied R${value})')
        return self.balance

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r} - {self.account!r} - {self.balance!r} - {self.limite!r})'
        return f'{class_name}{attrs}'

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency!r} - {self.account!r} - {self.balance!r} - {self.limite!r})'
        return f'{class_name}{attrs}'
