def book_ticket(name, age, seat_pref):
    valid_seats = ["Window", "Middle", "Aisle"]

    if not name or name.strip() == "":
        return "Error: Name cannot be empty"

    if age < 0:
        return "Error: Age cannot be negative"

    if seat_pref not in valid_seats:
        return f"Warning: Seat preference must be one of {valid_seats}"

    return f"Ticket Booked for {name}"

test_cases = [
    ("Aryan", 20, "Window"),
    ("", 25, "Middle"),
    ("Priya", -5, "Aisle"),
    ("Raj", 30, "Corner")
]

print("TICKET BOOKING VALIDATOR")
print("-" * 30)

for name, age, seat in test_cases:
    result = book_ticket(name, age, seat)
    print(f"Name: '{name}', Age: {age}, Seat: '{seat}'")
    print(f"Result: {result}")
    print()

print("="*30)
print("BOOK YOUR TICKET")
name = input("Enter passenger name: ")
try:
    age = int(input("Enter age: "))
    seat_pref = input("Enter seat preference (Window/Middle/Aisle): ")
    
    result = book_ticket(name, age, seat_pref)
    print(f"\nBooking result: {result}")
except ValueError:
    print("Please enter valid age")