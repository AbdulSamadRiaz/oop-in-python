class Payment:
    def __init__(self, amount):
        self.amount = amount


class CreditCard(Payment):

    def payment(self):
        print(f"Credit Card: Payment of {self.amount} completed.")


class JazzCash(Payment):

    def payment(self):
        print(f"JazzCash: Payment of {self.amount} completed.")


class BankTransfer(Payment):

    def payment(self):
        print(f"Bank Transfer: Payment of {self.amount} completed.")


card = CreditCard(12000)
jazzcash = JazzCash(2000)
bank = BankTransfer(10000)

card.payment()
jazzcash.payment()
bank.payment()