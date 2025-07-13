pin = input("Enter your 4-digit PIN: ")

try:
    # Check if PIN is all digits AND exactly 4 characters long
    if not (pin.isdigit() and len(pin) == 4):
        # Create custom error if validation fails
        raise ValueError("PIN must be exactly 4 digits.")
    print("PIN accepted")

except ValueError as e:
    print(e)