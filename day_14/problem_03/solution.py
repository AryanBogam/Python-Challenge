while True:
    try:
        value = float(input("Enter a float number: "))
        print(f"You entered a float: {value}")
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a float.")
