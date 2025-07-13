def validate_form():
    try:
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")

        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be positive.")

        # Get email and remove extra spaces
        email = input("Enter your email: ").strip()
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")

    # Show any validation errors
    except ValueError as e:
        print("Form Error:", e)
    
    else:
        print("Form submitted successfully!")
        print(f"Name: {name}, Age: {age}, Email: {email}")

validate_form()