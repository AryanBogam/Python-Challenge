email = input("Enter your email: ")

try:
    # Check if email has both @ and . symbols
    if "@" not in email or "." not in email:
        # Manually create an error if format is wrong
        raise ValueError("Invalid email format.")
    print("Email looks good")

# Catch the error we created and show the message
except ValueError as e:
    print(e)