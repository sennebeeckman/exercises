class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_numer = account_number
        self.__initial_balance = initial_balance

    def get_account_number(self):
        return self.__account_numer

    def get_balance(self):
        return self.__initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Cannot deposit zero or negative funds")
        else:
            self.__initial_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Cannot withdraw zero or negative funds")
        else:
            if (self.__initial_balance - amount) < 0:
                raise ValueError("Insufficient funds")
            else:
                self.__initial_balance -= amount