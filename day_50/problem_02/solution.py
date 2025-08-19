visitors = ["Alice", "Bob", "Alice", "Eve"]

unique_visitors = []
for visitor in visitors:
    if visitor not in unique_visitors:
        unique_visitors.append(visitor)

unique_count = len(unique_visitors)
print(unique_count)