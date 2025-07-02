# Taking info from the user.
age = int(input("Enter age: "))
hours = int(input("Daily learning hours: "))
dream = input("Dream(AI/Web3/Crypto/Automation): ")

# Conditions to assign value in focus.
if hours < 2:
    focus = ("Low focus")
elif 2<hours<4:
    focus = ("Moderate focus")
else:
    focus = ("High achiever")

# It is printing the final answer.
print(f"At age {age}, with {focus}, Aryan is on track to dominate {dream}")