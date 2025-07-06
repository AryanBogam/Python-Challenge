# Taking input of user portfolio.
portfolio = float(input("Enter your crypto portfolio size in ₹: "))

# Condition to print.
if portfolio > 1000000:
    print("Whale")
elif portfolio >= 100000:
    print("Mid-level")
else:
    print("Shrimp")
