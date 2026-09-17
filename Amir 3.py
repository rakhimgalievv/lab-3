class ATMAccount:
    def __init__(self, balance, pin):
        self.__balance = balance
        self.__pin = pin

    def check_pin(self, pin):
        return self.__pin == pin

    def show_balance(self, pin):
        if self.check_pin(pin):
            print("Баланс:", self.__balance)
        else:
            print("Неверный PIN")

    def deposit(self, amount, pin):
        if self.check_pin(pin):
            self.__balance += amount
            print("Счёт пополнен на", amount)
        else:
            print("Неверный PIN")

    def withdraw(self, amount, pin):
        if self.check_pin(pin):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Снято:", amount)
            else:
                print("Недостаточно средств")
        else:
            print("Неверный PIN")


account = ATMAccount(20000, "1234")

account.show_balance("1234")

account.deposit(5000, "1234")

account.withdraw(3000, "1234")

account.show_balance("1234")
