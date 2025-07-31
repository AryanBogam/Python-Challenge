orders = [("Pizza", 2, 1), ("Burger", 1, 2), ("Pizza", 1, 1), ("Fries", 3, 2), ("Pizza", 2, 3)]

table_orders = {}
item_count = {}

for item, quantity, table_no in orders:
    if table_no not in table_orders:
        table_orders[table_no] = []
    table_orders[table_no].append((item, quantity))
    
    if item not in item_count:
        item_count[item] = 0
    item_count[item] += quantity

print("ORDER SUMMARY BY TABLE:")
print("-" * 30)
for table, table_items in table_orders.items():
    print(f"Table {table}:")
    total_items = 0
    for item, qty in table_items:
        print(f"  {item} x {qty}")
        total_items += qty
    print(f"  Total items: {total_items}")
    print()

most_popular = max(item_count, key=item_count.get)
print(f"Most popular item: {most_popular} ({item_count[most_popular]} orders)")