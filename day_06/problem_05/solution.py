# Taking info.
entry = float(input("Entry price: "))
exit_price = float(input("Exit price: "))


# Condition to print.
if exit_price > entry:
    print("Profit")
elif exit_price < entry:
    print("Loss")
else:
    print("No profit, no loss")
