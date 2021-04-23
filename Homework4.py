class BankAccount:
    Name = 100
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    @property
    def check(self):
     if self._balance <= 0:
         return "prover"
     return self._balance
    @property
    def nam(self):
        if self._name == "Akylbek":
            return 'Jalil'
        return 'Kiber ataka'

    def __setattr__(self, key, value):
        if key == "Name":
            raise ValueError
        else:
            self.__dict__[key] = value

account = BankAccount('Akylbek', 90)
account._balance = 9700000
account._name = "Akylbek"
# account.Name = 10
# Cчет пользователя {self._balance}
print(account.nam)
print(account.check,"$")
