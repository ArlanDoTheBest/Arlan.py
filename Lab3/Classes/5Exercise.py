class BankAccount():
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
my_account = BankAccount(owner=str(input()), initial_balance=int(input()))
my_account.deposit(500)
my_account.deposit(200)
my_account.withdraw(300)
my_account.withdraw(1000) 
print(f"Balance for {my_account.owner}: {my_account.balance}")
