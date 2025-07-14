# Keep asking for username until valid
while True:
    username = input("Enter a username: ")
    if not username.isalnum():
        print("Username must be alphanumeric.")
    elif " " in username:
        print("Username must not contain spaces.")
    else:
        print("Username accepted")
        break
