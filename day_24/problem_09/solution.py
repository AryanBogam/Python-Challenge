seats = {}
total_seats = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C", "4A"]

bookings = [
    ("John", "1A"),
    ("Alice", "2B"), 
    ("Bob", "1A"),
    ("Charlie", "3C")
]

print("Seat allocation:")
for passenger, seat in bookings:
    if seat in seats:
        print(f"{passenger} wants {seat} - already booked by {seats[seat]}")
    else:
        seats[seat] = passenger
        print(f"{passenger} allocated seat {seat}")

print(f"\nAllocated seats:")
for seat, passenger in seats.items():
    print(f"{seat}: {passenger}")

print(f"\nAvailable seats:")
for seat in total_seats:
    if seat not in seats:
        print(seat)