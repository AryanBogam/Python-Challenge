try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b

# Handle when user tries to divide by zero
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Handle when user enters invalid input
except ValueError:
    print("Please enter valid numbers.")
else:
    print("Result:", result)