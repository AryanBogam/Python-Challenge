cart = [["Milk", 2, 30], ["Bread", 1, 40], ["Eggs", 12, 5]]

total_bill = 0
print("Shopping Cart:")
print("-" * 30)

for item_name, quantity, price_per_unit in cart:
    item_total = quantity * price_per_unit
    total_bill += item_total
    print(f"{item_name}: {quantity} x {price_per_unit} = {item_total}")

print("-" * 30)
print(f"Total Bill: {total_bill}")