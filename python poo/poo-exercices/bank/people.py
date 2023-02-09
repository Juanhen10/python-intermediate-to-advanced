import account


class People():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        # if age < 18:
        #     print('You cannot creat an account')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}{attrs}'


class Client(People):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: account.Account | None = None


if __name__ == '__main__':

    c1 = Client('Juan', 15)
    c1.account = account.ContaCorrente(111, 222, 0, 12)

    c2 = Client('Juan', 15)
    c2.account = account.ContaPupanca(12, 12, 12)

    print(c1)
    print(c1.account)

    print(c2)
    print(c2.account)
