cart = ["Shoes", "Watch", "Shoes"]

if len(cart) != len(set(cart)):
    print("Duplicate found")
else:
    print("No duplicates")