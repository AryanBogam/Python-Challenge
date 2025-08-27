menu = (("Burger", 10), ("Pizza", 15), ("Fries", 5), ("Coke", 3))
orders = []

while True:
    print("1. View menu")
    print("2. Place order")
    print("3. View bill")
    print("4. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        print("Menu:")
        for item, price in menu:
            print("-", item, "$" + str(price))
    
    elif choice == "2":
        item_name = input("Enter item name: ")
        found = False
        for item, price in menu:
            if item == item_name:
                orders.append((item, price))
                print("Item added to order!")
                found = True
                break
        if not found:
            print("Item not found!")
    
    elif choice == "3":
        print("Your order:")
        total = 0
        for item, price in orders:
            print("-", item, "$" + str(price))
            total = total + price
        print("Total: $" + str(total))
    
    elif choice == "4":
        break