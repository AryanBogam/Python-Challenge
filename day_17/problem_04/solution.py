def validate_email(email):
    return "@" in email and "." in email

def validate_password(password):
    return (len(password) >= 8 and 
            any(c.isupper() for c in password) and 
            any(c.isdigit() for c in password))

def login_system(email, password):
    if not validate_email(email):
        return False
    if not validate_password(password):
        return False
    return True

print(login_system("user@email.com", "Password123"))
print(login_system("invalid", "Password123"))
print(login_system("user@email.com", "weak"))