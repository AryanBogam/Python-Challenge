# Perform (a / b) / c and handle all errors with proper messages
try:
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))
    c = float(input("Enter number c: "))
    result = (a / b) / c  # Perform nested division
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid numeric inputs.")
else:
    print("Result is:", result)
finally:
    print("Thanks for using this calculator.")
