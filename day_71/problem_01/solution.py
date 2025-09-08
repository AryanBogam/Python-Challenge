users = {}

def register_user(username, email, password):
    if username in users:
        return "Username already exists!"
    
    for user_data in users.values():
        if user_data["email"] == email:
            return "Email already exists!"
    
    users[username] = {
        "email": email,
        "password": password
    }
    return "Registration successful!"

print(register_user("john", "john@email.com", "pass123"))
print(register_user("jane", "jane@email.com", "pass456"))
print(register_user("john", "different@email.com", "pass789"))
print(users)