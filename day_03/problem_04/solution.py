# It is given numbers
nums = (1, 4, 2, 1, 2, 5, 1, 3, 2, 1)

# Taking the user_input number.
user_input = int(input("Enter a number to count: "))

# Couting the user numbers in nums.
count = nums.count(user_input)

# Printing the Final answer.
print(f"Number {user_input} appears {count} times.")
