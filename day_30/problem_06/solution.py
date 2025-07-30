seats = [
    ["Empty", "Taken", "Empty"],
    ["Taken", "Taken", "Empty"],
    ["Empty", "Empty", "Empty"]
]

empty_count = 0
for row in seats:
    for seat in row:
        if seat == "Empty":
            empty_count += 1

print(f"Total empty seats: {empty_count}")

print("Seat layout:")
for i, row in enumerate(seats):
    print(f"Row {i+1}: {row}")