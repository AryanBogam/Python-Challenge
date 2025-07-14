try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format.")

    age = int(input("Enter age: "))
    if age <= 0:
        raise ValueError("Age must be greater than 0.")

    print("Form submitted successfully!")
except ValueError as e:
    print("Form Error:", e)
