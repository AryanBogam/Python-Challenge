def parse_seat(seat_code):
    parts = seat_code.split("-")
    
    if len(parts) != 2:
        return "Invalid seat code format"
    
    coach = parts[0]
    try:
        seat_number = int(parts[1])
        return (coach, seat_number)
    except ValueError:
        return "Invalid seat number"

test_seats = ["B3-45", "S1-23", "A1-12", "C2-67", "X1-abc", "B3"]

print("COACH NUMBER EXTRACTOR")
print("-" * 30)

for seat_code in test_seats:
    result = parse_seat(seat_code)
    print(f"Seat code: '{seat_code}' → {result}")

print("\n" + "="*30)
user_seat = input("Enter seat code (format: C1-23): ")
result = parse_seat(user_seat)

if isinstance(result, tuple):
    coach, seat_num = result
    print(f"Coach: {coach}")
    print(f"Seat Number: {seat_num}")
else:
    print(f"Error: {result}")