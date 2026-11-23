
class BankAccount:

    def __init__(self, balance):
        if balance < 0:
            self.__balance = 0
            print("Invalid initial balance! Balance set to 0.")
        else:
            self.__balance = balance

    # Deposit
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount!")
        else:
            self.__balance += amount
            print(f"Deposited: {amount}")

    # Withdraw
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    # Display balance
    def get_balance(self):
        print(f"Current Balance: {self.__balance}")


account1 = BankAccount(-15000)

account1.deposit(5000)
account1.withdraw(2000)
account1.get_balance()
