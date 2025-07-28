inventory = {"apples": 10, "bananas": 0, "oranges": 5}

item = input("What item to buy? ")

try:
    quantity = inventory[item]
    if quantity == 0:
        print(f"{item} is out of stock!")
    else:
        print(f"{item} available: {quantity}")
except KeyError:
    print(f"{item} not found!")
    print("Available items:", list(inventory.keys()))