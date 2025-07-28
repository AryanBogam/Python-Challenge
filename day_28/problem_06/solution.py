accounts = {"john": 1000, "mary": 500, "bob": 2000}

username = input("Enter username: ")
amount = float(input("Enter withdraw amount: "))

try:
    balance = accounts[username]
    
    if amount < 0:
        print("Cannot withdraw negative amount")
    elif amount > balance:
        print("Insufficient balance")
    else:
        new_balance = balance - amount
        accounts[username] = new_balance
        print(f"Withdrawal successful! New balance: {new_balance}")
        
except KeyError:
    print("Invalid user")
except ValueError:
    print("Enter valid amount")