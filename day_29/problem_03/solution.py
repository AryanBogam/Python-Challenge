items = [1, 2, 3, 4, 5]
k = 2

rotated = items[-k:] + items[:-k]

print(f"Original: {items}")
print(f"Rotated by {k}: {rotated}")