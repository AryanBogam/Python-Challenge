items = [10, 20, 30]
try:
    idx = int(input("Enter index (0–2): "))
    print("Item:", items[idx])

# Handle both invalid index and invalid input
except (IndexError, ValueError):
    print("Index out of range or invalid input.")