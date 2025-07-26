items = []

while True:
    item = input("Enter product name: ")
    if item.lower() == "done":
        break
    items.append(item)

# Printing in reverse order
items.reverse()
print("Items in reverse:")
for item in items:
    print(item)