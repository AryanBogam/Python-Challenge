def apply_discount(price, code):
    original_price = price
    discount_applied = 0
    
    if code == "SAVE10":
        discount_applied = price * 0.10
        final_price = price - discount_applied
        return final_price, f"10% off applied: ₹{discount_applied:.2f}"
    
    elif code == "FREESHIP":
        discount_applied = 50
        final_price = max(0, price - discount_applied)
        return final_price, f"Flat ₹50 off applied"
    
    elif code == "NEWUSER":
        discount_applied = price * 0.15
        if discount_applied > 100:
            discount_applied = 100
        final_price = price - discount_applied
        return final_price, f"15% off (max ₹100) applied: ₹{discount_applied:.2f}"
    
    else:
        return price, "Invalid discount code"

test_cases = [(500, "SAVE10"), (200, "FREESHIP"), (1000, "NEWUSER"), (300, "INVALID")]

print("DISCOUNT ENGINE TEST")
print("-" * 40)

for price, code in test_cases:
    final_price, message = apply_discount(price, code)
    print(f"Price: ₹{price}, Code: {code}")
    print(f"Final Price: ₹{final_price:.2f}")
    print(f"Details: {message}")
    print()