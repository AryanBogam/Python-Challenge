def check_password(password):
    errors = []
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    if len(password) < 8:
        errors.append("Must be at least 8 characters long")
    if not any(char.isupper() for char in password):
        errors.append("Must contain an uppercase letter")
    if not any(char.islower() for char in password):
        errors.append("Must contain a lowercase letter")
    if not any(char.isdigit() for char in password):
        errors.append("Must contain a digit")
    if not any(char in special_characters for char in password):
        errors.append("Must contain a special character")

    if not errors:
        return "Password is strong"
    else:
        return errors
print(check_password("Hello123"))
