
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Available Balance:", self.__balance)


account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)
account.show_balance()
