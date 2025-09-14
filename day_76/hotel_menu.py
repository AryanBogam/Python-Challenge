#Define the menu of restuarant
menu = {
    "pizza" : 40,
    "Pasta" : 50,
    "Burger" : 60,
    "Salad": 70,
    "Coffee": 80,
}

#Greet
print("\n")
print("Welcome to Python Restuart")
print("--------------------------")
print("Pizza: Rs40\nPasta: Rs60\nBurger: Rs60\nSalad: Rs70\nCoffe: Rs80")

order_total = 0

# Asking the first order.
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not avaiable yet!")

# Asking the second order.
another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" or "yes":
    item_2 = input("Enter the name of item you want to order = ")
    if item_2 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_1} is not avaiable yet!")