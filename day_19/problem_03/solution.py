inventory = ["headphones", "charger", "phone case", "laptop"]

search = input("Search for a product: ").lower()

if search in inventory:
    print("Product is available.")
else:
    print("Not in stock.")
