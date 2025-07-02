# Taking password from the user.
password = input("Enter password: ")

# It is condition to print.
if len(password) < 8:
    print("Weak")
elif "123" in password:
    print("Warn")
else:
    print("strong")