# Validate password for length, number, and uppercase
password = input("Enter your password: ")

try:
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must include at least one number.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must include at least one uppercase letter.")
    print("Strong password")
except ValueError as e:
    print("Error:", e)
