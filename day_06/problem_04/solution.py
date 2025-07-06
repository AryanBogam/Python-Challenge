# Taking info.
income = float(input("Monthly income: "))
expenses = float(input("Monthly expenses: "))


# Conditions to print.
if expenses > income:
    print("You're burning cash!")
elif expenses == income:
    print("You're just breaking even")
else:
    print("Healthy runway")
