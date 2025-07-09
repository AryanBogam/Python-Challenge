# Function to find the largest of three numbers
def find_maximum(num1,num2,num3):
    return max(num1,num2,num3)

# Get three numbers from the user
num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

# Display the maximum
result = find_maximum(num1,num2,num3)
print(f"The largest number is {result}")