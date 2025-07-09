# Function to calculate factorial using a loop
def factorial_number(num):

    # Condition for the 1 , 0 or negative numbers
    if num < 0:
        return "Factorial is not defined for negative numbers"
    if num == 0 or num == 1:
        return 1
    
    # Calculate factorial using loop
    fact = 1
    for i in range(1,num + 1):
        fact *= i
    return fact

# Get input from user
num = int(input("Enter number: "))

# Calculate and display result
result = factorial_number(num)
print(result)