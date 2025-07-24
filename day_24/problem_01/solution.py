products = [
    {"name": "Laptop", "qty": 5, "price": 50000},
    {"name": "Mouse", "qty": 0, "price": 500},
    {"name": "Keyboard", "qty": 10, "price": 1500},
    {"name": "Monitor", "qty": 0, "price": 15000},
    {"name": "Phone", "qty": 8, "price": 25000}
]

total_value = 0
for product in products:
    stock_value = product["qty"] * product["price"]
    total_value = total_value + stock_value

print("Total Stock Value:", total_value)

print("Out-of-stock items:")
for product in products:
    if product["qty"] == 0:
        print(product["name"])