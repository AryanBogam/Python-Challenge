def withdraw(balance, amount):
    if amount > balance:
        return "Insufficient balance"
    else:
        return balance - amount

print(withdraw(1000, 500))
print(withdraw(1000, 1500))