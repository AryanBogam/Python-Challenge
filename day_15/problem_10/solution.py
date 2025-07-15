def custom_exception():
    try:
        number = float(input("Enter a number: "))
        print(f"You entered: {number}")
    except ValueError:
        print("Error: Input must be a valid number!")

custom_exception()