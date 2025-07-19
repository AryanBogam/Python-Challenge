total = float(input("Enter cart total: ₹"))
coupon = input("Enter coupon code: ")

if total > 1000 and coupon == "SAVE10":
    total *= 0.9
    print(f"Coupon applied! New total: ₹{total:.2f}")
else:
    print(f"No discount applied. Total: ₹{total:.2f}")