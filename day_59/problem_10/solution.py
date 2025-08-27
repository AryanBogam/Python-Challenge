cart = []

while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        item = input("Enter item name: ")
        price = float(input("Enter item price: "))
        cart.append({"item": item, "price": price})
        print("Item added to cart!")
    
    elif choice == "2":
        item_name = input("Enter item to remove: ")
        for item in cart:
            if item["item"] == item_name:
                cart.remove(item)
                print("Item removed!")
                break
        else:
            print("Item not found!")
    
    elif choice == "3":
        print("Your cart:")
        for item in cart:
            print("-", item["item"], "$" + str(item["price"]))
    
    elif choice == "4":
        total_items = len(cart)
        total_price = 0
        for item in cart:
            total_price = total_price + item["price"]
        print("Checkout Summary:")
        print("Total items:", total_items)
        print("Total price: $" + str(total_price))
    
    elif choice == "5":
        break