# Function to determine if a number is even or odd
def check_odd_even(num):
    if num % 2 == 0:
        return("Even")
    else:
        return("Odd")

# Get a number from the user
num = int(input("Enter a number: "))

# Check and display the result
result = check_odd_even(num)
print(f"The number {num} is {result}")