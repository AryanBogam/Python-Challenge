inventory = [("Pen", 10), ("Pencil", 20), ("Notebook", 5)]

product = input("Which product do you want to buy? ")

found = False
for item_name, quantity in inventory:
    if item_name.lower() == product.lower():
        print(f"{item_name}: {quantity} left")
        found = True
        break

if not found:
    print("Item not found.")