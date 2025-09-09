users = {
    "john": {"email": "john@email.com", "password": "pass123", "online": False},
    "jane": {"email": "jane@email.com", "password": "pass456", "online": False},
    "bob": {"email": "bob@email.com", "password": "pass789", "online": False}
}
logged_in_users = []

def login_user(username, password):
    if username not in users:
        return "Username not found!"
    
    if users[username]["password"] != password:
        return "Wrong password!"
    
    users[username]["online"] = True
    if username not in logged_in_users:
        logged_in_users.append(username)
    
    return "Login successful!"

def logout_user(username):
    if username in logged_in_users:
        users[username]["online"] = False
        logged_in_users.remove(username)
        return "Logged out successfully!"
    return "User not logged in!"

def get_online_users():
    online = []
    for username, data in users.items():
        if data["online"]:
            online.append(username)
    return online

def check_user_status(username):
    if username not in users:
        return "User not found!"
    
    return "Online" if users[username]["online"] else "Offline"

def get_online_friends(username, friends_list):
    if username not in users:
        return "User not found!"
    
    online_friends = []
    for friend in friends_list:
        if friend in users and users[friend]["online"]:
            online_friends.append(friend)
    
    return online_friends

print(login_user("john", "pass123"))
print(login_user("jane", "pass456"))

print("Online users:", get_online_users())
print("John's status:", check_user_status("john"))
print("Bob's status:", check_user_status("bob"))

print(logout_user("john"))
print("Online users after logout:", get_online_users())