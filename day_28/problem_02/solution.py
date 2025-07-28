users = {"john": "john@email.com", "mary": "mary@email.com"}

email = input("Enter email: ")

found = False
for username, user_email in users.items():
    if user_email == email:
        print(f"Username: {username}")
        found = True
        break

if not found:
    print("Email not registered")