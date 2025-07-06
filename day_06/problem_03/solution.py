# Taking input of user age.
age = int(input("Enter your age: "))


# Conditions to print.
if age < 13:
    print("Too young ")
elif age <= 17:
    print("Teen – limited access ")
elif age <= 25:
    print("Young Builder – full access ")
else:
    print("Late start is better than no start ")
