def main():
    # Menu with items and prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    
    total = 0.0
    
    print("Welcome to Felipe's Taqueria!")
    
    try:
        while True:
            # Get item from user
            item = input("Item: ").title()
            
            # Check if item is on the menu
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
            
    except EOFError:
        print()  # Print newline before exiting


if __name__ == "__main__":
    main()