users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"},
    "aryan": {"email": "aryan@email.com", "password": "pass789"},
    "arjun": {"email": "arjun@email.com", "password": "pass101"},
    "bob": {"email": "bob@email.com", "password": "pass202"}
}

def search_users(search_term):
    search_term = search_term.lower()
    found_users = []
    
    for username in users:
        if search_term in username.lower():
            found_users.append(username)
    
    return found_users

print(search_users("ar"))
print(search_users("j"))
print(search_users("bob"))
print(search_users("xyz"))