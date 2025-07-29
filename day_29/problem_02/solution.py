orders = [101, 102, 103, 102, 101, 104]

unique_orders = []
for order in orders:
    if order not in unique_orders:
        unique_orders.append(order)

print(unique_orders)