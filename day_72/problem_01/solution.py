users = {
    "john": {"email": "john@email.com", "password": "pass123"},
    "jane": {"email": "jane@email.com", "password": "pass456"}
}

def reset_password(username, email, new_password):
    if username not in users:
        return "Username not found!"
    
    if users[username]["email"] != email:
        return "Email does not match!"
    
    users[username]["password"] = new_password
    return "Password reset successfully!"

def verify_email_for_reset(username, email):
    if username not in users:
        return "Username not found!"
    
    if users[username]["email"] != email:
        return "Email does not match!"
    
    return "Email verified! You can now reset your password."

print(verify_email_for_reset("john", "john@email.com"))
print(reset_password("john", "john@email.com", "newpass123"))
print(users["john"])