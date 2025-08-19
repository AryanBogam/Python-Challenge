password = "Aryan123!"

has_lower = False
has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.islower():
        has_lower = True
    elif char.isupper():
        has_upper = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if has_lower and has_upper and has_digit and has_special:
    print("Strong password")
else:
    print("Weak password")