class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Счёт пополнен на", amount)

    def show_balance(self):
        print("Владелец:", self.owner)
        print("Баланс:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Снято:", amount)
        else:
            print("Недостаточно средств")


account = BankAccount("Самандар", 10000)

account.show_balance()

account.deposit(5000)
account.show_balance()

account.withdraw(3000)
account.show_balance()
