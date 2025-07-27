def calculate_tip(bill_amount, tip_percent):
    return bill_amount * tip_percent / 100

try:
    bill = float(input("Enter bill amount: "))
    tip = float(input("Enter tip percent: "))
    result = calculate_tip(bill, tip)
    print(f"Tip amount: {result}")
except ValueError:
    print("Please enter valid numbers!")