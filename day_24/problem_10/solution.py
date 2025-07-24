menu_prices = {"Pizza": 200, "Burger": 150, "Pasta": 180, "Coke": 50}

orders = {
    "Table 1": [{"dish": "Pizza", "qty": 2}, {"dish": "Coke", "qty": 2}],
    "Table 2": [{"dish": "Burger", "qty": 3}, {"dish": "Pasta", "qty": 1}],
    "Table 3": [{"dish": "Pizza", "qty": 1}, {"dish": "Burger", "qty": 2}]
}

print("Total bill per table:")
for table, table_orders in orders.items():
    total = 0
    for order in table_orders:
        dish_total = menu_prices[order["dish"]] * order["qty"]
        total = total + dish_total
    print(f"{table}: {total}")

dish_count = {}
for table_orders in orders.values():
    for order in table_orders:
        dish = order["dish"]
        qty = order["qty"]
        if dish in dish_count:
            dish_count[dish] = dish_count[dish] + qty
        else:
            dish_count[dish] = qty

top_dish = ""
max_qty = 0
for dish, qty in dish_count.items():
    if qty > max_qty:
        max_qty = qty
        top_dish = dish

print(f"\nTop ordered dish: {top_dish} ({max_qty} total)")