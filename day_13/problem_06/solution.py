# Importing math library for square root function
import math

try:
    num = float(input("Enter a number: "))
    
    # Check if number is negative
    if num < 0:
        raise ValueError("Cannot take square root of negative number.")
    
    # Calculate and show square root
    print("Square root:", math.sqrt(num))

except ValueError as e:
    print(e)