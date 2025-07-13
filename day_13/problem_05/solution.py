num = input("Enter a number: ")

try:
    # Check if there's a decimal point in the input
    if '.' in num:
        # Try to convert to float
        float(num)
        print("You entered a float.")
    else:
        # Try to convert to integer
        int(num)
        print("You entered an integer.")

# Handle when user enters something that's not a number
except ValueError:
    print("Invalid number.")