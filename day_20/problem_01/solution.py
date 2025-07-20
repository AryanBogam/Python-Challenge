
def validate_apple_id(email, password):
    if "@" not in email or "." not in email:
        return False, "Invalid email format"
    
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    banned_words = ["apple", "1234", "password"]
    password_lower = password.lower()
    
    for banned_word in banned_words:
        if banned_word in password_lower:
            return False, f"Password contains banned word: {banned_word}"
    
    return True, "Valid Apple ID"

print(validate_apple_id("john@gmail.com", "mystrongpass"))