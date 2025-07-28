menu = {"pizza": 250, "burger": 150, "fries": 80}

total_bill = 0

for i in range(3):
    print(f"Order {i + 1}:")
    try:
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        
        price = menu[item]
        cost = price * quantity
        total_bill += cost
        print(f"{item} x {quantity} = {cost}")
        
    except KeyError:
        print("Item not in menu!")
        print("Available items:", list(menu.keys()))
    except ValueError:
        print("Enter valid quantity!")

print(f"Total bill: {total_bill}")