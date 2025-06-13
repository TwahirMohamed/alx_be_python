class BankAccount:
    ''' Encapsulates Banking Operations'''
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance

    def deposit(self, amount):
        ''' Method to handle deposit'''
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Amount deposited must be positive.")
    def withdraw(self, amount):
        ''' Method to handle withdrawal'''
        if amount > self.__account_balance:
            return False
        elif amount <= 0:
            return False
        else:
            self.__account_balance -= amount
            return True
    def display_balance(self):
        ''' Method to display the account balance '''
        print(f"Current Balance: ${self.__account_balance}")