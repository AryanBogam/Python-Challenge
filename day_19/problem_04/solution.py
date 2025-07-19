def cart_total():
    headphone_qty = int(input("Headphones qty: "))
    charger_qty = int(input("Charger qty: "))
    case_qty = int(input("Phone case qty: "))

    total = (headphone_qty * 999) + (charger_qty * 499) + (case_qty * 299)
    return total

print(f"Total Cart Value: ₹{cart_total()}")