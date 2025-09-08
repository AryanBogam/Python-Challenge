users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"}
}
logged_in_users = []

def login_user(username, password):
    if username not in users:
        return "Username not found!"
    
    if users[username]["password"] != password:
        return "Wrong password!"
    
    if username not in logged_in_users:
        logged_in_users.append(username)
    
    return "Login successful!"

def logout_user(username):
    if username in logged_in_users:
        logged_in_users.remove(username)
        return "Logged out successfully!"
    return "User not logged in!"

print(login_user("john", "pass123"))
print(login_user("jane", "wrongpass"))
print(logged_in_users)
print(logout_user("john"))
print(logged_in_users)