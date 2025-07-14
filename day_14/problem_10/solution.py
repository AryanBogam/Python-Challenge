try:
    balance = float(input("Enter current balance: "))
    spend = float(input("Enter amount to spend: "))

    # Validate both values are positive
    if balance < 0 or spend < 0:
        raise ValueError("Values must be positive.")

    if spend > balance:
        raise ValueError("Insufficient funds!")

    print("Transaction successful. Remaining balance:", balance - spend)

except ValueError as e:
    print("Transaction Error:", e)
