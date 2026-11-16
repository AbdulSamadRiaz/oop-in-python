
class Bank_account:

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid deposit amount!")

        else:
            self.balance = self.balance + amount
            print("Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid withdrawal amount!")

        elif amount > self.balance:
            print("Insufficient balance!")

        else:
            self.balance = self.balance - amount
            print("Remaining balance:", self.balance)

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_no)
        print("Current Balance:", self.balance)


account1 = Bank_account("Abdul Samad Riaz", "12345", 10000)

account1.display_balance()
account1.deposit()
account1.withdraw()
account1.display_balance()
