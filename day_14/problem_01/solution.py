try:
    age = int(input("Enter your age: "))
    if age <= 0 or age > 120:
        print("Age must be between 1 and 120.")
    else:
        print(f"Valid age entered: {age}")
except ValueError:
    # Catches if the input is not a valid integer
    print("Please enter a valid number for age.")
