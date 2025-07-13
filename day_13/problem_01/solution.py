try:
    # Get age from user and converting to number
    age = int(input("Enter your age: "))
    
    # Checking if age is negative
    if age < 0:
        print("Age can't be negative!")
    else:
        # Age is good, show it back
        print(f"Your age is {age}")

# Handle when user enters invalid input
except ValueError:
    print("Please enter a valid age.")