def check_superhost_status(avg_rating, bookings):
    if avg_rating > 4.8 and bookings >= 50:
        return "Superhost"
    else:
        return "Regular Host"

avg_rating = 4.9
bookings = 60
result = check_superhost_status(avg_rating, bookings)
print(result)

print(check_superhost_status(4.9, 45))
print(check_superhost_status(4.7, 80))
print(check_superhost_status(4.8, 50))
print(check_superhost_status(4.85, 75))