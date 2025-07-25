class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError()

balance = 100
amount = int(input("How much to withdraw? "))

try:
    withdraw(balance, amount)
    print("Withdrawal success!")
except InsufficientFundsError:
    print("Not enough money!")