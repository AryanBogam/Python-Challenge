def validate_guest_capacity(max_guests, guests):
    if guests > max_guests:
        return "Too many guests"
    else:
        return "Booking allowed"

max_guests = 4
guests = 5
result = validate_guest_capacity(max_guests, guests)
print(result)

print(validate_guest_capacity(4, 3))
print(validate_guest_capacity(6, 6))
print(validate_guest_capacity(2, 4))
print(validate_guest_capacity(8, 5))